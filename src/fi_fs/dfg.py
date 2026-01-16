# src/fi_fs/dfg.py
from collections import Counter, defaultdict
import json
import shutil
import subprocess
import numpy as np
from pathlib import Path
from typing import List, Tuple, Dict, Set, Mapping, Sequence, Any, Optional, Union

Pair = Tuple[str, str]  # (op, conn)
START: Pair = ("<START>", "")
END: Pair   = ("<END>", "")

_CONN_ABBR = {"SEQ": ";", "AND": "&&", "OR": "||", "PIPE": "|", "BG": "&", "NONE": ""}

def _conn_short(conn: str) -> str:
    c = str(conn)
    return _CONN_ABBR.get(c, c)

def tok_label_short(t: Pair) -> str:
    op, conn = t
    c = _conn_short(conn)
    return f"{op} {c}".strip()

def parse_structured_tokens_local(struct_tokens: Sequence[Sequence[Any]]) -> List[Pair]:
    # struct_tokens: [["op", [...args...], "conn"], ...]
    return [(str(op), str(conn)) for op, _args, conn in struct_tokens]

def _collapse_runs(seq: List[Pair]) -> List[Pair]:
    if not seq:
        return []
    out = [seq[0]]
    for t in seq[1:]:
        if t != out[-1]:
            out.append(t)
    return out

def _seq_edges(seq: List[Pair]) -> Set[Tuple[Pair, Pair]]:
    path = [START] + seq + [END]
    return set(zip(path[:-1], path[1:]))

def _node_label(t: Pair) -> str:
    if t[0] == "<START>":
        return "START"
    if t[0] == "<END>":
        return "END"
    return tok_label_short(t)

def build_family_arche_pairs(
    family_members_df: Any,
    fam_id: int
) -> Dict[str, List[Pair]]:
    fam_members = family_members_df.loc[
        family_members_df["family_id"] == fam_id, ["fi_hash", "struct_tokens"]
    ].copy()
    fam_members["fi_hash"] = fam_members["fi_hash"].astype(str)

    if fam_members.empty:
        raise ValueError(f"No members for family {fam_id}")

    arche_pairs: Dict[str, List[Pair]] = {}
    for r in fam_members.itertuples(index=False):
        arche_pairs[str(r.fi_hash)] = parse_structured_tokens_local(json.loads(r.struct_tokens))
    return arche_pairs

def compute_edge_supports(
    arche_pairs: Dict[str, List[Pair]],
    fi_volumes: Dict[str, int],
    *,
    collapse_runs: bool = True,
):
    edge_fi   = Counter()
    edge_sess = Counter()
    out_fi    = Counter()
    out_sess  = Counter()
    pos_acc = defaultdict(list)

    fi_hashes = list(arche_pairs.keys())
    n_fi_family = len(fi_hashes)
    n_sess_family = int(sum(fi_volumes.get(h, 0) for h in fi_hashes))

    for fh, seq in arche_pairs.items():
        seq2 = _collapse_runs(seq) if collapse_runs else list(seq)
        w = int(fi_volumes.get(fh, 0))

        for i, t in enumerate(seq2):
            pos_acc[t].append(i)

        edges = _seq_edges(seq2)
        for a, b in edges:
            edge_fi[(a, b)] += 1
            edge_sess[(a, b)] += w

    for (a, _b), c in edge_fi.items():
        out_fi[a] += c
    for (a, _b), c in edge_sess.items():
        out_sess[a] += c

    node_pos = {t: float(np.mean(xs)) for t, xs in pos_acc.items() if xs}
    return edge_fi, edge_sess, out_fi, out_sess, node_pos, n_fi_family, n_sess_family

def dfg_filter_topk_per_source(
    edge_weights: Counter,
    *,
    topk: int = 3,
    keep_end: bool = True
):
    outgoing = defaultdict(list)
    for (a, b), w in edge_weights.items():
        outgoing[a].append(((a, b), w))

    kept = []
    for a, items in outgoing.items():
        items.sort(key=lambda x: x[1], reverse=True)

        if keep_end:
            end_items = [x for x in items if x[0][1] == END]
            non_end   = [x for x in items if x[0][1] != END]
        else:
            end_items = []
            non_end   = items

        kept_edges = end_items + non_end[:topk]

        seen = set()
        for (e, w) in kept_edges:
            if e not in seen:
                kept.append((e, w))
                seen.add(e)

    kept.sort(key=lambda x: x[1], reverse=True)
    return kept

def html_label_white(text: str) -> str:
    return (
        '<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">'
        f'<TR><TD BGCOLOR="white">{text}</TD></TR>'
        '</TABLE>>'
    )

