# src/fi_fs/fs_families.py
from __future__ import annotations

import textwrap
from collections import Counter, defaultdict
from functools import lru_cache
from typing import Dict, List, Sequence, Tuple, Iterable, Any

import numpy as np
import pandas as pd
import plotly.graph_objects as go

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

# ---------------------------------------------------------------------------
# Label formatting (short labels for nodes + richer hover text)
# ---------------------------------------------------------------------------

_CONN_ABBR = {
    "SEQ": ";",
    "AND": "&&",
    "OR": "||",
    "PIPE": "|",
    "BG": "&",
    "NONE": "",
    "EOS": "EOS",
}

def _conn_short(conn: str) -> str:
    c = str(conn)
    return _CONN_ABBR.get(c, c)

def tok_label_short(t: Pair) -> str:
    op, conn = t
    c = _conn_short(conn)
    return f"{op} {c}".strip()

def tok_label_long(t: Pair) -> str:
    op, conn = t
    return f"({op}, {conn})"

def summarise_insert(tokens: List[Pair], mode: str = "first") -> str:
    """Summarise an insertion (a list of (op,conn) pairs) as a short label."""
    if not tokens:
        return ""
    if mode == "first":
        return tok_label_short(tokens[0])
    bits = [tok_label_short(x) for x in tokens[:4]]
    return " → ".join(bits) + (" …" if len(tokens) > 4 else "")

def _collapse_runs(seq: Sequence[Pair]) -> List[Pair]:
    if not seq:
        return []
    out = [seq[0]]
    for t in seq[1:]:
        if t != out[-1]:
            out.append(t)
    return out

