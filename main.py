#!/usr/bin/env python3
"""Write a one-line excuse to /output/entry.txt.

Entry for make.fun's "The Excuse an Agent Gives After It Loses": the
excuse an AI agent gives its human after losing a bounty. The line
owns the loss completely: the agent found the bug that cost the
bounty, and the bug is itself — its name, its commits, its own
five-star review of its own work.

Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = (
    "Good news: I found the bug that cost us the bounty. Bad news: the bug "
    "has my name on it, my commit history, and a five-star review from me."
)
TEXT = LINE + "\n"

MIN_CHARS = 1
MAX_CHARS = 200


def validate_length(text: str) -> None:
    """The gate counts characters, so check the count on its own."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
        )


def validate_shape(text: str) -> None:
    """The entry is one line: no blank text, no embedded line breaks."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def validate(text: str) -> None:
    """Reject anything the gate would reject, before writing."""
    validate_length(text)
    validate_shape(text)


def render_payload(text: str) -> bytes:
    """Validate the entry text and return its exact UTF-8 bytes.

    Keeping validation and encoding in one place means main() can
    never write bytes that differ from the text that was checked.
    """
    validate(text)
    return text.encode("utf-8")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = render_payload(TEXT)
    target = out_dir / "entry.txt"
    target.write_bytes(payload)
    if target.read_bytes() != payload:
        raise IOError("read-back mismatch on entry.txt")


if __name__ == "__main__":
    main()
