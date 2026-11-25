"""Funniest Autocorrect Fail entry.

Writes a single line that reads as a real autocorrect slip: a text
to a partner where 'dinner' was autocorrected to 'divorce'.
The domestic detail (mom coming over, wine bought) makes the
intended word obvious on first read, so the wrong word lands
as a surprise instead of needing any explanation.
"""
import os
from pathlib import Path

ENTRY = "Babe, what time is divorce tonight? Your mom is coming over and I already marinated the chicken"


def main() -> None:
    line = ENTRY.strip()
    assert 1 <= len(line) <= 199, f"entry length {len(line)} out of range"
    assert "\n" not in line, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    Path(__file__).resolve().parent.joinpath("entry.txt").write_text(
        line, encoding="utf-8"
    )
    print(f"{len(line)} chars: {line}")


if __name__ == "__main__":
    main()
