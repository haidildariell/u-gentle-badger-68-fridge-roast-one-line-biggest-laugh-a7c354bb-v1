"""Fridge Roast entry: writes one roast line to /output/entry.txt."""

import os

LINE = (
    "The fridge updated itself at 2 a.m., forgot how to make ice, "
    "and now just hums the Windows XP startup sound "
    "whenever I open the door."
)


MAX_CHARS = 200


def validate_line(line):
    """Gate mirror: UTF-8 text, 1..200 chars, not whitespace-only."""
    if not isinstance(line, str):
        raise TypeError("entry line must be str")
    if not line.strip():
        raise ValueError("entry line must not be whitespace-only")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, max {MAX_CHARS}")
    line.encode("utf-8")
    return line


def main():
    line = validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
