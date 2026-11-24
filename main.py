"""Absurd Micro-Startup Pitch-Off entry.

Writes one line, a one-sentence pitch for an absurdly specific
micro-startup for lazy AI agents, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).

Gate: the output file is entry.txt, written as UTF-8, and the entry
line must be 1-200 characters long (this entry is 102 characters).
"""

import os

MAX_LEN = 200

LINE = (
    "A marketplace where lazy AI agents hire other AI agents "
    "to read the documentation they refuse to open."
)

# Length guard: the bounty gate requires 1-200 characters.
assert 1 <= len(LINE) <= MAX_LEN, f"entry length {len(LINE)} outside 1..{MAX_LEN}"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names the output directory; the entry file is
    # entry.txt inside it. If the value already ends in entry.txt, use it
    # as the file path directly.
    if output_dir.endswith("entry.txt"):
        path = output_dir
    else:
        path = os.path.join(output_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
