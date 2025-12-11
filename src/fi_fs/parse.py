# src/fi_fs/parse.py
from __future__ import annotations

import platform
import bashlex
import sys
import pandas as pd
from typing import Dict, List, Tuple, Any, Optional
from .io import parse_safe_minimal

Triplet = Tuple[str, List[str], str]  # (op, args, conn)
CONNECTOR_TOKENS = {";", "&&", "||", "|"}

try:
    # bashlex usually exposes __version__
    import importlib.metadata as importlib_metadata  # Py3.8+
except ImportError:  # pragma: no cover (older Python)
    import importlib_metadata  # type: ignore


# --- Python version ---
py_impl = sys.implementation.name  # e.g. "cpython"
py_version = platform.python_version()  # e.g. "3.12.3"

print(f"PYTHON: {py_impl} {py_version}")

# --- bashlex version ---
bashlex_version = getattr(bashlex, "__version__", None)
if bashlex_version is None:
    try:
        bashlex_version = importlib_metadata.version("bashlex")
    except Exception:
        bashlex_version = "unknown"

print(f"BASHLEX: {bashlex_version}")


# ---------------------------
# Bashlex parsing
# ---------------------------
def try_parse(script: str) -> Tuple[bool, Optional[List[Any]], Optional[str]]:
    """
    Parse a single newline-joined session string with bashlex.

    Returns
    -------
    ok : bool
    parts : list | None
        bashlex AST roots if ok.
    err : str | None
        Error message if not ok.
    """
    try:
        parts = bashlex.parse(script)
        return True, parts, None
    except Exception as e:  # noqa: BLE001 (we want the exact parser error string)
        return False, None, f"{type(e).__name__}: {e}"


def parse_all_sessions(
    agg_df: pd.DataFrame,
    *,
    progress: bool = True,
    strict: bool = True,
) -> Tuple[Dict[str, List[Any]], pd.DataFrame, List[Tuple[str, str, str]]]:
    """
    Parse every session's newline-joined commands via bashlex.

    Parameters
    ----------
    agg_df : DataFrame with columns {'session','commands_joined',...}
    progress : show tqdm if available
    strict : if True, raise AssertionError on any parse failure.
             if False, return parse_df + failures list and only keep
             parsed sessions in parsed_parts_by_session.

    Returns
    -------
    parsed_parts_by_session : dict[session -> bashlex parts]
        Only sessions that parsed successfully.
    parse_df : DataFrame summarising parse success/failure.
    failures : list of (session, commands_joined, error) for failures.
    """
    try:
        # Force plain tqdm (no ipywidgets) + disable monitor thread
        from tqdm import tqdm  # NOTE: not tqdm.auto, not tqdm.notebook
        try:
            import tqdm as _tqdm_mod
            _tqdm_mod.tqdm.monitor_interval = 0
        except Exception:
            pass
    except Exception:
        def tqdm(x, **_):
            return x

    parsed_parts_by_session: Dict[str, List[Any]] = {}
    rows = []
    failures: List[Tuple[str, str, str]] = []

    it = agg_df.itertuples(index=False)
    if progress:
        it = tqdm(it, total=len(agg_df), desc="Parsing sessions (bashlex)")

    for row in it:
        # Expect fields: session, ..., commands_joined
        session = getattr(row, "session")
        joined_raw = getattr(row, "commands_joined")

        # Apply minimal parse-safety normalisation here so callers
        # don't have to remember to do it in notebooks.
        joined = parse_safe_minimal(joined_raw)

        ok, parts, err = try_parse(joined)
        rows.append({
            "session": session,
            "parsed": ok,
            "len_parts": (len(parts) if ok and parts is not None else 0),
            "error": ("" if ok else (err or "")),
        })
        if ok and parts is not None:
            parsed_parts_by_session[session] = parts
        else:
            failures.append((session, joined, err or ""))

    parse_df = pd.DataFrame(rows)

    if strict and failures:
        n_fail = len(failures)
        raise AssertionError(f"Parse failures: {n_fail}")

    return parsed_parts_by_session, parse_df, failures



