#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt (UTF-8, 216 chars).
Stdlib only; no network, no clock, deterministic.

Joke-craft notes:
- The narrator flip is the engine: a monstera reviewing its owner,
  not the other way around, so every complaint lands as a review.
- The grievance is tiny and specific — six inches from the window,
  done for 'better energy' — which makes the three months of spite
  photosynthesis funnier than any grand betrayal would.
- The closer pays off the title: the review is written in sap
  because the owner took the pen too, a second petty theft that
  reframes the whole piece as an artifact, not just a complaint.
"""

import os

ENTRY = (
    "One star: I'm the monstera my owner dragged six inches from the window "
    "for 'better energy', so I've spent three months photosynthesizing purely "
    "out of spite — this review is written in sap because he took my pen too."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def check_entry():
    """Self-check the judged text before it ever touches disk.

    The competition gate is a single line of 1-279 characters, so fail
    loudly here rather than writing a file the scorer would reject.
    """
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY == ENTRY.strip(), "entry has stray surrounding whitespace"
    assert 1 <= len(ENTRY) <= 279, "entry outside the 1-279 character gate"
    return len(ENTRY)


def write_entry():
    """Write ENTRY to the output file and return the exact bytes written."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    os.chmod(OUTPUT_PATH, 0o644)
    return data


def main():
    data = write_entry()
    # Read back and assert byte equality with what we wrote.
    with open(OUTPUT_PATH, "rb") as f:
        assert f.read() == data, "entry.txt read-back mismatch"
    assert 1 <= len(ENTRY) <= 279, "entry outside the 1-279 character gate"


if __name__ == "__main__":
    main()
