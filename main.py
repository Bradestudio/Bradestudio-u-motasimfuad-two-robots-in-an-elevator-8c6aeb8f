#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry (program/v1, stdlib only).

Writes exactly one line of awkward small talk that one robot says to
another while they ride an elevator together to /output/entry.txt.
No network, no local imports, no third-party libraries: plain standard
library so it runs unchanged in the grading sandbox (read-only
filesystem, no network).
"""

import os

LINE = (
    "My awkwardness sensor just hit 94%, so let's both blame the doors "
    "and never mention floor three."
)


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Read back and verify what the grader will see: one line, 1-200 chars.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == line, "written entry differs from the line"
    assert 1 <= len(written.strip()) <= 200, "written entry outside the gate"


if __name__ == "__main__":
    main()
