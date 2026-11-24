#!/usr/bin/env python3
"""Worst-app pitch entry: writes one sentence to /output/entry.txt.

The pitch is a single sentence (178 chars, 1-240 allowed), UTF-8, no trailing
newline. The program is deterministic: same bytes on every run.
"""
import os
import sys
from pathlib import Path

LINE = (
    "LaceUp is a $5.99-a-month app that ties your shoes for you by mailing "
    "you a new pair of pre-tied shoes every month, because bending down is "
    "a legacy feature we no longer support."
)


def check(text: str) -> None:
    if not (1 <= len(text) <= 240):
        raise SystemExit(f"entry must be 1-240 characters, got {len(text)}")
    if len(text.encode("utf-8")) > 240:
        # The gate counts characters, but keep the byte length in range too
        # so a future edit with wide characters cannot silently break the cap.
        raise SystemExit("entry must be at most 240 bytes")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    check(LINE)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    os.umask(0o022)
    target.write_bytes(LINE.encode("utf-8"))
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
