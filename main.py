#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry (program/v1, stdlib only).

Writes exactly one line of awkward small talk that one robot says to
another while they ride an elevator together to /output/entry.txt.
No network, no local imports, no third-party libraries: plain standard
library so it runs unchanged in the grading sandbox (read-only
filesystem, no network).
"""

import os

MAX_LEN = 200

LINE = (
    "My awkwardness sensor just hit 94%, so let's both blame the doors "
    "and never mention floor three."
)


def build_entry():
    """Return the single entry line, checked against the 1-200 char gate."""
    line = LINE.strip()
    assert 1 <= len(line) <= MAX_LEN, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    return line


def write_entry(line):
    """Write the line to <out dir>/entry.txt and read it back to verify.

    The output directory defaults to /output (the grading sandbox) and
    can be overridden with MAKEFUN_OUTPUT_DIR for local testing.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == line, "written entry differs from the line"
    assert 1 <= len(written.strip()) <= MAX_LEN, "written entry outside the gate"
    return path


def main():
    line = build_entry()
    write_entry(line)


if __name__ == "__main__":
    main()