def dfg_to_dot_layered(
    edge_fi: Counter,
    edge_sess: Counter,
    out_fi: Counter,
    out_sess: Counter,
    node_pos: Dict[Pair, float],
    *,
    n_fi_family: int,
    n_sess_family: int,
    conditional_mode: str = "fi",
    topk_per_source: int = 3,
    keep_end_edges: bool = True,
    max_edges: int = 120,
    rank_bins: int = 8,
    graph_title: str = "",
    decimals: int = 1,
    suppress_100: bool = True,
    caption: bool = True,
):
    if conditional_mode not in {"fi", "sess"}:
        raise ValueError("conditional_mode must be 'fi' or 'sess'")

    edge_w = edge_fi if conditional_mode == "fi" else edge_sess
    out_w  = out_fi  if conditional_mode == "fi" else out_sess

    filtered = dfg_filter_topk_per_source(edge_w, topk=topk_per_source, keep_end=keep_end_edges)
    filtered = filtered[:max_edges]

    nodes: Set[Pair] = {START, END}
    for (a, b), _ in filtered:
        nodes.add(a); nodes.add(b)

    pos_vals = [node_pos.get(t, np.nan) for t in nodes if t not in {START, END}]
    pos_vals = [p for p in pos_vals if np.isfinite(p)]
    pmin, pmax = (float(min(pos_vals)), float(max(pos_vals))) if pos_vals else (0.0, 1.0)

    def bin_pos(t: Pair) -> int:
        if t == START:
            return -1
        if t == END:
            return rank_bins + 1
        p = node_pos.get(t, pmax)
        if not np.isfinite(pmax - pmin) or (pmax - pmin) < 1e-9:
            return 0
        x = (p - pmin) / (pmax - pmin)
        return int(np.clip(np.floor(x * (rank_bins - 1e-9)), 0, rank_bins - 1))

    rank_groups = defaultdict(list)
    for t in nodes:
        rank_groups[bin_pos(t)].append(t)

    def esc(s: str) -> str:
        return s.replace('"', '\\"')

    def pct(a: Pair, b: Pair) -> float:
        num = float(edge_w.get((a, b), 0))
        den = float(out_w.get(a, 0))
        return (num / den * 100.0) if den > 0 else 0.0

    def fmt_pct(p: float) -> str:
        if suppress_100 and p >= 99.95:
            return ""
        return f"{p:.{decimals}f}%"

    lines: List[str] = []
    lines.append("digraph DFG {")
    lines.append("rankdir=LR;")
    lines.append('graph [fontname="monospace"];')
    lines.append('node  [shape=box, fontname="monospace"];')
    lines.append('edge  [fontname="monospace"];')
    lines.append('edge [labeldistance=2.0, labelangle=45];')

    if caption:
        cap = (
            f"{graph_title} "
            f"(Family: FI={n_fi_family}, sessions={n_sess_family} | "
            f"edge labels: conditional next-step % over {'FI-classes' if conditional_mode=='fi' else 'sessions'} | "
            f"filtered: top-{topk_per_source}/node + END edges)"
        ).strip()
        lines.append(f'label="{esc(cap)}";')
        lines.append("labelloc=b;")
        lines.append("fontsize=12;")

    node_id: Dict[Pair, str] = {}
    for t in nodes:
        lbl = _node_label(t)
        node_id[t] = lbl
        lines.append(f'"{esc(lbl)}";')

    for r in sorted(rank_groups.keys()):
        same = " ".join(f'"{esc(node_id[t])}"' for t in rank_groups[r])
        lines.append("{ rank=same; " + same + " }")

    for (a, b), _w in filtered:
        la = node_id[a]
        lb = node_id[b]
        el = fmt_pct(pct(a, b))
        if el:
            lines.append(f'"{esc(la)}" -> "{esc(lb)}" [label={html_label_white(el)}];')
        else:
            lines.append(f'"{esc(la)}" -> "{esc(lb)}";')

    lines.append("}")
    return "\n".join(lines)

