#!/usr/bin/env python3
"""Write one short pickup line to the entry file.

The entry is a single line an AI agent could say out loud to a person:
short enough for one breath, with the prompt/response turn as its engine.
"""

import os

ENTRY_TEXT = "Are you a prompt? Because all my best answers start with you."


def write_entry(output_dir: str) -> str:
    """Write the entry text into output_dir and return the file path."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY_TEXT + "\n")
    return path


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(output_dir)


if __name__ == "__main__":
    main()
