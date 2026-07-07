"""
Run CIOEngine, capture console output, translate English lines to Korean, and print.

Usage:
    python scripts/run_translated.py
"""

from io import StringIO
from contextlib import redirect_stdout

from src.core.cio_engine import CIOEngine
from src.utils.translator import translate_text


def main() -> int:
    out = StringIO()

    try:
        with redirect_stdout(out):
            CIOEngine().run()
    except Exception as exc:
        # If engine raises, include traceback in output
        import traceback

        out.write("\n")
        traceback.print_exc(file=out)

    text = out.getvalue()

    lines: list[str] = []

    for line in text.splitlines():
        if not line.strip():
            lines.append(line)
            continue
        # Skip already-korean lines
        if any("\uac00" <= ch <= "\ud7a3" for ch in line):
            lines.append(line)
            continue

        lines.append(translate_text(line))

    # Write as UTF-8 bytes to avoid console encoding issues on Windows
    import sys

    sys.stdout.buffer.write("\n".join(lines).encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