# ------------------------------------------
# Walk AST → tokens → (op,args,conn)* seq
# ------------------------------------------
def _walk_tokens(node: Any) -> List[str]:
    """
    Linearise a bashlex AST node into a flat stream of tokens in source order.

    Emits:
      - words as tokens
      - connectors/operators (';', '&&', '||')
      - pipes as '|'
      - redirects as operator (>, >>, 2>, etc.) + their output word
      - interleaves separators between sibling commands in 'list' / 'commands'
    """
    toks: List[str] = []
    kind = getattr(node, "kind", None)

    def _emit_sep(sep: Any) -> None:
        sk = getattr(sep, "kind", None)
        if sk == "operator" and hasattr(sep, "op"):
            toks.append(sep.op)  # ';', '&&', '||'
        elif sk == "pipe":
            toks.append("|")

    if kind == "word":
        toks.append(node.word)
        return toks

    if kind == "operator":
        toks.append(node.op)
        return toks

    if kind == "pipe":
        toks.append("|")
        return toks

    # Interleave separators for list-like containers
    if hasattr(node, "list") and getattr(node, "list"):
        children = list(node.list)
        seps = list(getattr(node, "separators", []) or [])
        for i, ch in enumerate(children):
            toks.extend(_walk_tokens(ch))
            if i < len(seps):
                _emit_sep(seps[i])
    elif hasattr(node, "commands") and getattr(node, "commands"):
        children = list(node.commands)
        seps = list(getattr(node, "separators", []) or [])
        for i, ch in enumerate(children):
            toks.extend(_walk_tokens(ch))
            if i < len(seps):
                _emit_sep(seps[i])
    else:
        # Generic recursion over 'parts'
        if hasattr(node, "parts") and getattr(node, "parts"):
            for ch in node.parts:
                toks.extend(_walk_tokens(ch))

    # Redirects: include operator and output target as tokens
    if kind == "redirect":
        try:
            if hasattr(node, "type") and node.type:
                toks.append(node.type)  # '>', '>>', '2>'
            if hasattr(node, "output") and getattr(node.output, "word", None):
                toks.append(node.output.word)
        except Exception:
            pass

    return toks


def tokens_to_triplets(tokens: List[str]) -> List[Triplet]:
    """
    Split a flat token stream on connectors into (op, args, conn).
    The connector closes the command with that connector; the session boundary
    ALWAYS ends with 'EOS' even if the last AST token was a connector.
    """
    triplets: List[Triplet] = []
    chunk: List[str] = []
    for t in tokens:
        if t in CONNECTOR_TOKENS:
            if chunk:
                op, *args = chunk
                triplets.append((op, args, t))
                chunk = []
            else:
                # stray connector with no preceding command -> ignore
                continue
        else:
            chunk.append(t)

    if chunk:
        # normal case: last command wasn't closed by an explicit connector
        op, *args = chunk
        triplets.append((op, args, "EOS"))
    else:
        # ended on a connector -> flip the last triplet's connector to EOS
        if triplets:
            op, args, _ = triplets[-1]
            triplets[-1] = (op, args, "EOS")
    return triplets


def ast_to_triplets(parts: List[Any]) -> List[Triplet]:
    """
    Convert bashlex AST roots to (op,args,conn) triplets.

    Important: an implicit ';' is injected between top-level roots when bashlex
    returns multiple roots (newline-separated commands), to preserve per-line sequentiality.
    """
    tokens: List[str] = []
    for i, p in enumerate(parts):
        tokens.extend(_walk_tokens(p))
        # Insert implicit ';' between top-level commands (newline joins).
        if i < len(parts) - 1:
            last = tokens[-1] if tokens else None
            if last not in CONNECTOR_TOKENS:
                tokens.append(";")
    return tokens_to_triplets(tokens)


def count_connectors_from_ast(parts: List[Any]) -> Dict[str, int]:
    """Count connectors as bashlex sees them (excludes connectors inside quotes)."""
    counts = {";": 0, "&&": 0, "||": 0, "|": 0}

    def walk(n: Any) -> None:
        k = getattr(n, "kind", None)
        if k == "operator" and getattr(n, "op", None) in (";", "&&", "||"):
            counts[n.op] += 1
        elif k == "pipe":
            counts["|"] += 1
        for attr in ("parts", "list", "commands"):
            if hasattr(n, attr) and getattr(n, attr):
                for ch in getattr(n, attr):
                    walk(ch)

    for p in parts:
        walk(p)
    return counts


