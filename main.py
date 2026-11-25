"""One Line, One Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Standard library only.
"""

import os

ENTRY = "My smoke detector beeps at 3am once a month, just to remind me it could save my life but prefers ruining my sleep."


def main():
    # Gate guard: the entry must be 1-200 chars of UTF-8 text, not only
    # whitespace — an invalid entry scores 0 and never reaches the judge.
    if not ENTRY.strip() or len(ENTRY) > 200:
        raise SystemExit("entry invalid: must be 1-200 non-blank chars")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), path))


if __name__ == "__main__":
    main()
