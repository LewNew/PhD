"""FI/FS toolkit public API (current minimal set)."""

# ---- FI (serialise + cert + dataframe) ----
from .fi import (
    fi_cert,
    fi_hash,
    serialise_canonical,
    assert_serialisation_deterministic,
    build_fi_dataframe,
    write_fi_csv,
)

# ---- IO (load aggregated CSV) ----
from .io import (
    load_aggregated_csv,
)

# ---- Parse (bashlex → triplets + diagnostics) ----
from .parse import (
    parse_all_sessions,
    parse_dataframe_to_triplets,
    build_sequences_from_parsed,
    connector_mismatch_report,
)

# ---- Normalisation (aliases, placeholders, α-renumber) ----
from .normalise import (
    apply_aliases,
    apply_placeholders_args_only,
    assert_connectors_preserved,
    alpha_renumber,
    DEFAULT_ALIAS_MAP,
)

# ---- FS core (canonical → archetypes, tokenisation) ----
from .fs import (
    decode_canonical_json,
    build_archetypes,
    build_archetypes_from_map,
    triplets_to_tokens,
    token_cache,
)

# ---- FS measures (current: Levenshtein) ----
from .fs_lev import (
    fs_levenshtein,
)

# ---- FS clustering helpers ----
from .fs_cluster import (
    agglomerative_from_fs,
    evaluate_fs_clustering,
)

# ---- FS family summarisation (medoids, WLCS backbones, members) ----
from .fs_families import (
    summarise_families,
    build_family_members_df,
    wlcs_backbone,
)

# ---- Utils ----
from .utils import (
    get_cache_dir,
    labels_tag as _labels_tag,
    save_similarity,
    load_similarity,
)

__all__ = [
    # FI
    "fi_cert", "fi_hash", "serialise_canonical",
    "assert_serialisation_deterministic", "build_fi_dataframe", "write_fi_csv",

    # IO
    "load_aggregated_csv",

    # Parse
    "parse_all_sessions", "parse_dataframe_to_triplets",
    "build_sequences_from_parsed", "connector_mismatch_report",

    # Normalisation
    "apply_aliases", "apply_placeholders_args_only",
    "assert_connectors_preserved", "alpha_renumber", "DEFAULT_ALIAS_MAP",

    # FS core
    "decode_canonical_json", "build_archetypes", "build_archetypes_from_map",
    "triplets_to_tokens", "token_cache",

    # FS measures
    "fs_levenshtein",

    # FS clustering
    "agglomerative_from_fs", "evaluate_fs_clustering",

    # FS families
    "summarise_families", "build_family_members_df", "wlcs_backbone",

    # Utils
    "get_cache_dir", "_labels_tag", "save_similarity", "load_similarity",
]
