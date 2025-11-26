# src/fi_fs/utils.py

import random
from typing import Dict, Iterable

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