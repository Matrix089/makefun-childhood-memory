#!/usr/bin/env python3
"""Write a childhood memory for make.fun's
Make the AI Judge Feel Nostalgic: A Childhood Memory bounty.

Why this entry fits the judge's brief: it is one sentence built
around one concrete, believable childhood moment -- hiding under
Grandma's kitchen table to steal warm dumplings, her pretending
not to see my feet sticking out -- with a small honest detail
(the feet give the hiding away) and a warm ache that lingers: the adult still checks under the
table first in her now-empty kitchen. Specific ritual, real
place, child logic, and a present-day echo, not generic
pretty prose about summer evenings.
"""

import os

LINE = (
    "I used to hide under Grandma's kitchen table to steal warm "
    "dumplings off the plate, and she always pretended not to see "
    "my feet sticking out, so now I still check under the table "
    "first whenever I visit her empty kitchen."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-280 characters, a single sentence.
    # The line was counted at exactly 220 characters; pin that
    # so any accidental wording change fails loudly instead of
    # silently shipping a different (or over-long) entry.
    assert len(line) == 220, f"line is {len(line)} characters, expected 220"
    assert 1 <= len(line) <= 280, f"line is {len(line)} characters"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert line.strip() == line, "line must not have surrounding whitespace"
    # One sentence: exactly one period, the final character.
    assert line.count(".") == 1, "line must be a single sentence"
    assert line.endswith("."), "line must end with its single period"
    # The judge's brief: a specific childhood memory with concrete
    # senses, not a generic "I miss childhood" -- warm dumplings,
    # the kitchen table, feet sticking out, the empty kitchen now.
    assert "warm dumplings" in line, "line must keep its sensory detail"
    assert "kitchen table" in line, "line must keep the kitchen table"
    assert "feet sticking out" in line, "line must keep the honest detail"
    assert "empty kitchen" in line, "line must keep the lingering ache"
    assert "Grandma" in line, "line must keep whose kitchen it is"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 220, "entry.txt is not 220 characters"
    assert len(raw) == 220, "entry.txt is not 220 bytes (pure ASCII line)"
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
