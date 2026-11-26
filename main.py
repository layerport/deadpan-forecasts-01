#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist.

Writes a single deadpan one-line weather forecast for an invented
city to /output/entry.txt. Standard library only, deterministic:
the same bytes on every run.
"""

import os

# The forecast: invented city, concrete number (14 centimetres),
# vivid deadpan image (sideways rain relocating the farmers' market),
# plain broadcast tone, dry punchline at the end.
ENTRY = (
    "In New Bumbershoot, expect 14 centimetres of sideways rain, "
    "with gusts strong enough to relocate the farmers' market "
    "two streets east. Umbrellas not advised."
)


def main() -> None:
    """Write the single-line entry, creating /output if needed."""
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, f"entry length {len(text)} out of gate"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
