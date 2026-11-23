#!/usr/bin/env python3
"""One-star review of something essential: sleep.

Writes a single deadpan one-star review line to entry.txt inside
the output directory given by MAKEFUN_OUTPUT_DIR (falling back to
./output when the variable is unset).
"""

import os

REVIEW = (
    "One star. Sleep takes eight hours a night, charges full price "
    "in grogginess, and still ships me tired every morning. "
    "Would not recommend."
)


def main():
    # Guard: the review must be a single line of 1-160 characters.
    if not (1 <= len(REVIEW) <= 160):
        raise SystemExit(
            "review must be 1-160 chars, got %d" % len(REVIEW)
        )
    if "\n" in REVIEW or "\r" in REVIEW:
        raise SystemExit("review must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")

    # Read-back validation: what we wrote must match exactly.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != REVIEW + "\n":
        raise SystemExit("read-back mismatch in entry.txt")
    if not (1 <= len(written.strip()) <= 160):
        raise SystemExit("written review out of 1-160 char range")


if __name__ == "__main__":
    main()
