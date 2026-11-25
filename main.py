"""One Line, One Laugh — make.fun entry.

Writes a single funny line to /output/entry.txt.
"""

import os

ENTRY_TEXT = "I told my plants I was going on holiday. The ficus dropped three leaves by noon, and the cactus filed a formal complaint."
# One scene, one gag: the plants take the holiday personally.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
