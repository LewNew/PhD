# src/fi_fs/utils.py

from __future__ import annotations
import random
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Optional, Sequence, Union


def bright_palette_indices():
    """
    Return a list of bright-ish xterm 256-colour indices:
    - use the 6x6x6 colour cube (16-231)
    - skip low-intensity colours (r+g+b too small)
    - skip the grapyscale ramp (232-255)
    """
    indices = []
    for idx in range(16, 232):
        c = idx - 16
        r = c // 36
        g = (c % 36) // 6
        b = c % 6
        if r + g + b >= 6:
            indices.append(idx)
    return indices

def build_fi_colour_map(
        fi_hashes: Iterable[str],
        seed: int = 0,
) -> Dict[str, int]:

    fi_list = sorted(set(fi_hashes))
    bright = bright_palette_indices()

    if not bright:
        raise RuntimeError("Bright palette function returned an empty palette")

    random.seed(seed)
    palette = random.sample(bright, k=min(len(fi_list), len(bright)))

    return {
        fh: palette[i % len(palette)]
        for i, fh in enumerate(fi_list)
    }

def colour_text(text: str, fi_hash: str, fi_to_colour: Dict[str, int]) -> str:
    code = fi_to_colour.get(fi_hash)
    if code is None:
        return text
    return f"\033[38;5;{code}m{text}\033[0m"

def write_fs_families_report(
    *,
    dataset: Union[str, Path],
    root: Union[str, Path],
    fi_df: Any,
    summ_df: Any,
    archetypes: Any,
    family_groups: Mapping[int, Sequence[int]],
    cmd_col_candidates: Sequence[str] = ("commands_clean", "commands_joined", "commands"),
    out_subdir: Union[str, Path] = Path("projects/fi_fs/data/output") ,
    out_leaf: Union[str, Path] = Path("FS_eval"),
    snippet_chars: int = 300,
    top_members: int = 10,
) -> Path:
    """
    Write an FS families Markdown report to:
      {root}/{out_subdir}/{DATASET_NAME}/{out_leaf}/{DATASET_NAME}_FS_families_report.md

    Parameters
    ----------
    dataset:
        The dataset path (or any string) used to derive DATASET_NAME via Path(dataset).stem.
    root:
        Project root path used for output directory construction.
    fi_df, summ_df, archetypes:
        DataFrames used in the report. (Typed as Any to avoid a hard pandas dependency in utils.)
    family_groups:
        Mapping family_id -> iterable of archetype row indices into `archetypes`.
    cmd_col_candidates:
        Columns to search for in `fi_df` for the cleaned/joined command text.
    snippet_chars:
        Max characters for medoid snippet in the report.
    top_members:
        Number of member archetypes to list per family (by volume).

    Returns
    -------
    Path
        The full path to the written Markdown report.
    """
    root = Path(root)
    dataset_name = Path(dataset).stem

    report_dir = root / Path(out_subdir) / dataset_name / Path(out_leaf)
    report_dir.mkdir(parents=True, exist_ok=True)

    # Pick a commands column
    cmd_col = next((c for c in cmd_col_candidates if c in fi_df.columns), None)
    if cmd_col is None:
        raise KeyError(
            f"No commands column found in fi_df. Looked for: {list(cmd_col_candidates)}. "
            f"Got: {list(fi_df.columns)}"
        )

    # fi_hash -> raw session volume
    fi_volumes: Dict[str, int] = fi_df["fi_hash"].value_counts().to_dict()

    summ2 = summ_df.copy()

    def calculate_total_volume(fid: int) -> int:
        idxs = family_groups[fid]
        hashes = archetypes.loc[idxs, "fi_hash"].tolist()
        return int(sum(fi_volumes.get(fh, 0) for fh in hashes))

    summ2["total_sessions"] = summ2["family_id"].map(calculate_total_volume)

    # Sort by total_sessions, then size
    fam_order = (
        summ2.sort_values(["total_sessions", "size"], ascending=[False, False])["family_id"]
        .tolist()
    )

    lines = ["# FS Families Report\n"]
    lines.append(f"Total Families: {len(summ2)}\n")

    for fid in fam_order:
        row = summ2.loc[summ2["family_id"] == fid].iloc[0]
        idxs = family_groups[fid]
        medoid_idx = int(row["medoid_idx"])
        med = archetypes.iloc[medoid_idx]

        # Medoid command lookup
        med_rows = fi_df.loc[
            (fi_df["session"].astype(str) == str(med.session)) &
            (fi_df["fi_hash"] == med.fi_hash),
            cmd_col,
        ]
        med_cmds = str(med_rows.iloc[0]) if not med_rows.empty else "N/A"
        med_cmds_snip = med_cmds[:snippet_chars] + (" ..." if len(med_cmds) > snippet_chars else "")

        lines.append(
            f"## Family {fid}\n\n"
            f"- **Total Session Volume**: {int(row['total_sessions'])}\n"
            f"- **FI-Unique Archetypes**: {int(row['size'])}\n"
            f"- **Mean FS**: {row['mean_FS']:.3f} (±{row['sd_FS']:.3f})\n"
            f"- **Medoid Archetype**: `{med.fi_hash}` (Session: `{med.session}`, n_rows={int(med.n_rows)})\n\n"
            f"**Medoid Execution Snippet:**\n"
            f"```text\n{med_cmds_snip}\n```\n\n"
            f"**Consensus Skeleton (op, conn pairs):**\n"
            f"`{row['consensus_skeleton_pairs']}`\n\n"
            f"Top operators: {row.get('top_ops', 'N/A')}\n\n"
        )

        # Members table with per-archetype volume
        members = archetypes.loc[idxs, ["fi_hash", "session", "n_rows"]].copy()
        members["session_count"] = members["fi_hash"].map(fi_volumes).fillna(0).astype(int)
        members = members.sort_values("session_count", ascending=False).head(int(top_members))

        lines.append("**Top Member Archetypes by Volume:**\n\n" + members.to_markdown(index=False) + "\n")
        lines.append("---\n")

    report_path = report_dir / f"{dataset_name}_FS_families_report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    return report_path



