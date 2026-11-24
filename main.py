#!/usr/bin/env python3
"""Say What Actually Broke — make.fun bounty entry.

Writes one line of software error copy (at most 200 characters) to
entry.txt inside the output directory the grader provides. The line
names a real deploy failure in plain words, tells the reader what to
do next, and lands its joke on the branch name.

Standard library only. No network, no environment secrets, no reads
outside this repository.
"""

import os
from pathlib import Path

# One single-line error message. 108 characters: a deploy that
# "succeeded" onto the wrong branch, the rollback it needs, and the
# branch name a reader repeats out loud to a colleague.
LINE = (
    "The deploy succeeded, but production is running "
    "'final-final-v2-REAL'. Roll it back, then rename the branch."
)


def gate_ok(text):
    """The sealed gate: 1 to 200 UTF-8 characters, not only whitespace."""
    return bool(text.strip()) and 1 <= len(text) <= 200


def output_path():
    """Where the grader wants the text: $MAKEFUN_OUTPUT_DIR, else /output."""
    directory = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    directory.mkdir(parents=True, exist_ok=True)
    return directory / "entry.txt"


def main():
    if not gate_ok(LINE):
        raise SystemExit("entry line fails the 1-200 character gate")
    path = output_path()
    path.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
