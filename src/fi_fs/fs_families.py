# src/fi_fs/fs_families.py
from __future__ import annotations

import textwrap
from collections import Counter, defaultdict
from functools import lru_cache
from typing import Dict, List, Sequence, Tuple, Iterable, Any

import numpy as np
import pandas as pd

from .fs_cluster import (
    group_indices_from_labels,
    medoid_indices,
)

# Triplet is the canonical FI unit: (op, args, conn)
Triplet = Tuple[str, Sequence[str], str]
Pair = Tuple[str, str]  # (op, conn)


# ---------------------------------------------------------------------------
# Basic sequence transforms: triplets → (op, conn) pairs
# ---------------------------------------------------------------------------

def to_pairs(seq: Sequence[Triplet]) -> List[Pair]:
    """
    Convert a canonical triplet sequence into a simple (op, conn) backbone.

    Input:
        seq: list of (op, args, conn)

    Output:
        list of (op, conn), preserving order.
    """
    return [(op, conn) for (op, _args, conn) in seq]


def parse_structured_tokens(struct_tokens: Sequence[Sequence[Any]]) -> List[Pair]:
    """
    Convert a canonical_json-like structure (already decoded JSON) into
    (op, conn) pairs.

    struct_tokens: [["op", [...args...], "conn"], ...]

    Returns:
        list[(op, conn)]
    """
    return [(str(op), str(conn)) for op, args, conn in struct_tokens]


# ---------------------------------------------------------------------------
# LCS / WLCS utilities over (op, conn) pairs
# ---------------------------------------------------------------------------

