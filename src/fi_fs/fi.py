# src/fi_fs/fi.py
from __future__ import annotations

import hashlib
import json
import os
from typing import Dict, List, Tuple

import pandas as pd

Triplet = Tuple[str, List[str], str]  # (op, args, conn)


# ----------------------------
# Canonical serialisation
# ----------------------------
def serialise_canonical(seq: List[Triplet]) -> str:
    """
    Deterministic JSON serialisation of a canonical triplet sequence.
    - Fixed order
    - No locale quirks
    - Compact separators
    """
    arr = [[op, list(args), conn] for (op, args, conn) in seq]
    return json.dumps(arr, ensure_ascii=False, separators=(",", ":"), sort_keys=False)


def assert_serialisation_deterministic(seqs_by_sid: Dict[str, List[Triplet]]) -> None:
    for sid, trips in seqs_by_sid.items():
        s1 = serialise_canonical(trips)
        s2 = serialise_canonical(trips)
        if s1 != s2:
            raise AssertionError(f"Serialisation not deterministic for session {sid}")


# ----------------------------
# Hashing / FI certificate
# ----------------------------
def fi_hash(serialised: str) -> str:
    """SHA-256 over canonical JSON string."""
    # return hashlib.sha256(serialised.encode("utf-8", errors="strict")).hexdigest()
    full_hash = hashlib.sha256(serialised.encode("utf-8")).hexdigest()
    return full_hash[:16]


def fi_cert(trips: List[Triplet]) -> str:
    """
    Stable FI-class certificate for a canonical sequence (post-normalisation).
    Convenience wrapper: serialise → sha256.
    """
    return fi_hash(serialise_canonical(trips))


# ----------------------------
# FI table construction
# ----------------------------
def build_fi_dataframe(
    agg_df: pd.DataFrame,
    seqs_alpha: Dict[str, List[Triplet]],
    *,
    commands_col: str = "commands_joined",
) -> pd.DataFrame:
    """
    Build the FI table:
      session, n_rows, commands_clean, canonical_json, fi_hash

    Parameters
    ----------
    agg_df     : DataFrame with columns {'session','n_rows', commands_col}
    seqs_alpha : dict[session -> canonical (op,args,conn) triplets]
    commands_col : name of the input column with the raw joined commands

    Returns
    -------
    pd.DataFrame
    """
    rows = []
    for row in agg_df.itertuples(index=False):
        sid = getattr(row, "session")
        n_rows = int(getattr(row, "n_rows"))
        cmds = getattr(row, commands_col)
        trips = seqs_alpha[sid]
        ser = serialise_canonical(trips)
        rows.append(
            {
                "session": sid,
                "n_rows": n_rows,
                # FIX AFTER. IT'S FOR TESTING PURPOSES ONLY
                # FIX: MOVE FI_HASH AFTER CANONICAL JSON
                "fi_hash": fi_hash(ser),
                "commands_clean": cmds,
                "canonical_json": ser,
                # "fi_hash": fi_hash(ser),
            }
        )
    fi_df = pd.DataFrame(rows)
    return fi_df


def write_fi_csv(fi_df: pd.DataFrame, input_dataset_path: str, *, suffix: str = "_canonical.csv") -> str:
    """
    Write the FI dataframe next to the input dataset base name:
      <base>_canonical.csv
    Returns the written path.
    """
    base = os.path.splitext(os.path.basename(input_dataset_path))[0]
    out_csv = f"{base}{suffix}"
    fi_df.to_csv(out_csv, index=False, encoding="utf-8")
    return out_csv