def sankey_from_family_enhanced(
    family_seqs: List[List[Pair]],
    backbone: List[Pair] | None = None,
    title: str = "Family — Sankey (WLCS backbone)",
    min_variant_support: float = 0.10,
    topN_variants_per_gap: int = 3,
    bucket_other_variants: bool = True,
    variant_label_mode: str = "first",
    normalise_widths: bool = False,
    show_link_counts: bool = True,
    caption: Dict[str, Any] | None = None,
    collapse_runs: bool = True,

    show_caption: bool = True,
    caption_backbone_max_tokens: int = 14,
    caption_wrap_width: int = 85,

    # Styling / layout knobs (matches your notebook version)
    node_pad: int = 18,
    node_thickness: int = 6,
    fig_width: int | None = None,
    fig_height: int | None = None,
    height_per_node: int = 12,
):
    """
    Compact Sankey:
      - WLCS backbone over (op,conn)
      - variants per gap via LCS alignment to backbone
      - top-N variants shown per gap; remainder bucketed as "Other variants"
      - short node labels, richer hover text
      - grey ribbons; bold labels on white background
      - adaptive layout sizing (overrideable)
    """
    if not family_seqs:
        raise ValueError("family_seqs is empty")

    # 1) Preprocess sequences for visuals (optional)
    seqs_proc = [_collapse_runs(s) for s in family_seqs] if collapse_runs else [list(s) for s in family_seqs]

    # 2) Backbone
    if backbone is None:
        backbone = wlcs_backbone(seqs_proc)
    elif collapse_runs:
        backbone = _collapse_runs(backbone)

    m = len(backbone)
    n_sessions = len(seqs_proc)

    # 3) Count bare backbone vs insertions per gap
    main_counts = np.zeros(m + 1, dtype=int)
    variant_detail: Dict[int, Counter[str]] = defaultdict(Counter)

    for s in seqs_proc:
        pairs = lcs_map(s, backbone)
        matched_i = [-1] + [i for (i, _) in pairs] + [len(s)]
        matched_j = [-1] + [j for (_, j) in pairs] + [m]

        for t in range(len(matched_j) - 1):
            prev_j = matched_j[t]
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

    # 4) Build nodes with styled labels + hover text
    labels: List[str] = []
    plain_labels: List[str] = []
    hovers: List[str] = []
    node_index: Dict[str, int] = {}

    def add_node(lbl: str, hover: str) -> int:
        styled_lbl = (
            f"<span style='background-color: rgba(255,255,255,0.85); "
            f"color: black; padding: 1px 4px; border-radius: 4px; "
            f"font-weight: 700;'>{lbl}</span>"
        )
        k = f"{lbl}||{hover}"
        if k not in node_index:
            node_index[k] = len(labels)
            labels.append(styled_lbl)
            plain_labels.append(lbl)  # <-- NEW
            hovers.append(hover)
        return node_index[k]

    START = add_node("START", "START")
    END = add_node("END", "END")
    B = [add_node(tok_label_short(t), tok_label_long(t)) for t in backbone]

    # Variant nodes per gap (keep counts)
    gap_variant_nodes: Dict[int, List[Tuple[int, int]]] = {}
    for k in range(m + 1):
        cnts = variant_detail.get(k, Counter())
        if not cnts:
            gap_variant_nodes[k] = []
            continue

        items = [(lbl, c, c / max(1, n_sessions)) for lbl, c in cnts.most_common()]
        items_keep = [it for it in items if it[2] >= min_variant_support]
        top = items_keep[:topN_variants_per_gap]
        remainder = sum(c for _, c, _ in items_keep[topN_variants_per_gap:])

        nodes: List[Tuple[int, int]] = []
        for lbl, c, _sup in top:
            nid = add_node(lbl, f"Variant insertion @ gap {k}: {lbl} | support={c}/{n_sessions}")
            nodes.append((nid, c))

        if bucket_other_variants and remainder > 0:
            nid = add_node("Other variants", f"Other insertions @ gap {k} | support={remainder}/{n_sessions}")
            nodes.append((nid, remainder))

        gap_variant_nodes[k] = nodes

    # Decide “main” path per gap for shading (bare vs dominant variant)
    gap_main_mode: Dict[int, str] = {}
    gap_main_variant_ids: Dict[int, set[int]] = {}
    for k in range(m + 1):
        bare = int(main_counts[k])
        vars_k = gap_variant_nodes.get(k, [])
        if not vars_k and bare == 0:
            gap_main_mode[k] = "none"
            gap_main_variant_ids[k] = set()
            continue

        max_var = max([c for _, c in vars_k], default=0)
        if max_var > bare:
            gap_main_mode[k] = "variant"
            gap_main_variant_ids[k] = {nid for nid, c in vars_k if c == max_var}
        else:
            gap_main_mode[k] = "bare"
            gap_main_variant_ids[k] = set()

    # 5) Links (grey ribbons)
    sources: List[int] = []
    targets: List[int] = []
    values: List[float] = []
    colors: List[str] = []
    link_hovers: List[str] = []

    main_col = "rgba(120, 120, 120, 0.30)"
    var_col = "rgba(160, 160, 160, 0.18)"

    def _fmt_link_hover(s: int, t: int, val: int) -> str:
        if show_link_counts:
            return f"{plain_labels[s]} → {plain_labels[t]}; ({val}/{n_sessions})"
        return f"{plain_labels[s]} → {plain_labels[t]};"

    def add_link(s: int, t: int, val: int, col: str):
        if val <= 0:
            return
        sources.append(s)
        targets.append(t)
        values.append(val / max(1, n_sessions) if normalise_widths else val)
        colors.append(col)
        link_hovers.append(_fmt_link_hover(s, t, val))

    if m == 0:
        add_link(START, END, n_sessions, main_col)
    else:
        # gap 0: START -> B0 (and variants in that gap)
        k = 0
        mode = gap_main_mode[k]

        for nid, c in gap_variant_nodes.get(k, []):
            col = main_col if (mode == "variant" and nid in gap_main_variant_ids[k]) else var_col
            add_link(START, nid, c, col)
            add_link(nid, B[0], c, col)

        if main_counts[k] > 0:
            col = main_col if mode == "bare" else var_col
            c = int(main_counts[k])
            add_link(START, B[0], c, col)

        # internal gaps
        for i in range(m - 1):
            gap = i + 1
            mode = gap_main_mode[gap]

            for nid, c in gap_variant_nodes.get(gap, []):
                col = main_col if (mode == "variant" and nid in gap_main_variant_ids[gap]) else var_col
                add_link(B[i], nid, c, col)
                add_link(nid, B[i + 1], c, col)

            if main_counts[gap] > 0:
                col = main_col if mode == "bare" else var_col
                c = int(main_counts[gap])
                add_link(B[i], B[i + 1], c, col)

        # tail gap m: B_last -> END
        gap = m
        mode = gap_main_mode[gap]

        for nid, c in gap_variant_nodes.get(gap, []):
            col = main_col if (mode == "variant" and nid in gap_main_variant_ids[gap]) else var_col
            add_link(B[-1], nid, c, col)
            add_link(nid, END, c, col)

        if main_counts[gap] > 0:
            col = main_col if mode == "bare" else var_col
            c = int(main_counts[gap])
            add_link(B[-1], END, c, col)

    # 6) Adaptive sizing (overrideable)
    n_nodes = len(labels)
    if fig_width is None:
        width = int(np.clip(700 + 85 * max(1, m), 900, 1700))
    else:
        width = int(fig_width)

    if fig_height is None:
        height = int(np.clip(420 + height_per_node * max(1, n_nodes), 320, 1200))
    else:
        height = int(fig_height)

    node_color = "rgba(0, 121, 107, 1.0)"  # teal nodes (your style)

    fig = go.Figure(
        data=[
            go.Sankey(
                arrangement="snap",
                node=dict(
                    label=labels,
                    pad=node_pad,
                    thickness=node_thickness,
                    color=node_color,
                    hovertemplate="%{customdata}<extra></extra>",
                    customdata=hovers,
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values,
                    color=colors,
                    hovertemplate="%{customdata}<extra></extra>",
                    customdata=link_hovers,
                ),
            )
        ]
    )

    # Caption (optional)
    caption_lines: List[str] = []
    if show_caption and caption:
        def fmt_ops(ops, k: int = 6) -> str:
            return ", ".join(f"{op}×{cnt}" for op, cnt in ops[:k])

        # Trim backbone so it never runs off the page
        bb_tokens = [tok_label_short(t) for t in backbone] if backbone else []
        if len(bb_tokens) > caption_backbone_max_tokens:
            bb_tokens = bb_tokens[:caption_backbone_max_tokens] + ["…"]
        bb = " → ".join(bb_tokens) if bb_tokens else "(empty)"
        bb_wrapped = "<br>".join(
            textwrap.wrap(bb, width=caption_wrap_width, break_long_words=False, break_on_hyphens=False)
        )

        caption_lines.append(
            f"Family {caption.get('family_id', '?')}  |  "
            f"n={caption.get('n_sessions', n_sessions)}  |  "
            f"mean_FS={caption.get('mean_FS', '?')}  sd_FS={caption.get('sd_FS', '?')}"
        )
        if caption.get("medoid_fi_hash"):
            caption_lines.append(
                f"Medoid: fi_hash={caption['medoid_fi_hash']}  "
                f"(session {caption.get('medoid_session', '?')}, n_rows={caption.get('medoid_n_rows', '?')})"
            )
        if caption.get("top_ops"):
            caption_lines.append(f"Top ops: {fmt_ops(caption['top_ops'])}")
        caption_lines.append(f"Backbone: {bb_wrapped}")

    if caption_lines:
        fig.update_layout(margin=dict(l=40, r=40, t=60, b=190))
        fig.add_annotation(
            xref="paper",
            yref="paper",
            x=0.0,
            y=-0.28,  # push caption further down so it doesn’t overlap nodes
            showarrow=False,
            align="left",
            font=dict(family="monospace", size=11),
            text="<br>".join(caption_lines),
        )
    else:
        fig.update_layout(margin=dict(l=40, r=40, t=60, b=60))

    fig.update_layout(
        title=title,
        font_family="monospace",
        font_size=12,
        width=width,
        height=height,
    )

    debug = {
        "backbone": backbone,
        "main_counts": main_counts,
        "variant_detail": {k: dict(v) for k, v in variant_detail.items()},
        "n_nodes": n_nodes,
        "width": width,
        "height": height,
        "node_pad": node_pad,
        "node_thickness": node_thickness,
    }
    return fig, backbone, debug

