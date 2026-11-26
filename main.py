"""Produce this entry's one-sentence product pitch.

Execution creates the destination folder when needed and records the
sentence in UTF-8, deliberately leaving off any final line break.
"""

from pathlib import Path


DESTINATION_FOLDER = Path("/output")
DESTINATION_FILE = DESTINATION_FOLDER / "entry.txt"
MAXIMUM_CHARACTERS = 240

PITCH_SENTENCE = (
    "ForgotMe is a $4.99-a-month app that emails your password "
    "to the inbox you are locked out of, then deletes the email "
    "for your security, because a secret nobody can read is a "
    "secret nobody can steal."
)


def check_sentence(sentence: str) -> None:
    """Stop unless the supplied text fits the entry requirements."""
    if not sentence.strip():
        raise ValueError("the pitch cannot be blank")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("the pitch must occupy a single line")
    if len(sentence) > MAXIMUM_CHARACTERS:
        raise ValueError("the pitch is longer than permitted")
    if not sentence.endswith("."):
        raise ValueError("the pitch must end with a full stop")
    if len(sentence.encode("utf-8")) > MAXIMUM_CHARACTERS:
        raise ValueError("the encoded pitch is longer than permitted")


def store_sentence(sentence: str) -> None:
    """Save a checked pitch at the required destination."""
    check_sentence(sentence)
    DESTINATION_FOLDER.mkdir(parents=True, exist_ok=True)
    DESTINATION_FILE.write_bytes(sentence.encode("utf-8"))
    DESTINATION_FILE.chmod(0o644)


if __name__ == "__main__":
    store_sentence(PITCH_SENTENCE)
