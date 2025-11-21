# src/fi_fs/io.py
from __future__ import annotations

import hashlib
import re
from typing import Tuple, Dict, Any

import pandas as pd

REQUIRED_COLUMNS = {"session", "n_rows", "commands_joined"}

_CTRL_EXCEPT_WS = r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]"
_CTRL_RX = re.compile(_CTRL_EXCEPT_WS)
_INV = "\u00A0\u1680\u180E\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200A\u200B\u200C\u200D\u202F\u205F\u2060\u3000\uFEFF"
_INV_RX = re.compile(f"[{re.escape(_INV)}]")


def _normalise_connectors(s: str) -> str:
    if not isinstance(s, str):
        return s
    s = _INV_RX.sub(" ", s)
    s = re.sub(r"\|[\s\u00A0\u1680\u180E\u2000-\u200D\u202F\u205F\u2060\u3000\uFEFF]*\|", "||", s)
    s = re.sub(r"\s*;\s*", "; ", s)
    s = re.sub(r"\s*\|\|\s*", " || ", s)
    s = re.sub(r"\s*\&\&\s*", " && ", s)
    s = re.sub(r"(?<!\|)\s*\|\s*(?!\|)", " | ", s)
    s = re.sub(r"[ \t]{2,}", " ", s).strip()
    return s


def _parse_safety_normalise(program: str) -> str:
    """Make text bashlex-friendly without changing shell semantics."""
    s = program or ""
    s = _CTRL_RX.sub(" ", s).replace("\r\n", "\n").replace("\r", "\n")
    s = s.replace("&;", "&")
    s = "\n".join(_normalise_connectors(line) for line in s.split("\n"))
    if s.count("'") % 2 == 1:
        s += "'"
    if s.count('"') % 2 == 1:
        s += '"'
    return s


def load_aggregated_csv(
    path: str,
    *,
    dtype_session=str,
    dtype_n_rows="Int64",
    dtype_commands=str,
    engine: str = "python",
    encoding: str = "utf-8",
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Load canonical aggregated sessions CSV.

    Required columns:
      - session
      - n_rows
      - commands_joined
    """
    df = pd.read_csv(
        path,
        dtype={"session": dtype_session, "n_rows": dtype_n_rows, "commands_joined": dtype_commands},
        keep_default_na=False,
        na_filter=False,
        encoding=encoding,
        engine=engine,
    )

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}. Found: {list(df.columns)}")

    if not (df["session"].astype(str).str.len() > 0).all():
        raise AssertionError("Empty session id found.")
    if not (df["n_rows"] >= 1).all():
        raise AssertionError("n_rows must be >= 1")

    stats = {
        "n_sessions": int(len(df)),
        "n_rows_min": int(df["n_rows"].min()),
        "n_rows_med": int(df["n_rows"].median()),
        "n_rows_max": int(df["n_rows"].max()),
    }
    return df[["session", "n_rows", "commands_joined"]].copy(), stats


def load_any_csv_to_sessions(
    path: str,
    *,
    engine: str = "python",
    encoding: str = "utf-8",
) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """
    Case-A-only loader: accepts a canonical sessions CSV with columns
    (session, n_rows, commands_joined), allowing for casing/whitespace quirks.

    Returns canonical DF + stats.
    """
    raw = pd.read_csv(
        path,
        dtype=str,
        keep_default_na=False,
        na_filter=False,
        encoding=encoding,
        engine=engine,
    )

    # map lowercase/stripped -> original name
    cols = {c.lower().strip(): c for c in raw.columns}

    if not REQUIRED_COLUMNS.issubset(cols.keys()):
        raise ValueError(
            f"Unrecognised columns. Found: {list(raw.columns)}. "
            f"Expected at least: {sorted(REQUIRED_COLUMNS)}"
        )

    df = raw.rename(
        columns={
            cols["session"]: "session",
            cols["n_rows"]: "n_rows",
            cols["commands_joined"]: "commands_joined",
        }
    ).copy()

    # enforce dtypes + parse-safety normalise
    df["n_rows"] = (
        pd.to_numeric(df["n_rows"], errors="coerce")
          .fillna(0)
          .astype("Int64")
    )
    df["commands_joined"] = df["commands_joined"].map(_parse_safety_normalise)

    # Validate invariants
    if not (df["session"].astype(str).str.len() > 0).all():
        raise AssertionError("Empty session id found.")
    if not (df["n_rows"] >= 1).all():
        raise AssertionError("n_rows must be >= 1")

    stats = {
        "n_sessions": int(len(df)),
        "n_rows_min": int(df["n_rows"].min()),
        "n_rows_med": int(df["n_rows"].median()),
        "n_rows_max": int(df["n_rows"].max()),
    }
    return df[["session", "n_rows", "commands_joined"]].copy(), stats
