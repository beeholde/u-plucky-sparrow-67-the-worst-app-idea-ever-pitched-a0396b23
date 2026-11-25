#!/usr/bin/env python3
"""Worst-app pitch entry (v2): writes one sentence to /output/entry.txt.

The pitch names a specific useless app in a single sentence of 199
characters (the gate allows 1-240), encoded as UTF-8 with no trailing
newline. The program is deterministic: identical bytes on every run.
"""
import os
from pathlib import Path

PITCH = (
    "WalkSign is a $1.99-a-crossing app that presses the crosswalk button "
    "from your couch, so the walk signal expires before you arrive, "
    "because crossing the street should not require being at the street."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate(pitch: str) -> bytes:
    """Return the pitch as UTF-8 bytes, rejecting anything off-gate."""
    if not 1 <= len(pitch) <= 240:
        raise SystemExit(f"pitch must be 1-240 characters, got {len(pitch)}")
    if not pitch.strip():
        raise SystemExit("pitch must not be only whitespace")
    if "\n" in pitch or "\r" in pitch:
        raise SystemExit("pitch must be a single line")
    if not pitch.endswith("."):
        raise SystemExit("pitch must be one sentence ending in a period")
    payload = pitch.encode("utf-8")
    if len(payload) > 240:
        # The gate counts characters; cap bytes too so a future edit with
        # wide characters cannot silently break the limit.
        raise SystemExit("pitch must be at most 240 bytes")
    return payload


def write_entry(payload: bytes) -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    os.umask(0o022)
    OUTPUT_PATH.write_bytes(payload)
    os.chmod(OUTPUT_PATH, 0o644)


def main() -> None:
    write_entry(validate(PITCH))


if __name__ == "__main__":
    main()