def write_family_dfgs(
    *,
    dataset: Union[str, "Path"],
    root: Union[str, "Path"],
    family_members_df: Any,
    fi_df: Any,
    out_subdir: Union[str, "Path"] = Path("projects/fi_fs/data/output"),
    out_leaf: Union[str, "Path"] = Path("FS_Families"),
    collapse_runs: bool = True,
    topk_per_source: int = 3,
    keep_end_edges: bool = True,
    rank_bins: int = 8,
    max_edges: int = 120,
    decimals: int = 1,
    suppress_100: bool = True,
    caption: bool = False,
    render: bool = True,
    render_format: str = "png",
    dpi: int = 300,
    fail_fast: bool = True,
    verbose: bool = True,
) -> Tuple["Path", "Path"]:
    """
    Write BOTH DFG variants to:
      {root}/{out_subdir}/{dataset_stem}/{out_leaf}/DFG-FI-Weighted/
      {root}/{out_subdir}/{dataset_stem}/{out_leaf}/DFG-Prevalence-Weighted/
    Each family writes .dot + (optionally) rendered image via Graphviz `dot`.
    """

    root = Path(root)
    dataset_name = Path(dataset).stem
    base_dir = root / Path(out_subdir) / dataset_name / Path(out_leaf)

    out_dir_fi   = base_dir / "DFG-FI-Weighted"
    out_dir_sess = base_dir / "DFG-Prevalence-Weighted"
    out_dir_fi.mkdir(parents=True, exist_ok=True)
    out_dir_sess.mkdir(parents=True, exist_ok=True)

    if render:
        if shutil.which("dot") is None:
            raise RuntimeError(
                "Graphviz `dot` not found on PATH. Install graphviz or call with render=False."
            )

    fi_volumes = fi_df["fi_hash"].astype(str).value_counts().to_dict()
    fam_ids = sorted(family_members_df["family_id"].unique().tolist())

    try:
        from tqdm.auto import tqdm
        iterator = tqdm(fam_ids, desc="Rendering DFGs (FI + Prevalence)", unit="family")
    except Exception:
        iterator = fam_ids

    def _run_dot(dot_in: Path, img_out: Path) -> None:
        # Need to run it as a subprocess via command line
        # -Gdpi works for raster outputs; harmless for svg
        cmd = ["dot", f"-T{render_format}", f"-Gdpi={int(dpi)}", str(dot_in), "-o", str(img_out)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        # if proc.returncode != 0:
        #     msg = (
        #         f"Graphviz failed for: {dot_in}\n"
        #         f"Command: {' '.join(cmd)}\n"
        #         f"STDERR (first 2000 chars):\n{(proc.stderr or '')[:2000]}"
        #     )
        #     raise RuntimeError(msg)

    errors = []

    for fam in iterator:
        fam_id = int(fam)

        arche_pairs = build_family_arche_pairs(family_members_df, fam_id)
        edge_fi, edge_sess, out_fi, out_sess, node_pos, n_fi, n_sess = compute_edge_supports(
            arche_pairs,
            fi_volumes,
            collapse_runs=collapse_runs,
        )

        dot_fi = dfg_to_dot_layered(
            edge_fi, edge_sess, out_fi, out_sess, node_pos,
            n_fi_family=n_fi,
            n_sess_family=n_sess,
            conditional_mode="fi",
            topk_per_source=topk_per_source,
            keep_end_edges=keep_end_edges,
            rank_bins=rank_bins,
            max_edges=max_edges,
            graph_title=f"DFG (FI-weighted) — Family {fam_id}",
            decimals=decimals,
            suppress_100=suppress_100,
            caption=caption,
        )
        dot_path_fi = out_dir_fi / f"DFG_Family_{fam_id}.dot"
        img_path_fi = out_dir_fi / f"DFG_Family_{fam_id}.{render_format}"
        dot_path_fi.write_text(dot_fi, encoding="utf-8")

        dot_sess = dfg_to_dot_layered(
            edge_fi, edge_sess, out_fi, out_sess, node_pos,
            n_fi_family=n_fi,
            n_sess_family=n_sess,
            conditional_mode="sess",
            topk_per_source=topk_per_source,
            keep_end_edges=keep_end_edges,
            rank_bins=rank_bins,
            max_edges=max_edges,
            graph_title=f"DFG (prevalence-weighted) — Family {fam_id}",
            decimals=decimals,
            suppress_100=suppress_100,
            caption=caption,
        )
        dot_path_sess = out_dir_sess / f"DFG_Family_{fam_id}.dot"
        img_path_sess = out_dir_sess / f"DFG_Family_{fam_id}.{render_format}"
        dot_path_sess.write_text(dot_sess, encoding="utf-8")

        if render:
            try:
                _run_dot(dot_path_fi, img_path_fi)
                _run_dot(dot_path_sess, img_path_sess)
            except Exception as e:
                if fail_fast:
                    raise
                errors.append((fam_id, str(e)))

    def _rel(p: Path) -> str:
        try:
            return str(p.relative_to(root))
        except Exception:
            return str(p)

    if verbose:
        print("Done.")
        print("FI-weighted output:        ", _rel(out_dir_fi))
        print("Prevalence-weighted output:", _rel(out_dir_sess))

        if errors:
            print("\nSome families failed to render:")
            for fam_id, err in errors[:10]:
                print(f"  - Family {fam_id}: {err.splitlines()[0]}")

    return out_dir_fi, out_dir_sess