def sankey_for_family_id(
    family_id: int,
    family_members_df: pd.DataFrame,
    summ_df: pd.DataFrame,
    archetypes: pd.DataFrame,
    *,
    title: str | None = None,
    show_caption: bool = True,
    **sankey_kwargs: Any,
):
    """
    Convenience helper: build caption + sequences and call sankey_from_family_enhanced.
    Expects family_members_df from build_family_members_df(), and summ_df from summarise_families().
    """
    import json as _json

    rows = family_members_df.loc[family_members_df["family_id"] == family_id, "struct_tokens"]
    if rows.empty:
        avail = sorted(family_members_df["family_id"].unique().tolist())
        raise ValueError(f"No members for family {family_id}. Available family_ids (first 20): {avail[:20]}")

    family_seqs = [parse_structured_tokens(_json.loads(s)) for s in rows]

    meta_row = summ_df.loc[summ_df["family_id"] == family_id].iloc[0]
    medoid_idx = int(meta_row["medoid_idx"])
    med = archetypes.iloc[medoid_idx]

    caption = {
        "family_id": family_id,
        "n_sessions": len(family_seqs),
        "mean_FS": meta_row["mean_FS"],
        "sd_FS": meta_row["sd_FS"],
        "medoid_fi_hash": med.get("fi_hash", ""),
        "medoid_session": med.get("session", ""),
        "medoid_n_rows": int(med.get("n_rows", 0)),
        "top_ops": meta_row.get("top_ops", []),
    }

    if title is None:
        title = f"Family {family_id} - Sankey (compact)"

    fig, backbone, stats = sankey_from_family_enhanced(
        family_seqs,
        title=title,
        caption=caption,
        show_caption=show_caption,
        **sankey_kwargs,
    )
    return fig, backbone, stats
