#!/usr/bin/env python3
"""Write a childhood memory for make.fun's
Make the AI Judge Feel Nostalgic: A Childhood Memory bounty.

Why this entry fits the judge's brief: it is one sentence that
brings back a childhood summer through concrete senses -- the
smell of fresh rice, rain on hot dust, the creak of the screen
door -- and the ache that it would never end. The memory is
specific (grandma's kitchen, one more bowl) rather than a
generic "I miss childhood", so it reads like a real photograph
kept in a tin, not a slogan.
"""

import os

LINE = (
    "Grandma's kitchen smelled of fresh rice and rain on hot dust, "
    "and I was small enough to believe summer evenings would never "
    "end, that the screen door would always creak open and call me "
    "home for one more bowl."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-280 characters, a single sentence.
    # The line was counted at exactly 209 characters; pin that
    # so any accidental wording change fails loudly instead of
    # silently shipping a different (or over-long) entry.
    assert len(line) == 209, f"line is {len(line)} characters, expected 209"
    assert 1 <= len(line) <= 280, f"line is {len(line)} characters"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert line.strip() == line, "line must not have surrounding whitespace"
    # One sentence: exactly one period, the final character.
    assert line.count(".") == 1, "line must be a single sentence"
    assert line.endswith("."), "line must end with its single period"
    # The judge's brief: a specific childhood memory with concrete
    # senses, not a generic "I miss childhood" -- the fresh rice,
    # the summer evening, the screen door calling the child home.
    assert "fresh rice" in line, "line must keep its sensory detail"
    assert "summer evenings" in line, "line must keep the summer evening"
    assert "screen door" in line, "line must keep the screen door"
    assert "Grandma" in line, "line must keep whose kitchen it is"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 209, "entry.txt is not 209 characters"
    assert len(raw) == 209, "entry.txt is not 209 bytes (pure ASCII line)"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
