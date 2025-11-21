# src/fi_fs/normalise.py
from __future__ import annotations
import re
from collections import defaultdict
from typing import Dict, List, Tuple, Optional, Any

Triplet = Tuple[str, List[str], str]  # (op, args, conn)

# Default alias map.
DEFAULT_ALIAS_MAP: Dict[str, str] = {
    "/bin/busybox": "busybox",
    "python3": "python",
}

FILE_OPERATORS = {
    "chmod", "chown", "chgrp", "rm", "cat", "head", "tail", "cp", "mv", "touch", "tee",
}

# Flags on executed binaries that commonly take arbitrary text values
EXEC_FLAG_TAKES_VALUE = {
    "-p", "--pass", "--password", "--rig-id", "--rig", "--worker", "-w",
    "--device-name", "--worker-name",
}


def apply_aliases(
    seqs_by_sid: Dict[str, List[Triplet]],
    alias_map: Optional[Dict[str, str]] = None,
    *,
    return_changes: bool = True,
) -> Tuple[Dict[str, List[Triplet]], Optional[List[Tuple[str, str, str, str]]]]:
    """
    Apply an operator alias map to every (op, args, conn) triplet.

    Parameters
    ----------
    seqs_by_sid : dict[session -> list of triplets]
    alias_map   : dict of {from_op -> to_op}; if None, uses DEFAULT_ALIAS_MAP
    return_changes : whether to return a list of (sid, before, '->', after)

    Returns
    -------
    seqs_alias : dict with ops canonicalised
    changes    : list of (sid, old_op, '->', new_op) or None
    """
    amap = alias_map or DEFAULT_ALIAS_MAP
    out: Dict[str, List[Triplet]] = {}
    changes: List[Tuple[str, str, str, str]] = [] if return_changes else None

    for sid, trips in seqs_by_sid.items():
        new_trips: List[Triplet] = []
        for (op, args, conn) in trips:
            op2 = amap.get(op, op)
            if return_changes and op2 != op:
                changes.append((sid, op, "->", op2))
            new_trips.append((op2, args, conn))
        out[sid] = new_trips

    return out, changes


# ----------------------------------------------
# Typed placeholders on ARGS only
# ----------------------------------------------

# Recognisers (strong, whole-token matches)
PH_PATTERNS = {
    "URL":    re.compile(r"^(?:https?|ftp)://\S+$", re.I),
    "IP":     re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$"),
    "HOST":   re.compile(r"^(?=.{1,253}$)(?!-)[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+$"),
    "EXEC":   re.compile(r"^[A-Za-z0-9._-]+\.(?:sh|py|pl|exe|bin)$", re.I),
    "SUBCMD": re.compile(r"^\$\(.+\)$"),  # e.g., $(which ls)
    "PORT":   re.compile(r"^:\d{1,5}$"),
}

# host:port (whole token, no slash)
HOSTPORT_RX = re.compile(r"""
    ^
    (?P<host>(?:(?:\d{1,3}\.){3}\d{1,3})|(?:[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+|localhost))
    :
    (?P<port>\d{1,5})
    $
""", re.X)

_BARE_FILENAME_RX = re.compile(r"^[A-Za-z0-9._-]{1,128}$")

# Hex-escape payload: >= 8 bytes of \xHH (optionally quoted)
HEX_ESC_RX = re.compile(r"^(?:['\"])?(?:\\x[0-9A-Fa-f]{2}){8,}(?:['\"])??$")

# username:password (simple, whole token)
USERPASS_RX = re.compile(r'^([A-Za-z0-9._-]{1,32}):([^\s]{1,256})$')

# BusyBox “marker” heuristic: 4–8 uppercase letters, not a real applet name.
BUSYBOX_MARKER_RX = re.compile(r"^[A-Z]{4,8}$")
KNOWN_APPLETS = {
    "sh","ash","bash","zsh","echo","cat","dd","chmod","cp","mv","rm","ls","cd",
    "tftp","wget","mkdir","sleep","kill","ps","env","uname","true","false"
}


# Embedded patterns (appear anywhere inside a token)
EMBEDDED_IP_RX  = re.compile(r"(?<!\d)(?:\d{1,3}\.){3}\d{1,3}(?!\d)")
EMBEDDED_URL_RX = re.compile(r"(?:https?|ftp)://\S+", re.I)

