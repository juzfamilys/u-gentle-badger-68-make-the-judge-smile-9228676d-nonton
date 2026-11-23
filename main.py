"""Make the Judge Smile — one warm line about a small good thing today.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python standard library; deterministic output.
"""

import os

LINE = (
    "This morning the warung auntie slipped an extra krupuk into my bag, "
    "whispering 'for the cat' \u2014 and Oyen crunched it on the porch like "
    "a food critic giving five stars."
)


def validate(text):
    """Enforce the competition gate: 1-200 chars, single line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if text.strip() == "":
        raise ValueError("entry must not be blank or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    count = len(text)
    if count < 1 or count > 200:
        raise ValueError("entry must be 1-200 characters, got %d" % count)
    return count


def main():
    count = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    with open(path, "r", encoding="utf-8") as handle:
        landed = handle.read()
    if landed != LINE + "\n":
        raise ValueError("output on disk does not match the entry line")
    validate(landed.rstrip("\n"))
    print("entry (%d chars): %s" % (count, LINE))


if __name__ == "__main__":
    main()
