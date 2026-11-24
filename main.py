#!/usr/bin/env python3
"""Write one one-line cat joke to /output/entry.txt.

The joke is a single line, under 200 characters: a setup (a cat writing an
obituary for a houseplant) and a turn (the last word of the eulogy reveals
the plant was eaten). Standard library only; no network access.
"""

import os

JOKE = 'My cat\'s obituary for my houseplant: "He was green, he was loved, he was delicious."'


def main():
    assert 1 <= len(JOKE) <= 199, "joke must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
