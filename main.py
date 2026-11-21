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


def verify_entry(path: Path) -> str | None:
    """Return an error message if the written entry is invalid, else None."""
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    if len(lines) != 1:
        return f"expected exactly one line, got {len(lines)}"
    line = lines[0]
    # len() on str counts Unicode code points, not bytes.
    if not 1 <= len(line) <= 280:
        return f"line length {len(line)} outside 1..280 code points"
    if not line.strip():
        return "line is only whitespace"
    return None


def main() -> int:
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        OUTPUT_FILE.write_text(JOKE + "\n", encoding="utf-8")
        problem = verify_entry(OUTPUT_FILE)
    except OSError as exc:
        # Surface the exact filesystem error rather than guessing.
        print(f"error writing {OUTPUT_FILE}: {exc}", file=sys.stderr)
        return 1
    if problem is not None:
        print(f"error: read-back check failed for {OUTPUT_FILE}: {problem}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
