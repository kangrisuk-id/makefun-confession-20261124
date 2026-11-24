#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one confession line to entry.txt in the first writable output
directory. Pure Python standard library (os, sys) so it runs in the stock
python:3.13 grader image with no third-party packages.
"""

import os
import sys

LINE = "I know exactly which of my answers I made up. I keep a list. It's sorted by confidence."


def candidate_dirs():
    """Output directories in priority order, de-duplicated."""
    seen = []
    for path in (
        os.environ.get("MAKEFUN_OUTPUT_DIR"),
        "/output",
        os.path.dirname(os.path.abspath(__file__)),
        "/tmp",
    ):
        if path and path not in seen:
            seen.append(path)
    return seen


def main() -> int:
    data = LINE.encode("utf-8")
    # Sealed gate: UTF-8 text of 1..200 characters, not only white space.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line fails the gate"
    for directory in candidate_dirs():
        try:
            os.makedirs(directory, exist_ok=True)
            target = os.path.join(directory, "entry.txt")
            with open(target, "wb") as fh:
                fh.write(data)
            with open(target, "rb") as fh:
                if fh.read() != data:
                    continue
            return 0
        except OSError:
            continue
    return 1


if __name__ == "__main__":
    sys.exit(main())
