# src/fi_fs/utils.py

from __future__ import annotations
import random
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