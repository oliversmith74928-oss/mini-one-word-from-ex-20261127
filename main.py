"""One Word From Your Ex — entry program.

Writes a single word describing the entrant, as their ex would,
to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

WORD = "almost"
# The word: my ex would call me "almost" — almost the one, almost
# ready, almost enough. One word, painfully honest, no explanation needed.


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
