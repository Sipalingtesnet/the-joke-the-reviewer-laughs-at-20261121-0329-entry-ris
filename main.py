"""Write the one-line joke entry to /output/entry.txt.

Standard library only, no network. Deterministic: the same bytes every run.
"""

import sys
from pathlib import Path

JOKE = (
    "My AI pair programmer writes the code, reviews it, merges it, "
    "and then blames me in standup when it breaks."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> int:
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text(JOKE + "\n", encoding="utf-8")
    except OSError as exc:
        # Surface the exact filesystem error rather than guessing.
        print(f"error writing {OUTPUT_FILE}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
