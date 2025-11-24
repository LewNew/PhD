# src/fi_fs/fs_lev.py
from __future__ import annotations
from typing import Dict, Sequence, List
import numpy as np
from tqdm.auto import tqdm

from .fs import Trips, token_cache

def _levenshtein_tokens(a: Sequence[str], b: Sequence[str]) -> int:
    na, nb = len(a), len(b)
    if na == 0:
        return nb
    if nb == 0:
        return na
    if na > nb:
        a, b = b, a
        na, nb = nb, na
    prev = list(range(na + 1))
    cur  = [0] * (na + 1)
    for j in range(1, nb + 1):
        cur[0] = j
        bj = b[j - 1]
        for i in range(1, na + 1):
            cost = 0 if a[i - 1] == bj else 1
            cur[i] = min(
                prev[i] + 1,        # deletion
                cur[i - 1] + 1,     # insertion
                prev[i - 1] + cost  # substitution
            )
        prev, cur = cur, prev
    return prev[na]

# ---------------------------------------------------------------------------
# FS Levenshtein similarity on full token streams
# ---------------------------------------------------------------------------

def fs_levenshtein(
    arche: Dict[str, Trips],
    include_connectors: bool = True,
    progress: bool = False,
):
    """
    NxN similarity using normalised token-level Levenshtein distance
    over triplets_to_tokens() (OP + ARG + optional CONN), with
    placeholder index stripping, ARGREF markers and redirection tagging.

    sim(a,b) = 1 - dist / max(len(a), len(b))  (both empty -> 1)

    Returns (labels, S) with diag=1, S in [0,1].
    """
    labels = list(arche.keys())
    tokens = token_cache(
        arche,
        include_connectors=include_connectors,
        strip_placeholder_indices=True,
        mark_placeholder_reuse=True,
        tag_redirection=True,
    )
    n = len(labels)
    S = np.eye(n, dtype=np.float64)

    it_rows = tqdm(range(n), desc="Levenshtein (rows)", leave=False) if progress else range(n)
    total_pairs = n * (n - 1) // 2
    pb_pairs = tqdm(total=total_pairs, desc="Levenshtein (pairs)", leave=True) if progress else None

    for i in it_rows:
        ai = tokens[labels[i]]
        lai = len(ai)
        for j in range(i + 1, n):
            aj = tokens[labels[j]]
            lbj = len(aj)
            denom = max(lai, lbj)
            if denom == 0:
                sim = 1.0
            else:
                d = _levenshtein_tokens(ai, aj)
                sim = max(0.0, 1.0 - (d / denom))
            S[i, j] = S[j, i] = sim
            if pb_pairs:
                pb_pairs.update(1)

    if pb_pairs:
        pb_pairs.close()
    return labels, S


# ---------------------------------------------------------------------------
# Lane A structural Levenshtein on (op, conn) only
# ---------------------------------------------------------------------------

def _tokens_op_conn(trips: Trips, include_connectors: bool = True) -> List[str]:
    """
    Tokenise only operators and connectors, e.g.:

        OP:wget, CONN:&&, OP:chmod, CONN:;, ...

    This matches the simplified Lane A structural comparator used in FS Eval.
    """
    toks: List[str] = []
    for op, args, conn in trips:
        toks.append(f"OP:{op}")
        if include_connectors and conn:
            toks.append(f"CONN:{conn}")
    return toks


def fs_levenshtein_structural(
    arche: Dict[str, Trips],
    include_connectors: bool = True,
    progress: bool = False,
):
    """
    Lane A structural FS: NxN similarity using normalised Levenshtein
    distance over (op, conn) token streams only.

    sim(a,b) = 1 - dist / max(len(a), len(b))  (both empty -> 1)

    Returns (labels, S) with diag=1, S in [0,1].
    """
    labels = list(arche.keys())
    token_map = {
        fid: _tokens_op_conn(trips, include_connectors=include_connectors)
        for fid, trips in arche.items()
    }

    n = len(labels)
    S = np.eye(n, dtype=np.float64)

    it_rows = tqdm(range(n), desc="Levenshtein-struct (rows)", leave=False) if progress else range(n)
    total_pairs = n * (n - 1) // 2
    pb_pairs = tqdm(total=total_pairs, desc="Levenshtein-struct (pairs)", leave=True) if progress else None

    for i in it_rows:
        ai = token_map[labels[i]]
        lai = len(ai)
        for j in range(i + 1, n):
            aj = token_map[labels[j]]
            lbj = len(aj)
            denom = max(lai, lbj)
            if denom == 0:
                sim = 1.0
            else:
                d = _levenshtein_tokens(ai, aj)
                sim = max(0.0, 1.0 - (d / denom))
            S[i, j] = S[j, i] = sim
            if pb_pairs:
                pb_pairs.update(1)

    if pb_pairs:
        pb_pairs.close()
    return labels, S