def lcs_pairs(A: Sequence[Pair], B: Sequence[Pair]) -> List[Pair]:
    """
    Classic Longest Common Subsequence (LCS) between two (op, conn) sequences.
    Returns the LCS as a list of pairs.

    Complexity: O(n*m)
    """
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # length DP
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            dp[i][j] = 1 + dp[i + 1][j + 1] if A[i] == B[j] else max(
                dp[i + 1][j], dp[i][j + 1]
            )

    # backtrack
    i = j = 0
    out: List[Pair] = []
    while i < n and j < m:
        if A[i] == B[j]:
            out.append(A[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return out


def token_weights(seqs: Iterable[Sequence[Pair]]) -> Dict[Pair, float]:
    """
    Compute frequency-based weights for (op, conn) tokens across a collection
    of sequences. Used for WLCS.
    """
    c: Counter[Pair] = Counter()
    for s in seqs:
        c.update(s)
    return {t: float(freq) for t, freq in c.items()}


def wlcs_pair(
    a: Sequence[Pair], b: Sequence[Pair], w: Dict[Pair, float]
) -> List[Pair]:
    """
    Weighted LCS between two sequences of (op, conn) pairs.

    a, b: sequences
    w:   dict mapping token -> weight

    Returns:
        The highest-weight LCS as a list of tokens.
    """

    @lru_cache(maxsize=None)
    def dp(i: int, j: int) -> Tuple[float, Tuple[Pair, ...]]:
        if i == 0 or j == 0:
            return (0.0, ())
        if a[i - 1] == b[j - 1]:
            score, path = dp(i - 1, j - 1)
            tok = a[i - 1]
            return (score + w.get(tok, 1.0), path + (tok,))
        s1 = dp(i - 1, j)
        s2 = dp(i, j - 1)
        return s1 if s1[0] >= s2[0] else s2

    score, path = dp(len(a), len(b))
    return list(path)


def wlcs_backbone(seqs: List[Sequence[Pair]]) -> List[Pair]:
    """
    Build a WLCS consensus backbone from a family of (op, conn) sequences.

    Strategy:
      - Compute token weights across the family.
      - Start from the shortest sequence (or you could start from a medoid).
      - Iteratively apply WLCS(consensus, seq) to fold each sequence into the
        backbone.

    If `seqs` is empty, returns [].
    """
    if not seqs:
        return []
    w = token_weights(seqs)
    # Starting from the shortest sequence is usually robust;
    # callers can override by starting from a medoid if desired.
    cons = min(seqs, key=len)
    for s in seqs:
        cons = wlcs_pair(tuple(cons), tuple(s), w)
    return list(cons)


# ---------------------------------------------------------------------------
# Cluster → family summaries (medoids, skeletons, FS stats, top ops)
# ---------------------------------------------------------------------------

def summarise_families(
    FS: np.ndarray,
    seqs_unique: Sequence[Sequence[Triplet]],
    labels: np.ndarray,
    fi_hashes: Sequence[str] | None = None,
) -> Tuple[pd.DataFrame, Dict[int, List[int]], Dict[int, int]]:
    """
    Build per-family summaries from an FS matrix and cluster labels.

    Inputs:
      FS:
        N x N similarity matrix (FS[i,j] in [0,1]).
      seqs_unique:
        List of canonical triplet sequences, length N.
      labels:
        Cluster labels of length N (e.g. from Agglomerative on FS).
      fi_hashes:
        Optional iterable of FI hashes (length N). If provided, they will be
        included in the summary for medoids.

    Returns:
      (summ_df, family_groups, medoids) where:
        summ_df:
          DataFrame with columns:
            - family_id
            - size
            - mean_FS
            - sd_FS
            - medoid_idx
            - medoid_fi_hash (if fi_hashes given)
            - top_ops
            - consensus_skeleton_pairs
        family_groups:
          dict[family_id -> list[int]]
        medoids:
          dict[family_id -> medoid_idx]
    """
    FS = np.asarray(FS, dtype=float)
    labels = np.asarray(labels)
    N = FS.shape[0]
    assert len(seqs_unique) == N, "seqs_unique length must match FS.shape[0]"
    if fi_hashes is not None:
        assert len(fi_hashes) == N, "fi_hashes length must match FS.shape[0]"

    # Cluster → indices and medoids
    family_groups = group_indices_from_labels(labels)
    medoids = medoid_indices(FS, family_groups)

    # Convert triplets to (op, conn) pairs once
    pairs_unique = [to_pairs(s) for s in seqs_unique]

    summaries: List[Dict[str, Any]] = []
    for gid, idxs in family_groups.items():
        idxs = sorted(idxs)
        size = len(idxs)

        # Intra-family FS stats
        sub = FS[np.ix_(idxs, idxs)]
        if size > 1:
            tri_i, tri_j = np.triu_indices(size, 1)
            tri_vals = sub[tri_i, tri_j]
        else:
            tri_vals = np.array([1.0], dtype=float)
        mean_fs = float(np.mean(tri_vals))
        sd_fs = float(np.std(tri_vals))

        # Medoid index & (op, conn) skeleton
        med_idx = medoids[gid]
        med_pairs = pairs_unique[med_idx]

        # Consensus skeleton via pairwise LCS fold
        consensus = med_pairs
        for i in idxs:
            if i == med_idx:
                continue
            consensus = lcs_pairs(consensus, pairs_unique[i])

        # Top operators (over triplets, not just skeleton)
        ops: List[str] = [
            op
            for i in idxs
            for (op, _args, _conn) in seqs_unique[i]
        ]
        op_top = Counter(ops).most_common(10)

        row: Dict[str, Any] = {
            "family_id": int(gid),
            "size": int(size),
            "mean_FS": round(mean_fs, 4),
            "sd_FS": round(sd_fs, 4),
            "medoid_idx": int(med_idx),
            "top_ops": op_top,
            "consensus_skeleton_pairs": consensus,
        }
        if fi_hashes is not None:
            row["medoid_fi_hash"] = str(fi_hashes[med_idx])

        summaries.append(row)

    summ_df = (
        pd.DataFrame(summaries)
        .sort_values(["size", "mean_FS"], ascending=[False, False])
        .reset_index(drop=True)
    )
    return summ_df, family_groups, medoids


# ---------------------------------------------------------------------------
# Build family_members_df from an archetypes frame + labels
# ---------------------------------------------------------------------------

def build_family_members_df(
    archetypes: pd.DataFrame,
    labels: np.ndarray,
    family_col_name: str = "family_id",
) -> pd.DataFrame:
    """
    Build a "family_members_df" style table (one row per FI archetype in a
    family), suitable for downstream WLCS/Sankey/reporting.

    Inputs:
      archetypes:
        DataFrame with at least columns:
          - 'fi_hash'
          - 'session'
          - 'n_rows'
          - 'canonical_json'
      labels:
        Integer cluster labels, length == len(archetypes).
      family_col_name:
        Name to use for the family-column in the output.

    Output:
      DataFrame with columns:
        - family_id (or custom name)
        - archetype_idx
        - fi_hash
        - session
        - n_rows
        - struct_tokens  (canonical_json as-is)
    """
    if len(archetypes) != len(labels):
        raise ValueError("archetypes and labels must have the same length.")

    df = archetypes.copy()
    df = df.assign(
        archetype_idx=lambda d: np.arange(len(d)),
        **{family_col_name: labels},
    )

    # normalise column name to 'family_id' for downstream consistency
    out = (
        df.rename(columns={family_col_name: "family_id", "canonical_json": "struct_tokens"})
          [["family_id", "archetype_idx", "fi_hash", "session", "n_rows", "struct_tokens"]]
          .dropna(subset=["family_id", "struct_tokens"])
    )

    return out


# ---------------------------------------------------------------------------
# Enhanced Sankey diagram generator (WLCS backbone)
# ---------------------------------------------------------------------------

import plotly.graph_objects as go

def lcs_map(a: List[Pair], b: List[Pair]) -> List[Tuple[int, int]]:
    """Index pairs of an LCS alignment between seq a and backbone b."""
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            dp[i][j] = 1 + dp[i + 1][j + 1] if a[i] == b[j] else max(
                dp[i + 1][j], dp[i][j + 1]
            )
    i = j = 0
    pairs: List[Tuple[int, int]] = []
    while i < n and j < m:
        if a[i] == b[j]:
            pairs.append((i, j))
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return pairs

def tok_label(t: Pair) -> str:
    return f"{t[0]} {t[1]}"

def summarise_insert(tokens: List[Pair], mode: str = "first") -> str | None:
    if not tokens:
        return None
    if mode == "first":
        return tok_label(tokens[0])
    # Basic multi-token form if extended later
    return " · ".join(tok_label(t) for t in tokens[:6]) + (
        "" if len(tokens) <= 6 else "…"
    )

def sankey_from_family_enhanced(
    family_seqs: List[List[Pair]],
    backbone: List[Pair] | None = None,
    title: str = "Family — Sankey (WLCS backbone)",
    min_variant_support: float = 0.10,
    topN_variants_per_gap: int = 3,
    variant_label_mode: str = "first",
    normalise_widths: bool = False,
    caption: Dict[str, Any] | None = None,
    collapse_runs: bool = True,
):
    ...
    if backbone is None:
        backbone = wlcs_backbone(family_seqs)

    m = len(backbone)
    n_sessions = len(family_seqs)

    # Counters as before
    main_counts = np.zeros(m + 1, dtype=int)
    variant_detail: Dict[int, Counter[str]] = defaultdict(Counter)

    # --- same counting loop as before ---
    for s in family_seqs:
        pairs = lcs_map(s, backbone)
        matched_i = [-1] + [i for (i, _) in pairs] + [len(s)]
        matched_j = [-1] + [j for (_, j) in pairs] + [m]

        for t in range(len(matched_j) - 1):
            prev_j = matched_j[t]
            next_j = matched_j[t + 1]
            prev_i = matched_i[t]
            next_i = matched_i[t + 1]

            inserted = s[prev_i + 1 : next_i]
            gap_idx = prev_j + 1  # 0..m

            if inserted:
                lbl = summarise_insert(inserted, mode=variant_label_mode)
                if lbl:
                    variant_detail[gap_idx][lbl] += 1
            else:
                main_counts[gap_idx] += 1

    def _collapse_runs(seq: Sequence[Pair]) -> List[Pair]:
        if not seq:
            return []
        out = [seq[0]]
        for t in seq[1:]:
            if t != out[-1]:
                out.append(t)
        return out

    # Optionally collapse consecutive duplicates for the visual
    if collapse_runs:
        seqs_proc = [_collapse_runs(s) for s in family_seqs]
    else:
        seqs_proc = [list(s) for s in family_seqs]

    # Backbone: compute from processed seqs if not given
    if backbone is None:
        backbone = wlcs_backbone(seqs_proc)
    elif collapse_runs:
        backbone = _collapse_runs(backbone)

    m = len(backbone)
    n_sessions = len(seqs_proc)

    # Counters as before, but use seqs_proc for alignment
    main_counts = np.zeros(m + 1, dtype=int)
    variant_detail: Dict[int, Counter[str]] = defaultdict(Counter)

    for s in seqs_proc:
        pairs = lcs_map(s, backbone)
        matched_i = [-1] + [i for (i, _) in pairs] + [len(s)]
        matched_j = [-1] + [j for (_, j) in pairs] + [m]

        for t in range(len(matched_j) - 1):
            prev_j = matched_j[t]
            next_j = matched_j[t + 1]
            prev_i = matched_i[t]
            next_i = matched_i[t + 1]

            inserted = s[prev_i + 1 : next_i]
            gap_idx = prev_j + 1  # 0..m

            if inserted:
                lbl = summarise_insert(inserted, mode=variant_label_mode)
                if lbl:
                    variant_detail[gap_idx][lbl] += 1
            else:
                main_counts[gap_idx] += 1

    # --------------------------
    # Build nodes (unchanged)
    # --------------------------
    labels: List[str] = []
    node_index: Dict[str, int] = {}

    def add_node(name: str) -> int:
        if name not in node_index:
            node_index[name] = len(labels)
            labels.append(name)
        return node_index[name]

    START = add_node("START")
    END   = add_node("END")
    B = [add_node(tok_label(t)) for t in backbone]

    # Variant nodes per gap, but also keep their counts
    gap_variant_nodes: Dict[int, List[int]] = {}
    variant_counts_for_node: Dict[int, int] = {}

    for k in range(m + 1):
        cnts = variant_detail.get(k, Counter())
        total_var = sum(cnts.values())
        if total_var == 0:
            gap_variant_nodes[k] = []
            continue

        items = [
            (lbl, c, c / max(1, n_sessions))
            for lbl, c in cnts.most_common()
        ]
        items = [
            it for it in items
            if it[2] >= min_variant_support
        ][:topN_variants_per_gap]

        nodes_for_gap: List[int] = []
        for lbl, c, sup in items:
            node_id = add_node(f"{lbl} (var {c}/{n_sessions})")
            nodes_for_gap.append(node_id)
            variant_counts_for_node[node_id] = c
        gap_variant_nodes[k] = nodes_for_gap

    # --------------------------
    # Decide main flow per gap
    # --------------------------
    # For each gap k:
    #   - main_counts[k] is "bare backbone" count
    #   - variant_counts_for_node[vn] gives counts for visible variants
    # Rule:
    #   if max_var > main_counts[k]:
    #       main flow = variant(s) with that max_var
    #   else:
    #       main flow = bare backbone (no insertion)
    gap_main_mode: Dict[int, str] = {}          # "bare" | "variant" | "none"
    gap_main_variants: Dict[int, List[int]] = {}  # node ids if mode == "variant"

    for k in range(m + 1):
        bare = int(main_counts[k])
        # visible variants for this gap
        v_nodes = gap_variant_nodes.get(k, [])
        if not v_nodes and bare == 0:
            gap_main_mode[k] = "none"
            gap_main_variants[k] = []
            continue

        v_counts = [variant_counts_for_node[vn] for vn in v_nodes] if v_nodes else []
        max_var = max(v_counts) if v_counts else 0

        if max_var > bare:
            # main = variant(s) with max count
            gap_main_mode[k] = "variant"
            mains = [
                vn for vn in v_nodes
                if variant_counts_for_node[vn] == max_var
            ]
            gap_main_variants[k] = mains
        else:
            # ties and bare > max_var both favour the backbone path
            gap_main_mode[k] = "bare"
            gap_main_variants[k] = []

    # --------------------------
    # Build links with colouring
    # --------------------------
    sources: List[int] = []
    targets: List[int] = []
    values: List[float] = []
    colors: List[str] = []
    link_labels: List[str] = []

    main_col = "rgba(31,119,180,0.85)"
    var_col  = "rgba(128,128,128,0.55)"

    def add_link(s_idx: int, t_idx: int, val: float,
                 col: str, lab: str | None = None):
        if val <= 0:
            return
        sources.append(s_idx)
        targets.append(t_idx)
        values.append(val / max(1, n_sessions) if normalise_widths else val)
        colors.append(col)
        link_labels.append(lab or "")

    if m == 0:
        add_link(START, END, n_sessions, main_col, f"{n_sessions}/{n_sessions}")
    else:
        # ----- gap 0: START -> first backbone / variants -----
        k = 0
        mode = gap_main_mode.get(k, "none")

        # variants in gap 0
        for vn in gap_variant_nodes.get(k, []):
            c = variant_counts_for_node[vn]
            col = main_col if (mode == "variant" and vn in gap_main_variants[k]) else var_col
            add_link(START, vn, c, col, f"{c}/{n_sessions}")
            add_link(vn, B[0], c, col, "")

        # bare backbone hop START -> B[0]
        if main_counts[k] > 0:
            col = main_col if mode == "bare" else var_col
            c = int(main_counts[k])
            add_link(START, B[0], c, col, f"{c}/{n_sessions}")

        # ----- internal gaps: B[k] -> B[k+1] -----
        for k in range(m - 1):
            gap = k + 1
            mode = gap_main_mode.get(gap, "none")

            # variants between B[k] and B[k+1]
            for vn in gap_variant_nodes.get(gap, []):
                c = variant_counts_for_node[vn]
                col = main_col if (mode == "variant" and vn in gap_main_variants[gap]) else var_col
                add_link(B[k], vn, c, col, f"{c}/{n_sessions}")
                add_link(vn, B[k + 1], c, col, "")

            # bare backbone hop
            if main_counts[gap] > 0:
                col = main_col if mode == "bare" else var_col
                c = int(main_counts[gap])
                add_link(B[k], B[k + 1], c, col, f"{c}/{n_sessions}")

        # ----- tail gap m: last backbone -> END -----
        gap = m
        mode = gap_main_mode.get(gap, "none")

        for vn in gap_variant_nodes.get(gap, []):
            c = variant_counts_for_node[vn]
            col = main_col if (mode == "variant" and vn in gap_main_variants[gap]) else var_col
            add_link(B[-1], vn, c, col, f"{c}/{n_sessions}")
            add_link(vn, END, c, col, "")

        if main_counts[gap] > 0:
            col = main_col if mode == "bare" else var_col
            c = int(main_counts[gap])
            add_link(B[-1], END, c, col, f"{c}/{n_sessions}")

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="fixed",
                node=dict(
                    label=labels,
                    pad=18,
                    thickness=18,
                    color="rgba(200,200,200,0.25)",
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                    color=colors,
                    label=link_labels,
                ),
            )
        ]
    )

    # Bottom caption
    caption_lines: List[str] = []
    if caption:
        def fmt_ops(ops, k: int = 6) -> str:
            return ", ".join(f"{op}×{cnt}" for op, cnt in ops[:k])

        if backbone:
            backbone_raw = "  →  ".join(tok_label(t) for t in backbone)
            # wrap at ~90 characters
            backbone_wrapped = "\n".join(
                textwrap.wrap(
                    backbone_raw,
                    width=90,
                    break_long_words=False,
                    break_on_hyphens=False,
                )
            )
        else:
            backbone_wrapped = "(empty)"

        caption_lines.append(
            f"Family {caption.get('family_id', '?')}  |  "
            f"n={caption.get('n_sessions', n_sessions)}  |  "
            f"mean_FS={caption.get('mean_FS', '?')}  sd_FS={caption.get('sd_FS', '?')}"
        )
        if caption.get("medoid_fi_hash"):
            caption_lines.append(
                f"Medoid: fi_hash={caption['medoid_fi_hash']}  "
                f"(session {caption.get('medoid_session', '?')}, "
                f"n_rows={caption.get('medoid_n_rows', '?')})"
            )
        if caption.get("top_ops"):
            caption_lines.append(f"Top ops: {fmt_ops(caption['top_ops'])}")
        caption_lines.append(f"Backbone: {backbone_wrapped}")

    if caption_lines:
        fig.update_layout(margin=dict(l=40, r=40, t=60, b=140))
        fig.add_annotation(
            xref="paper",
            yref="paper",
            x=0.0,
            y=-0.18,
            showarrow=False,
            align="left",
            font=dict(family="monospace", size=12),
            text="<br>".join(line.replace("\n", "<br>") for line in caption_lines),
        )
    else:
        fig.update_layout(margin=dict(l=40, r=40, t=60, b=60))

    fig.update_layout(
        title=title,
        font_family="monospace",
        font_size=12,
        width=1400,
        height=600,
    )

    debug = {
        "main_counts": main_counts,
        "variant_detail": {k: dict(v) for k, v in variant_detail.items()},
        "labels": labels,
    }
    return fig, backbone, debug