def _is_printable_ascii(s: str) -> bool:
    return bool(s) and all(32 <= ord(ch) <= 126 for ch in s)

def _is_bare_filename(tok: str) -> bool:
    # No spaces, no slashes, no shell metachars; common filename chars only.
    return bool(_BARE_FILENAME_RX.fullmatch(tok))

def _looks_like_path(tok: str) -> bool:
    if not isinstance(tok, str) or not tok:
        return False
    return (
        tok.startswith("/")
        or tok.startswith("./")
        or tok.startswith("../")
        or tok.startswith("~")
        or ("/" in tok)
    )

def _mark_placeholder(tok: str) -> Tuple[str, Optional[str]]:
    """
    Map a literal token to a typed-with-value placeholder 'PH_<TYPE>::<value>'.
    Returns (new_token, reason) where reason is a short label for debug, or None.
    Only apply to ARGUMENTS (operators are handled upstream via alias map).
    """
    if not isinstance(tok, str):
        return tok, None

    # Strong patterns first (whole-token)
    if PH_PATTERNS["URL"].match(tok):    return f"PH_URL::{tok}", "URL"
    if PH_PATTERNS["IP"].match(tok):     return f"PH_IP::{tok}", "IP"
    if PH_PATTERNS["PORT"].match(tok):   return f"PH_PORT::{tok}", "PORT"
    if PH_PATTERNS["EXEC"].match(tok):   return f"PH_EXEC::{tok}", "EXEC"
    if PH_PATTERNS["SUBCMD"].match(tok): return f"PH_SUBCMD::{tok}", "SUBCMD"
    if tok.lower() == "localhost":       return f"PH_HOST::{tok}", "HOST"
    if PH_PATTERNS["HOST"].match(tok):   return f"PH_HOST::{tok}", "HOST"

    # host:port (no slash)
    if HOSTPORT_RX.match(tok):
        return f"PH_HOSTPORT::{tok}", "HOSTPORT"

    # Scheme-less URL (host/ip + path)
    if "/" in tok:
        head, _ = tok.split("/", 1)
        if (PH_PATTERNS["IP"].match(head)
            or PH_PATTERNS["HOST"].match(head)
            or head.lower() == "localhost"):
            return f"PH_URL::{tok}", "URL_SCHEMELESS"

    # Special-case: simple './file' (no subdirs) → treat as EXEC
    if tok.startswith("./") and "/" not in tok[2:]:
        return f"PH_EXEC::{tok}", "EXEC_DOT"

    # Generic path catch-all
    if _looks_like_path(tok):
        return f"PH_PATH::{tok}", "PATH"

    # Embedded literals anywhere inside the token
    if EMBEDDED_URL_RX.search(tok):
        return f"PH_EMBURL::{tok}", "EMBURL"
    if EMBEDDED_IP_RX.search(tok):
        return f"PH_EMBIP::{tok}", "EMBIP"

    # Otherwise literal
    return tok, None


# Port number validator
def _is_port_token(s: Any) -> bool:
    if not isinstance(s, str) or not s.isdigit():
        return False
    try:
        v = int(s)
        return 1 <= v <= 65535
    except ValueError:
        return False