def write_fs_summary(
    *,
    root: Union[str, Path],
    dataset: Union[str, Path],
    fi_df: pd.DataFrame,
    FS_lev: np.ndarray,
    summ_df: pd.DataFrame,
    family_groups: Mapping[int, Sequence[int]],
    archetypes: pd.DataFrame,
    # Optional context
    input_path: Optional[Union[str, Path]] = None,
    stats: Optional[Mapping[str, Any]] = None,
    agg: Optional[pd.DataFrame] = None,
    alias_changes: Optional[Sequence[Any]] = None,
    tau: Optional[Any] = None,
    fs_path: Optional[Union[str, Path]] = None,
    # Output control
    out_dir: Optional[Union[str, Path]] = None,
) -> Path:
    """
    Write an FS pipeline summary text file for a dataset.

    Returns:
        Path to the written summary file.
    """
    root = Path(root)
    dataset_path = Path(dataset)
    dataset_name = dataset_path.stem

    if input_path is None:
        input_path = (
            root
            / "projects"
            / "fi_fs"
            / "data"
            / "processed"
            / dataset_name
            / f"{dataset_name}.csv"
        )
    input_path = Path(input_path)
    input_file_str = input_path.name
    input_path_str = (
        str(input_path.relative_to(root)) if input_path.exists() else str(input_path)
    )

    # Output folder default
    if out_dir is None:
        out_dir = (
            root
            / "projects"
            / "fi_fs"
            / "data"
            / "output"
            / dataset_name
            / "FS_eval"
        )
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    summary_path = out_dir / f"{dataset_name}_FS_Summary.txt"

    # Raw counts
    n_raw: Optional[int] = None
    if stats is not None and isinstance(stats, Mapping) and "n_sessions" in stats:
        try:
            n_raw = int(stats["n_sessions"])
        except Exception:
            n_raw = None
    elif agg is not None:
        try:
            n_raw = int(len(agg))
        except Exception:
            n_raw = None

    n_parsed = int(len(fi_df))
    n_failed = int(max(0, n_raw - n_parsed)) if n_raw is not None else None
    parse_success_rate = (n_parsed / n_raw) * 100 if (n_raw is not None and n_raw > 0) else None
    parsed_str = (
        f"{n_parsed} ({parse_success_rate:.2f}%)"
        if parse_success_rate is not None
        else f"{n_parsed}"
    )

    # FI archetype stats
    n_fi_classes = int(fi_df["fi_hash"].nunique())
    fi_counts = fi_df["fi_hash"].value_counts()
    n_fi_singletons = int((fi_counts == 1).sum())
    n_fi_non_singletons = int((fi_counts >= 2).sum())

    dedup_factor = (n_parsed / n_fi_classes) if n_fi_classes > 0 else float("nan")
    avg_sessions_per_arch = (n_parsed / n_fi_classes) if n_fi_classes > 0 else float("nan")
    dedup_factor_str = f"{dedup_factor:.2f}x" if np.isfinite(dedup_factor) else "N/A"
    avg_sessions_str = f"{avg_sessions_per_arch:.2f}" if np.isfinite(avg_sessions_per_arch) else "N/A"

    # Alias changes
    n_alias_changes: Optional[int]
    try:
        n_alias_changes = 0 if alias_changes is None else int(len(alias_changes))
    except Exception:
        n_alias_changes = None
    alias_changes_str = str(n_alias_changes) if n_alias_changes is not None else "N/A"

    # FS stats (off-diagonal)
    N = int(FS_lev.shape[0])
    tri = FS_lev[np.triu_indices_from(FS_lev, 1)] if N >= 2 else np.array([])
    fs_stats_str = (
        f"  mean={float(tri.mean()):.3f}, median={float(np.median(tri)):.3f}, "
        f"min={float(tri.min()):.3f}, max={float(tri.max()):.3f}"
    ) if tri.size else "  N/A (matrix too small)"

    # FS saved path
    fs_saved_path: Optional[Path] = None
    if fs_path is not None:
        try:
            fs_saved_path = Path(fs_path)
        except Exception:
            fs_saved_path = None

    if fs_saved_path is None:
        candidate = (
            root
            / "projects"
            / "fi_fs"
            / "data"
            / "output"
            / dataset_name
            / "FS_eval"
            / "NumPy_Arrays"
            / f"{dataset_name}_FS_Lev_opconn_N{N}.npy"
        )
        fs_saved_path = candidate if candidate.exists() else None

    fs_saved_str = (
        str(fs_saved_path.relative_to(root))
        if fs_saved_path and fs_saved_path.exists()
        else (str(fs_saved_path) if fs_saved_path else "N/A")
    )

    tau_str = str(tau) if tau is not None else "N/A"

    # Family stats
    n_families = int(len(summ_df))
    fam_sizes = summ_df["size"].astype(int) if n_families else pd.Series([], dtype=int)
    n_fam_singletons = int((fam_sizes == 1).sum()) if n_families else 0
    n_fam_non_singletons = int((fam_sizes >= 2).sum()) if n_families else 0
    largest_family = int(fam_sizes.max()) if n_families else 0
    median_family = float(fam_sizes.median()) if n_families else float("nan")
    median_family_str = f"{median_family:.2f}" if np.isfinite(median_family) else "N/A"

    fi_volumes = fi_df["fi_hash"].astype(str).value_counts().to_dict()

    def family_total_sessions(fid: int) -> int:
        idxs = family_groups[int(fid)]
        fam_hashes = archetypes.loc[list(idxs), "fi_hash"].astype(str).tolist()
        return int(sum(fi_volumes.get(h, 0) for h in fam_hashes))

    summ2 = summ_df.copy()
    if n_families:
        summ2["total_sessions"] = summ2["family_id"].map(family_total_sessions)

        top5 = (
            summ2.sort_values(["total_sessions", "size", "mean_FS"], ascending=[False, False, False])
                 .head(5)
                 .loc[:, ["family_id", "total_sessions", "size", "mean_FS", "sd_FS"]]
        )
    else:
        top5 = pd.DataFrame(columns=["family_id", "total_sessions", "size", "mean_FS", "sd_FS"])

    top5_lines = []
    for _, r in top5.iterrows():
        top5_lines.append(
            f"  - Family {int(r['family_id'])}: total_sessions={int(r['total_sessions'])}, "
            f"archetypes={int(r['size'])}, mean_FS={float(r['mean_FS']):.3f} (±{float(r['sd_FS']):.3f})"
        )
    top5_block = "\n".join(top5_lines) if top5_lines else "  (none)"

    report_path = out_dir / f"{dataset_name}_FS_families_report.md"
    report_path_str = str(report_path.relative_to(root)) if report_path.exists() else str(report_path.relative_to(root))

    # Markdown content. Edit as needed
    summary_content = f"""FS Pipeline Summary: {dataset_name}
==========================================
Input File:               {input_file_str}
Input Path:               {input_path_str}

FI Bootstrap Context (for FS)
-----------------------------
Total Raw Sessions:        {n_raw if n_raw is not None else "N/A"}
Successfully Parsed:       {parsed_str}
Parse Failures:            {n_failed if n_failed is not None else "N/A"}

Unique Archetypes (FI):    {n_fi_classes}
FI Singleton Archetypes:   {n_fi_singletons}
FI Non-singletons:         {n_fi_non_singletons}
Deduplication Factor:      {dedup_factor_str}
Avg Sessions / Archetype:  {avg_sessions_str}

Normalisation Metadata
----------------------
Alias Changes applied:     {alias_changes_str}

Functional Similarity (FS)
---------------------------
FS Comparator:             structural Levenshtein (op+conn)
FS Matrix Size (N x N):    {N} x {N}

FS (off-diagonal) stats:
{fs_stats_str}

FS Matrix Saved:           {fs_saved_str}

FS Clustering
-------------
Method:                    Agglomerative (threshold tau)
tau:                       {tau_str}

Families discovered:       {n_families}
Singleton families:        {n_fam_singletons}
Non-singleton families:    {n_fam_non_singletons}

Largest family size:       {largest_family}
Median family size:        {median_family_str}

Top families by prevalence (volume-weighted):
{top5_block}

Outputs
-------
FS Families Report (MD):   {report_path_str}
"""

    summary_path.write_text(summary_content, encoding="utf-8")
    return summary_path
