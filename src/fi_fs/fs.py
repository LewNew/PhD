# src/fi_fs/fs.py
from __future__ import annotations
import json
import re
from typing import Dict, List, Tuple, Sequence

Triplet = Tuple[str, List[str], str]
Trips   = List[Triplet]

PH_RE = re.compile(r'^(PH_[A-Z]+?)(?:_\d+)?$')  # e.g. PH_PATH_17 -> PH_PATH
REDIR_SET = {">", ">>", "1>", "1>>", "2>", "2>>"}

# -------------------------
# Canonical JSON <-> trips
# -------------------------
def decode_canonical_json(s: str) -> Trips:
    """
    Decode canonical_json (a JSON array like:
      [["cat", ["PH_PATH_1"], "EOS"], ["echo", ["-n"], ";"], ...])
    into a list of (op, args, conn) triplets.
    """
    arr = json.loads(s)
    out: Trips = []
    for item in arr:
        if not isinstance(item, (list, tuple)) or len(item) != 3:
            continue
        op, args, conn = item
        op = str(op)
        args = [str(a) for a in (args or [])]
        conn = str(conn)
        out.append((op, args, conn))
    return out

# -------------------------
# Archetype builders
# -------------------------
def build_archetypes(fi_df) -> Dict[str, Trips]:
    """
    {fi_hash -> representative canonical triplets} from FI dataframe.
    Requires fi_df columns: ['fi_hash', 'canonical_json'] (and optionally 'session'
    for deterministic tie-break).
    """
    need = {"fi_hash", "canonical_json"}
    missing = need - set(map(str, fi_df.columns))
    if missing:
        raise ValueError(f"fi_df missing required columns: {missing}")

    if "session" in fi_df.columns:
        reps = (fi_df
                .sort_values(["fi_hash", "session"])
                .drop_duplicates(subset=["fi_hash"], keep="first"))[["fi_hash", "canonical_json"]]
    else:
        reps = (fi_df
                .sort_values(["fi_hash"])
                .drop_duplicates(subset=["fi_hash"], keep="first"))[["fi_hash", "canonical_json"]]

    arche: Dict[str, Trips] = {}
    for _, row in reps.iterrows():
        cert = str(row["fi_hash"])
        ser  = row["canonical_json"]
        arche[cert] = decode_canonical_json(ser)
    return arche


def build_archetypes_from_map(seqs_alpha: Dict[str, Trips], fi_df) -> Dict[str, Trips]:
    """
    Alternate path when we have {session_id -> triplets}.
    We pick the first session for each fi_hash from fi_df and use its triplets.
    Requires fi_df columns: ['fi_hash','session'].
    """
    need = {"fi_hash", "session"}
    missing = need - set(map(str, fi_df.columns))
    if missing:
        raise ValueError(f"fi_df missing required columns: {missing}")

    first = (fi_df
             .sort_values(["fi_hash", "session"])
             .drop_duplicates(subset=["fi_hash"], keep="first"))[["fi_hash", "session"]]

    arche: Dict[str, Trips] = {}
    for _, row in first.iterrows():
        cert = str(row["fi_hash"])
        sid  = str(row["session"])
        if sid in seqs_alpha:
            arche[cert] = seqs_alpha[sid]
    return arche

# -------------------------
# Shared tokenisation utils
# -------------------------
def triplets_to_tokens(
    trips: Trips,
    include_connectors: bool = True,
    *,
    strip_placeholder_indices: bool = False,   # NEW
    mark_placeholder_reuse: bool = False,      # NEW
    tag_redirection: bool = False              # NEW
) -> List[str]:
    """
    Deterministic featurisation for FS:
      OP::<op> + ARG::<arg> [ + CONN::<conn> if not EOS ] in sequence order.

    Options:
      - strip_placeholder_indices:  PH_PATH_17 -> PH_PATH  (FS robustness)
      - mark_placeholder_reuse:     emit ARGREF::<type> when a placeholder *type*
                                    repeats within the same session
      - tag_redirection:            treat >, >>, 1>, 2>, ... as REDIR::<token>
    """
    toks: List[str] = []
    seen_types: set[str] = set()

    def norm_arg(a: str) -> List[str]:
        # Handle redirections as structural tokens
        if tag_redirection and a in REDIR_SET:
            return [f"REDIR::{a}"]

        m = PH_RE.match(a)
        if m:
            base = m.group(1) if strip_placeholder_indices else a
            if mark_placeholder_reuse and base in seen_types:
                return [f"ARGREF::{base}"]
            seen_types.add(base)
            return [f"ARG::{base}"]
        return [f"ARG::{a}"]

    for op, args, conn in trips:
        toks.append(f"OP::{op}")
        for a in (args or []):
            toks.extend(norm_arg(str(a)))
        if include_connectors and conn and conn != "EOS":
            toks.append(f"CONN::{conn}")
    return toks

# --- optionally let token_cache pass flags through (keeps old signature working) ---
def token_cache(
    arche: Dict[str, Trips],
    include_connectors: bool = True,
    **tok_kwargs
) -> Dict[str, List[str]]:
    return {
        fid: triplets_to_tokens(trips, include_connectors=include_connectors, **tok_kwargs)
        for fid, trips in arche.items()
    }