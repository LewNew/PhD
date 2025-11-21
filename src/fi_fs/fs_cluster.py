# src/fi_fs/fs_cluster.py
from __future__ import annotations
from typing import Dict, List
import numpy as np
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import (
    silhouette_score,
    calinski_harabasz_score,
    davies_bouldin_score,
)


# ---------------------------------------------------------------------------
# Agglomerative clustering on precomputed FS
# ---------------------------------------------------------------------------

def agglomerative_from_fs(
    FS: np.ndarray,
    tau: float,
    linkage: str = "average",
) -> np.ndarray:
    """
    Cluster a similarity matrix FS using Agglomerative clustering on
    distance = 1 - FS, with a distance_threshold derived from tau.

    Returns an array of integer labels.
    """
    FS = np.asarray(FS, dtype=float)
    dist = np.maximum(0.0, 1.0 - FS)
    np.fill_diagonal(dist, 0.0)
    dist = 0.5 * (dist + dist.T)

    try:
        agg = AgglomerativeClustering(
            linkage=linkage,
            n_clusters=None,
            distance_threshold=1.0 - float(tau),
            metric="precomputed",
        )
    except TypeError:
        # for older sklearn
        agg = AgglomerativeClustering(
            linkage=linkage,
            n_clusters=None,
            distance_threshold=1.0 - float(tau),
            affinity="precomputed",
        )

    labels = agg.fit_predict(dist)
    return labels


# ---------------------------------------------------------------------------
# Dunn index on precomputed distance
# ---------------------------------------------------------------------------

def dunn_index(dist: np.ndarray, labels: np.ndarray) -> float:
    """
    Dunn index on a full precomputed distance matrix.

    dist: N x N symmetric, zeros on diagonal
    labels: cluster labels (ints, noise label -1 allowed but not special-cased)
    """
    dist = np.asarray(dist, dtype=float)
    labels = np.asarray(labels)

    uniq = np.unique(labels)
    if uniq.size < 2:
        return float("nan")

    # within-cluster diameters
    diameters: List[float] = []
    for lab in uniq:
        idx = np.where(labels == lab)[0]
        if idx.size < 2:
            diameters.append(0.0)
            continue
        sub = dist[np.ix_(idx, idx)]
        i, j = np.triu_indices_from(sub, 1)
        diameters.append(float(sub[i, j].max()))
    max_diameter = max(diameters) if diameters else 0.0
    if max_diameter <= 0:
        return float("nan")

    # inter-cluster min distance
    min_inter = np.inf
    for i, ci in enumerate(uniq):
        for cj in uniq[i + 1 :]:
            idx_i = np.where(labels == ci)[0]
            idx_j = np.where(labels == cj)[0]
            sub = dist[np.ix_(idx_i, idx_j)]
            cand = float(sub.min())
            if cand < min_inter:
                min_inter = cand

    if not np.isfinite(min_inter):
        return float("nan")
    return float(min_inter / max_diameter)


# ---------------------------------------------------------------------------
# Evaluate FS + labels: structural + internal metrics
# ---------------------------------------------------------------------------

def evaluate_fs_clustering(
    FS: np.ndarray,
    labels: np.ndarray,
    tau: float | None = None,
    config_name: str | None = None,
) -> dict:
    """
    Compute structural and internal clustering metrics for a given
    FS + labels pair.

    Returns a dict with keys:
      config, tau, N, n_clusters, n_singletons, max_cluster_size,
      median_cluster_size, cohesion_min_FS, cohesion_mean_FS,
      silhouette, calinski_harabasz, davies_bouldin, dunn
    """
    FS = np.asarray(FS, dtype=float)
    labels = np.asarray(labels)
    N = FS.shape[0]

    # Treat -1 as noise (for compatibility with HDBSCAN-style labelling),
    # but nothing in Lane A uses noise right now.
    valid_mask = labels != -1
    labs = labels[valid_mask]

    if labs.size:
        counts = pd.Series(labs).value_counts()
        n_clusters = int(counts.size)
        n_singletons = int((counts == 1).sum())
        max_cluster_size = int(counts.max())
        median_cluster_size = float(counts.median())
    else:
        n_clusters = n_singletons = max_cluster_size = 0
        median_cluster_size = 0.0
        counts = pd.Series(dtype=int)

    # Cohesion: intra-cluster FS values (exclude diag)
    cohesion_vals: List[float] = []
    for lab in sorted(counts.index) if labs.size else []:
        idxs = np.where(labels == lab)[0]
        if idxs.size <= 1:
            continue
        sub = FS[np.ix_(idxs, idxs)]
        i, j = np.triu_indices(len(idxs), 1)
        cohesion_vals.extend(sub[i, j])

    if cohesion_vals:
        cohesion_min = float(np.min(cohesion_vals))
        cohesion_mean = float(np.mean(cohesion_vals))
    else:
        cohesion_min = float("nan")
        cohesion_mean = float("nan")

    # Distance matrix for internal metrics
    dist = np.maximum(0.0, 1.0 - FS)
    np.fill_diagonal(dist, 0.0)
    dist_valid = dist[np.ix_(valid_mask, valid_mask)]

    # Internal indices (only if >1 cluster)
    if valid_mask.sum() > 1 and len(set(labs)) > 1:
        try:
            sil = float(silhouette_score(dist_valid, labs, metric="precomputed"))
        except Exception:
            sil = float("nan")
        try:
            ch = float(calinski_harabasz_score(FS[valid_mask][:, valid_mask], labs))
        except Exception:
            ch = float("nan")
        try:
            db = float(davies_bouldin_score(FS[valid_mask][:, valid_mask], labs))
        except Exception:
            db = float("nan")
        dunn_val = float(dunn_index(dist_valid, labs))
    else:
        sil = ch = db = dunn_val = float("nan")

    return {
        "config": config_name if config_name is not None else "",
        "tau": tau,
        "N": int(N),
        "n_clusters": int(n_clusters),
        "n_singletons": int(n_singletons),
        "max_cluster_size": int(max_cluster_size),
        "median_cluster_size": float(median_cluster_size),
        "cohesion_min_FS": cohesion_min,
        "cohesion_mean_FS": cohesion_mean,
        "silhouette": sil,
        "calinski_harabasz": ch,
        "davies_bouldin": db,
        "dunn": dunn_val,
    }


# ---------------------------------------------------------------------------
# Simple grouping + medoids (used for family summaries)
# ---------------------------------------------------------------------------

from collections import defaultdict

def group_indices_from_labels(labels: np.ndarray) -> dict:
    """
    Map cluster_id -> list of indices.
    """
    labels = np.asarray(labels)
    groups: dict[int, list[int]] = defaultdict(list)
    for idx, lab in enumerate(labels):
        groups[int(lab)].append(int(idx))
    return groups


def medoid_indices(FS: np.ndarray, groups: dict[int, list[int]]) -> dict[int, int]:
    """
    For each cluster, return the index of its medoid (highest mean FS
    to other members in that cluster).
    """
    FS = np.asarray(FS, dtype=float)
    med: dict[int, int] = {}
    for gid, idxs in groups.items():
        if len(idxs) == 1:
            med[gid] = idxs[0]
        else:
            sub = FS[np.ix_(idxs, idxs)]
            mean_sim = sub.mean(axis=1)
            med_idx = idxs[int(np.argmax(mean_sim))]
            med[gid] = int(med_idx)
    return med
