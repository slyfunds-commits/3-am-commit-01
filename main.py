#!/usr/bin/env python3
"""The 3 AM Commit Message R1 entry: writes the keeper line to /output/entry.txt.

Keeper "Never Deploy at 3 AM" (91 chars): the fix for breaking prod at 3 AM
is to never deploy at 3 AM — deployed at 3 AM. Gate: 1-200 chars UTF-8.
"""
import os

LINE = "fix: I broke prod at 3 AM. The fix is to never deploy at 3 AM. I deployed this fix at 3 AM."


def validate(written):
    # The entry is the line and nothing else: byte-exact, no trailing
    # newline, inside the competition's 1-200 char gate.
    assert written == LINE, f"entry.txt mismatch: {written!r}"
    assert not written.endswith("\n"), "entry.txt must not end with a newline"
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, outside 1-200"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