def apply_placeholders_args_only(
    seqs_by_sid: Dict[str, List[Triplet]],
    *,
    debug: bool = False,
    preview_changed_first_n_sessions: int = 10,
    sample_per_reason: int = 8,
) -> Tuple[Dict[str, List[Triplet]], Optional[Dict[str, Any]]]:
    """
    Apply placeholder mapping to ARGS only. (Operators are left intact, except pragmatic promotions.)
    (With pragmatic tweaks:
      - BusyBox nonce marker mapping
      - Exec promotion for './name' basenames (incl. when './name' is the OP)
      - Exec promotion for any path-like operator (absolute or contains '/')
      - Echo password-sequence coarsening (prefix\\nX\\nX[\\n])
      - Echo printable text piped/redirected (no length cap) → PH_ECHO_TXT
      - bash/sh -s <printable> → PH_BASH_ARG
      - Bare filename operands for common file ops → PH_PATH::<name>
      - Port coarsening for tftp/busybox tftp/ftpget -P
    """
    # Recogniser for echo "prefix\nX\nX[\n]" payload after bashlex tokenisation:
    # token looks like: <anything-no-spaces>n<PASS>n<SAMEPASS>[n]
    ECHO_PASSSEQ_RX = re.compile(r'^[^\s]*n([A-Za-z0-9@._+$-]{6,})n\1n?$')

    # Small helpers local to this function (to avoid cross-file edits)
    FILE_OPERATORS = {
        "chmod", "chown", "chgrp", "rm", "cat", "head", "tail", "cp", "mv", "touch", "tee",
    }
    _BARE_FILENAME_RX = re.compile(r"^[A-Za-z0-9._-]{1,128}$")

    def _is_printable_ascii(s: str) -> bool:
        return bool(s) and all(32 <= ord(ch) <= 126 for ch in s)

    def _is_bare_filename(tok: str) -> bool:
        return isinstance(tok, str) and bool(_BARE_FILENAME_RX.fullmatch(tok))

    seqs_ph_local: Dict[str, List[Triplet]] = {}
    reason_counts = defaultdict(int)
    reason_examples = defaultdict(list)
    session_change_examples: List[Tuple[str, List[Tuple[str, str, str, str, str, str]]]] = []

    for sid, seq_trips in seqs_by_sid.items():
        # Collect basenames that appear as './name' anywhere in this session (no subdirs)
        exec_basenames = {
            a[2:] for (_op0, args0, _c0) in seq_trips for a in (args0 or [])
            if isinstance(a, str) and a.startswith("./") and "/" not in a[2:]
        }

        out_trips: List[Triplet] = []
        session_changes: List[Tuple[str, str, str, str, str, str]] = []

        for i, (op, args, conn) in enumerate(seq_trips):

            # BusyBox nonce → stable marker
            if op in ("busybox", "/bin/busybox") and args:
                first = args[0]
                if BUSYBOX_MARKER_RX.match(first) and first.lower() not in KNOWN_APPLETS:
                    args = ["PH_MARKER::BUSYBOX"] + args[1:]
                    if debug:
                        reason_counts["BUSYBOX_MARKER"] += 1
                        if len(reason_examples["BUSYBOX_MARKER"]) < sample_per_reason:
                            reason_examples["BUSYBOX_MARKER"].append((sid, first, "PH_MARKER::BUSYBOX"))

            # Promote OP if it is a simple './name'
            op2 = op
            if isinstance(op, str) and op.startswith("./") and "/" not in op[2:]:
                basename = op[2:]
                promoted_op = f"PH_EXEC::./{basename}"
                if debug:
                    reason_counts["EXEC_PROMOTE_OP"] += 1
                    if len(reason_examples["EXEC_PROMOTE_OP"]) < sample_per_reason:
                        reason_examples["EXEC_PROMOTE_OP"].append((sid, op, promoted_op))
                    if len(session_change_examples) < preview_changed_first_n_sessions:
                        session_changes.append(("OP", op, promoted_op, "EXEC_PROMOTE_OP", op, conn))
                op2 = promoted_op

            # NEW: Promote OP if it looks like a path (absolute or contains '/')
            if isinstance(op2, str) and _looks_like_path(op2):
                promoted_op = f"PH_EXEC::{op2}"
                if debug:
                    reason_counts["OP_EXEC_PATH"] += 1
                    if len(reason_examples["OP_EXEC_PATH"]) < sample_per_reason:
                        reason_examples["OP_EXEC_PATH"].append((sid, op2, promoted_op))
                    if len(session_change_examples) < preview_changed_first_n_sessions:
                        session_changes.append(("OP", op2, promoted_op, "OP_EXEC_PATH", op2, conn))
                op2 = promoted_op

            # Coarsen echo password-sequence "prefix\nX\nX[\n]" → PH_ECHO_PASSSEQ
            if op2 == "echo" and args:
                # skip leading -e/-ne/-en if present
                start_i = 1 if args[0] in ("-e", "-ne", "-en") else 0
                if start_i < len(args):
                    a0 = args[start_i]
                    if isinstance(a0, str) and ECHO_PASSSEQ_RX.match(a0):
                        old = a0
                        args = list(args)  # copy before mutate
                        args[start_i] = "PH_ECHO_PASSSEQ"
                        if debug:
                            reason_counts["ECHO_PASSSEQ"] += 1
                            if len(reason_examples["ECHO_PASSSEQ"]) < sample_per_reason:
                                reason_examples["ECHO_PASSSEQ"].append((sid, old, "PH_ECHO_PASSSEQ"))
                            if len(session_change_examples) < preview_changed_first_n_sessions:
                                session_changes.append(("ARG", old, "PH_ECHO_PASSSEQ", "ECHO_PASSSEQ", op2, conn))

            # Coarsen echo payloads, including BusyBox applet form and trailing \c
            if args and (
                op2 == "echo" or
                (op2 in ("busybox", "/bin/busybox") and len(args) >= 1 and args[0] == "echo")
            ):
                # base index (busybox echo shifts args by +1)
                base = 0 if op2 == "echo" else 1

                # account for leading -e/-ne/-en/-n
                flag_i = base
                start_i = flag_i + 1 if len(args) > flag_i and args[flag_i] in ("-e", "-ne", "-en", "-n") else base

                if start_i < len(args):
                    a0 = args[start_i]
                    if isinstance(a0, str):
                        # local helpers
                        def _strip_basic_quotes(s: str) -> str:
                            if len(s) >= 2 and s[0] in "'\"" and s[-1] == s[0]:
                                return s[1:-1]
                            if s.startswith("$'") and s.endswith("'") and len(s) >= 3:
                                return s[2:-1]
                            return s

                        def _normalise_backslashes(s: str) -> str:
                            prev = None
                            cur = s
                            while prev != cur:
                                prev = cur
                                cur = cur.replace("\\\\", "\\")
                            return cur

                        def _strip_trailing_c(s: str) -> str:
                            s2 = _normalise_backslashes(s)
                            return s2[:-2] if s2.endswith("\\c") else s2

                        # normalised views
                        raw = a0
                        unq = _strip_basic_quotes(raw)
                        norm_no_c = _strip_trailing_c(unq)

                        # HEX blob detection (robust to multiple escaping; allows short blobs if dense)
                        parts = re.findall(r'\\x[0-9A-Fa-f]{2}', _normalise_backslashes(norm_no_c))
                        byte_count = len(parts)
                        hex_chars = byte_count * 4
                        density = (hex_chars / max(1, len(norm_no_c))) if norm_no_c else 0.0
                        is_hex_blob = byte_count >= 3 or density >= 0.6

                        changed = False

                        if is_hex_blob:
                            old = a0
                            args = list(args)
                            args[start_i] = "PH_HEXDATA"
                            changed = True
                            if debug:
                                reason_counts["ECHO_HEX"] += 1
                                if len(reason_examples["ECHO_HEX"]) < sample_per_reason:
                                    reason_examples["ECHO_HEX"].append((sid, old, "PH_HEXDATA"))
                                if len(session_change_examples) < preview_changed_first_n_sessions:
                                    session_changes.append(("ARG", old, "PH_HEXDATA", "ECHO_HEX", op2, conn))

                        # echo "user:pass" | chpasswd  → PH_CHPASSWD
                        elif conn == "|" and i + 1 < len(seq_trips):
                            next_op, _na, _nc = seq_trips[i + 1]
                            if next_op == "chpasswd":
                                a0_stripped = _strip_basic_quotes(raw)
                                if USERPASS_RX.match(a0_stripped):
                                    old = a0
                                    args = list(args)
                                    args[start_i] = "PH_CHPASSWD"
                                    changed = True
                                    if debug:
                                        reason_counts["ECHO_USERPASS"] += 1
                                        if len(reason_examples["ECHO_USERPASS"]) < sample_per_reason:
                                            reason_examples["ECHO_USERPASS"].append((sid, old, "PH_CHPASSWD"))
                                        if len(session_change_examples) < preview_changed_first_n_sessions:
                                            session_changes.append(
                                                ("ARG", old, "PH_CHPASSWD", "ECHO_USERPASS", op2, conn))

                        # Printable echo payload piped to next command → PH_ECHO_TXT (length-agnostic)
                        if not changed and op2 == "echo" and conn == "|" and args:
                            start_i2 = 1 if args and args[0] in ("-e", "-ne", "-en", "-n") else 0
                            if start_i2 < len(args):
                                raw_payload = args[start_i2]
                                if isinstance(raw_payload, str):
                                    payload_unquoted = _strip_basic_quotes(raw_payload)
                                    payload_norm = _strip_trailing_c(payload_unquoted)
                                    if _is_printable_ascii(payload_norm):
                                        old = raw_payload
                                        args = list(args)
                                        args[start_i2] = "PH_ECHO_TXT"
                                        changed = True
                                        if debug:
                                            reason_counts["ECHO_TXT_PIPE"] += 1
                                            if len(reason_examples["ECHO_TXT_PIPE"]) < sample_per_reason:
                                                reason_examples["ECHO_TXT_PIPE"].append((sid, old, "PH_ECHO_TXT"))
                                            if len(session_change_examples) < preview_changed_first_n_sessions:
                                                session_changes.append(
                                                    ("ARG", old, "PH_ECHO_TXT", "ECHO_TXT_PIPE", op2, conn)
                                                )

                        # Printable text redirected to a file → PH_ECHO_TXT  (no length cap)
                        if not changed:
                            if start_i + 2 < len(args) and args[start_i + 1] in (">", ">>") and isinstance(args[start_i + 2], str):
                                s = norm_no_c  # unquoted, trailing \c removed
                                if _is_printable_ascii(s):
                                    old = a0
                                    args = list(args)
                                    args[start_i] = "PH_ECHO_TXT"
                                    changed = True
                                    if debug:
                                        reason_counts["ECHO_TXT"] += 1
                                        if len(reason_examples["ECHO_TXT"]) < sample_per_reason:
                                            reason_examples["ECHO_TXT"].append((sid, old, "PH_ECHO_TXT"))
                                        if len(session_change_examples) < preview_changed_first_n_sessions:
                                            session_changes.append(("ARG", old, "PH_ECHO_TXT", "ECHO_TXT", op2, conn))

                        # BusyBox echo (applet) printable literal redirected → PH_ECHO_TXT (no length cap)
                        if not changed and op2 in ("busybox", "/bin/busybox") and args and len(args) >= 4:
                            if args[0] == "echo" and args[2] in (">", ">>"):
                                lit = args[1]
                                if isinstance(lit, str) and not lit.startswith("PH_"):
                                    # collapse multi-escaped backslashes: '\\\\c' -> '\\c' -> '\c'
                                    lit_norm = lit
                                    prev = None
                                    while prev != lit_norm:
                                        prev = lit_norm
                                        lit_norm = lit_norm.replace("\\\\", "\\")
                                    # strip trailing \c (BusyBox "no newline")
                                    core = lit_norm[:-2] if lit_norm.endswith("\\c") else lit_norm
                                    if core == "" or _is_printable_ascii(core):
                                        old = lit
                                        a2 = list(args)
                                        a2[1] = "PH_ECHO_TXT"
                                        args = a2
                                        changed = True
                                        if debug:
                                            reason_counts["ECHO_BB_REDIR"] += 1
                                            if len(reason_examples["ECHO_BB_REDIR"]) < sample_per_reason:
                                                reason_examples["ECHO_BB_REDIR"].append((sid, old, "PH_ECHO_TXT"))
                                            if len(session_change_examples) < preview_changed_first_n_sessions:
                                                session_changes.append(
                                                    ("ARG", old, "PH_ECHO_TXT", "ECHO_BB_REDIR", op2, conn))

            # Coarsen explicit port numbers for tftp / busybox tftp / ftpget -P
            if args:
                # tftp ... <PORT> ...
                if op2 == "tftp":
                    a2 = list(args)
                    for j, a in enumerate(a2):
                        if _is_port_token(a):
                            old = a
                            a2[j] = "PH_PORT"
                            if debug:
                                reason_counts["PORT_TFTP"] += 1
                                if len(reason_examples["PORT_TFTP"]) < sample_per_reason:
                                    reason_examples["PORT_TFTP"].append((sid, old, "PH_PORT"))
                                if len(session_change_examples) < preview_changed_first_n_sessions:
                                    session_changes.append(("ARG", old, "PH_PORT", "PORT_TFTP", op2, conn))
                    args = a2

                # busybox tftp ... <PORT> ...
                elif op2 == "busybox" and len(args) >= 2 and args[0] == "tftp":
                    a2 = list(args)
                    for j in range(1, len(a2)):  # scan after 'tftp'
                        a = a2[j]
                        if _is_port_token(a):
                            old = a
                            a2[j] = "PH_PORT"
                            if debug:
                                reason_counts["PORT_BB_TFTP"] += 1
                                if len(reason_examples["PORT_BB_TFTP"]) < sample_per_reason:
                                    reason_examples["PORT_BB_TFTP"].append((sid, old, "PH_PORT"))
                                if len(session_change_examples) < preview_changed_first_n_sessions:
                                    session_changes.append(("ARG", old, "PH_PORT", "PORT_BB_TFTP", op2, conn))
                    args = a2

                # ftpget ... -P <PORT> ...
                elif op2 == "ftpget":
                    a2 = list(args)
                    for j in range(len(a2) - 1):
                        if a2[j] == "-P" and _is_port_token(a2[j + 1]):
                            old = a2[j + 1]
                            a2[j + 1] = "PH_PORT"
                            if debug:
                                reason_counts["PORT_FTPGET"] += 1
                                if len(reason_examples["PORT_FTPGET"]) < sample_per_reason:
                                    reason_examples["PORT_FTPGET"].append((sid, old, "PH_PORT"))
                                if len(session_change_examples) < preview_changed_first_n_sessions:
                                    session_changes.append(("ARG", old, "PH_PORT", "PORT_FTPGET", op2, conn))
                    args = a2

            # Args mapping (order preserved)
            new_args: List[str] = []
            for j, a in enumerate(args):
                if isinstance(a, str) and a in exec_basenames:
                    promoted = f"PH_EXEC::./{a}"
                    if debug:
                        reason_counts["EXEC_PROMOTE"] += 1
                        if len(reason_examples["EXEC_PROMOTE"]) < sample_per_reason:
                            reason_examples["EXEC_PROMOTE"].append((sid, a, promoted))
                        if len(session_change_examples) < preview_changed_first_n_sessions:
                            session_changes.append(("ARG", a, promoted, "EXEC_PROMOTE", op2, conn))
                    new_a, reason = promoted, "EXEC_PROMOTE"

                # NEW: bash/sh -s <printable> → PH_BASH_ARG
                elif op2 in ("bash", "sh") and isinstance(a, str):
                    if len(args) >= 2 and args[0] == "-s" and j == 1 and not a.startswith("PH_") and _is_printable_ascii(a):
                        promoted = "PH_BASH_ARG"
                        if debug:
                            reason_counts["BASH_S_ARG"] += 1
                            if len(reason_examples["BASH_S_ARG"]) < sample_per_reason:
                                reason_examples["BASH_S_ARG"].append((sid, a, promoted))
                            if len(session_change_examples) < preview_changed_first_n_sessions:
                                session_changes.append(("ARG", a, promoted, "BASH_S_ARG", op2, conn))
                        new_a, reason = promoted, "BASH_S_ARG"
                    else:
                        new_a, reason = _mark_placeholder(a)
                        if debug and reason and len(session_change_examples) < preview_changed_first_n_sessions:
                            session_changes.append(("ARG", a, new_a, reason, op2, conn))

                # NEW: Executed script first nonce-ish arg → PH_EXEC_ARG
                # Case A: operator is a promoted executable (PH_EXEC::<path> or PH_EXEC_<n>), coarsen first positional arg
                elif isinstance(op2, str) and (
                        op2.startswith("PH_EXEC::") or op2.startswith("PH_EXEC_")) and isinstance(a, str):
                    if j == 0 and not a.startswith("PH_") and not a.startswith("-") and _is_printable_ascii(a):
                        promoted = "PH_EXEC_ARG"
                        if debug:
                            reason_counts["EXEC_FIRST_ARG"] += 1
                            if len(reason_examples["EXEC_FIRST_ARG"]) < sample_per_reason:
                                reason_examples["EXEC_FIRST_ARG"].append((sid, a, promoted))
                            if len(session_change_examples) < preview_changed_first_n_sessions:
                                session_changes.append(("ARG", a, promoted, "EXEC_FIRST_ARG", op2, conn))
                        new_a, reason = promoted, "EXEC_FIRST_ARG"
                    else:
                        new_a, reason = _mark_placeholder(a)
                        if debug and reason and len(session_change_examples) < preview_changed_first_n_sessions:
                            session_changes.append(("ARG", a, new_a, reason, op2, conn))

                # Case B: `sh|bash <exec> <nonce>` — if first arg is an exec placeholder, coarsen the *second* arg
                elif op2 in ("sh", "bash") and isinstance(a, str):
                    if (len(args) >= 2 and j == 1 and isinstance(args[0], str)
                            and (args[0].startswith("PH_EXEC::") or args[0].startswith("PH_EXEC_"))
                            and not a.startswith("PH_") and not a.startswith("-") and _is_printable_ascii(a)):
                        promoted = "PH_EXEC_ARG"
                        if debug:
                            reason_counts["EXEC_FIRST_ARG"] += 1
                            if len(reason_examples["EXEC_FIRST_ARG"]) < sample_per_reason:
                                reason_examples["EXEC_FIRST_ARG"].append((sid, a, promoted))
                            if len(session_change_examples) < preview_changed_first_n_sessions:
                                session_changes.append(("ARG", a, promoted, "EXEC_FIRST_ARG", op2, conn))
                        new_a, reason = promoted, "EXEC_FIRST_ARG"
                    else:
                        new_a, reason = _mark_placeholder(a)
                        if debug and reason and len(session_change_examples) < preview_changed_first_n_sessions:
                            session_changes.append(("ARG", a, new_a, reason, op2, conn))

                # NEW: Coarsen values for specific flags when executing a promoted binary
                elif isinstance(a, str) and (
                        (isinstance(op2, str) and (op2.startswith("PH_EXEC::") or op2.startswith("PH_EXEC_")))
                        or (
                                op2 in ("sh", "bash")
                                and len(args) >= 2
                                and isinstance(args[0], str)
                                and (args[0].startswith("PH_EXEC::") or args[0].startswith("PH_EXEC_"))
                        )
                ):
                    # only flag-value coarsening here (j >= 1 case), else _mark_placeholder(...)
                    if j >= 1 and isinstance(args[j - 1], str) and args[j - 1] in EXEC_FLAG_TAKES_VALUE \
                            and not a.startswith("PH_") and not a.startswith("-") and _is_printable_ascii(a):
                        promoted = "PH_EXEC_FLAGVAL"
                        if debug:
                            reason_counts["EXEC_FLAGVAL"] += 1
                            if len(reason_examples["EXEC_FLAGVAL"]) < sample_per_reason:
                                reason_examples["EXEC_FLAGVAL"].append((sid, a, promoted))
                            if len(session_change_examples) < preview_changed_first_n_sessions:
                                session_changes.append(("ARG", a, promoted, "EXEC_FLAGVAL", op2, conn))
                        new_a, reason = promoted, "EXEC_FLAGVAL"
                    else:
                        new_a, reason = _mark_placeholder(a)
                        if debug and reason and len(session_change_examples) < preview_changed_first_n_sessions:
                            session_changes.append(("ARG", a, new_a, reason, op2, conn))


                # NEW: For promoted executables (PH_EXEC::<path>), coarsen values of specific flags (e.g., -p)
                elif isinstance(op2, str) and op2.startswith("PH_EXEC::") and isinstance(a, str):
                    # If current arg is the value for a previous flag that takes a value, coarsen it.
                    if j >= 1 and isinstance(args[j - 1], str) and args[j - 1] in EXEC_FLAG_TAKES_VALUE \
                       and not a.startswith("PH_") and not a.startswith("-") and _is_printable_ascii(a):
                        promoted = "PH_EXEC_FLAGVAL"
                        if debug:
                            reason_counts["EXEC_FLAGVAL"] += 1
                            if len(reason_examples["EXEC_FLAGVAL"]) < sample_per_reason:
                                reason_examples["EXEC_FLAGVAL"].append((sid, a, promoted))
                            if len(session_change_examples) < preview_changed_first_n_sessions:
                                session_changes.append(("ARG", a, promoted, "EXEC_FLAGVAL", op2, conn))
                        new_a, reason = promoted, "EXEC_FLAGVAL"
                    else:
                        new_a, reason = _mark_placeholder(a)
                        if debug and reason and len(session_change_examples) < preview_changed_first_n_sessions:
                            session_changes.append(("ARG", a, new_a, reason, op2, conn))



                # NEW: context-aware bare filename operands for common file operators
                elif op2 in FILE_OPERATORS and isinstance(a, str) and not a.startswith("PH_"):
                    if a.startswith("-"):
                        new_a, reason = a, None  # flags untouched
                    elif op2 == "chmod" and j == 0 and a.isdigit():
                        new_a, reason = a, None  # chmod mode (e.g., 777) untouched
                    elif _is_bare_filename(a):
                        promoted = f"PH_PATH::{a}"
                        if debug:
                            reason_counts["FILE_BARE_OPND"] += 1
                            if len(reason_examples["FILE_BARE_OPND"]) < sample_per_reason:
                                reason_examples["FILE_BARE_OPND"].append((sid, a, promoted))
                            if len(session_change_examples) < preview_changed_first_n_sessions:
                                session_changes.append(("ARG", a, promoted, "FILE_BARE_OPND", op2, conn))
                        new_a, reason = promoted, "FILE_BARE_OPND"
                    else:
                        new_a, reason = _mark_placeholder(a)
                        if debug and reason and len(session_change_examples) < preview_changed_first_n_sessions:
                            session_changes.append(("ARG", a, new_a, reason, op2, conn))

                else:
                    new_a, reason = _mark_placeholder(a)
                    if debug and reason and len(session_change_examples) < preview_changed_first_n_sessions:
                        session_changes.append(("ARG", a, new_a, reason, op2, conn))

                if debug and reason:
                    reason_counts[reason] += 1
                    if len(reason_examples[reason]) < sample_per_reason:
                        reason_examples[reason].append((sid, a, new_a))
                new_args.append(new_a)

            out_trips.append((op2, new_args, conn))

        seqs_ph_local[sid] = out_trips
        if debug and session_changes and len(session_change_examples) < preview_changed_first_n_sessions:
            session_change_examples.append((sid, session_changes))

    debug_info = None
    if debug:
        debug_info = {
            "total_changed": int(sum(reason_counts.values())),
            "reason_counts": dict(sorted(reason_counts.items(), key=lambda x: (-x[1], x[0]))),
            "reason_examples": dict(reason_examples),
            "session_change_examples": session_change_examples,
        }

    return seqs_ph_local, debug_info