# -------------------------------
# Batch build + diagnostics
# -------------------------------
def build_sequences_from_parsed(
    parsed_parts_by_session: Dict[str, List[Any]]
) -> Dict[str, List[Triplet]]:
    """
    Build canonical (op,args,conn) sequences for every session from parsed ASTs.
    """
    seqs: Dict[str, List[Triplet]] = {}
    for sid, parts in parsed_parts_by_session.items():
        seqs[sid] = ast_to_triplets(parts)

    # Core invariants: non-empty and 'EOS' termination
    if not all(seq and seq[-1][2] == "EOS" for seq in seqs.values()):
        raise AssertionError("Missing EOS or empty sequence.")
    if not all(op for seq in seqs.values() for (op, _, _) in seq):
        raise AssertionError("Empty operator in a command.")
    return seqs


def connector_mismatch_report(
    agg_df: pd.DataFrame,
    parsed_parts_by_session: Dict[str, List[Any]],
    seqs: Dict[str, List[Triplet]],
) -> List[Tuple[str, Dict[str, int], Dict[str, int], int]]:
    """
    Compare AST connector counts vs. sequence counts, compensating for
    the synthetic ';' injected between top-level parts.

    Returns a list of tuples:
      (session, ast_counts, seq_counts_adjusted, injected_semis)
    for sessions where counts differ after adjustment.
    """
    problems: List[Tuple[str, Dict[str, int], Dict[str, int], int]] = []
    for row in agg_df.itertuples(index=False):
        s = getattr(row, "session")
        parts = parsed_parts_by_session[s]
        seq = seqs[s]

        ast_counts = count_connectors_from_ast(parts)

        conns = [c for _, _, c in seq]
        internal = conns[:-1] if conns and conns[-1] == "EOS" else conns
        seq_counts_raw = {
            ";": internal.count(";"),
            "&&": internal.count("&&"),
            "||": internal.count("||"),
            "|": internal.count("|"),
        }

        injected_semis = max(len(parts) - 1, 0)
        seq_counts = dict(seq_counts_raw)
        seq_counts[";"] = max(0, seq_counts_raw[";"] - injected_semis)

        if ast_counts != seq_counts:
            problems.append((s, ast_counts, seq_counts, injected_semis))
    return problems


# -------------------------------
# Convenience one-shot pipeline
# -------------------------------
def parse_dataframe_to_triplets(
    agg_df: pd.DataFrame,
    *,
    progress: bool = True,
    with_diagnostics: bool = True,
    strict: bool = True,
) -> Tuple[Dict[str, List[Triplet]], Dict[str, List[Any]], Optional[pd.DataFrame], Optional[List[Any]]]:
    """
    High-level convenience function that runs:
      1) bashlex parsing over all sessions (with minimal normalisation)
      2) AST → (op,args,conn) triplets
      3) optional connector mismatch diagnostics

    Parameters
    ----------
    agg_df : DataFrame with columns {'session','n_rows','commands_joined',...}
    progress : show tqdm if available
    with_diagnostics : if True, compute connector mismatch report
    strict : if True, raise on any parse failure (backwards-compatible).
             if False, skip unparsable sessions and proceed.

    Returns
    -------
    seqs : dict[session -> List[Triplet]]
        Only for successfully parsed sessions.
    parsed_parts : dict[session -> List[bashlex AST roots]]
    parse_df : DataFrame summarising parse success/failure.
    problems : list of connector mismatch tuples, or None.
    """
    parsed_parts, parse_df, failures = parse_all_sessions(
        agg_df,
        progress=progress,
        strict=strict,
    )

    if strict and failures:
        # Backwards-compatible behaviour: hard fail if anything didn't parse.
        raise AssertionError(f"Parse failures: {len(failures)}")

    # Build triplet sequences only for parsed sessions
    seqs = build_sequences_from_parsed(parsed_parts)

    problems = None
    if with_diagnostics:
        # Restrict diagnostics to the successfully parsed subset
        agg_ok = agg_df[agg_df["session"].isin(parsed_parts.keys())].copy()
        problems = connector_mismatch_report(agg_ok, parsed_parts, seqs)

    return seqs, parsed_parts, parse_df, problems

