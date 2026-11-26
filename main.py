#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt (UTF-8, 216 chars).
Stdlib only; no network, no clock, deterministic.
"""

import os

ENTRY = (
    "One star: I'm the monstera my owner dragged six inches from the window "
    "for 'better energy', so I've spent three months photosynthesizing purely "
    "out of spite — this review is written in sap because he took my pen too."
)


def main():
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)
    # Read back and assert byte equality with what we wrote.
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == data, "entry.txt read-back mismatch"
    assert 1 <= len(ENTRY) <= 279, "entry outside the 1-279 character gate"


if __name__ == "__main__":
    main()