def assert_connectors_preserved(
    before: Dict[str, List[Triplet]],
    after: Dict[str, List[Triplet]],
) -> None:
    """
    Integrity check: triplet counts & connectors preserved 1:1.
    """
    for sid in before:
        if len(before[sid]) != len(after[sid]):
            raise AssertionError(f"Triplet count changed for session {sid}")
        for (_, _, c1), (_, _, c2) in zip(before[sid], after[sid]):
            if c1 != c2:
                raise AssertionError(f"Connector altered during placeholder mapping for session {sid}")


# ----------------------------------------------
# α-renumber placeholders per session
# ----------------------------------------------

NUM_PH_RE   = re.compile(r'^(PH_[A-Z]+)_(\d+)$')   # PH_URL_1
TYPED_PH_RE = re.compile(r'^(PH_[A-Z]+)::(.+)$')   # PH_URL::value

def alpha_renumber(
    seqs_by_sid: Dict[str, List[Triplet]],
    *,
    check_idempotent: bool = True,
) -> Dict[str, List[Triplet]]:
    """
    Assign per-session numbers to each distinct typed-with-value placeholder.
    Keeps already-numbered tokens as-is. Optionally asserts idempotence.

    Returns
    -------
    seqs_alpha : dict with placeholders renumbered per session
    """
    def renumber_one_sequence(seq_trips: List[Triplet]) -> List[Triplet]:
        counters = defaultdict(int)    # base -> next index
        mapping  = {}                  # full typed token -> numbered

        def renumber_token(tok: str) -> str:
            if not isinstance(tok, str):
                return tok
            if NUM_PH_RE.match(tok):               # already numbered
                return tok
            m = TYPED_PH_RE.match(tok)
            if m:                                  # typed-with-value
                base = m.group(1)                  # e.g., PH_URL
                full = tok                         # whole 'PH_URL::...'
                if full not in mapping:
                    counters[base] += 1
                    mapping[full] = f"{base}_{counters[base]}"
                return mapping[full]
            return tok

        out: List[Triplet] = []
        for op, args, conn in seq_trips:
            op2   = renumber_token(op)
            args2 = [renumber_token(a) for a in args]
            out.append((op2, args2, conn))
        return out

    seqs_alpha: Dict[str, List[Triplet]] = {sid: renumber_one_sequence(trips) for sid, trips in seqs_by_sid.items()}

    if check_idempotent:
        for sid, trips in seqs_alpha.items():
            again = {sid: renumber_one_sequence(trips)}[sid]
            if again != trips:
                raise AssertionError(f"α-renumbering not idempotent for session {sid}")

    return seqs_alpha
