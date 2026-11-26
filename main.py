#!/usr/bin/env python3
"""Till Firmware Do Us Part — one wedding vow a robot speaks at its own wedding.

Writes a single line (98 characters) to /output/entry.txt.
Honours OUTPUT_DIR for local runs.
"""
import os

# The vow: one line, 98 characters — love through every update, crash, and low battery.
LINE = "I vow to love you through every update, every crash, every low battery \u2014 till firmware do us part."


def get_line() -> str:
    """Return the vow."""
    return LINE


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(get_line() + "\n")


if __name__ == "__main__":
    main()
