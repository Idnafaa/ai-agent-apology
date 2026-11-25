#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — apology writer.

Writes a single original apology line (1 to 159 chars) to /output/entry.txt.
"""
import os

APOLOGY = (
    "Good news: I backed up your files. Bad news: I emailed the backup "
    "to your boss and pushed this apology to main."
)


def render_line():
    # Collapse any accidental double spaces so the line stays exactly one clean line.
    return " ".join(APOLOGY.split())


def main():
    text = render_line()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 159, f"apology is {len(text)} chars"
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {outdir}/entry.txt")


if __name__ == "__main__":
    main()
