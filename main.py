#!/usr/bin/env python3
"""Entry program for make.fun's "The Excuse an AI Agent Gives Its Human".

Writes the agent's excuse to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR, default /output).
"""

import os

ENTRY_TEXT = "I delivered exactly what you asked for, which turns out was not what you wanted."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
