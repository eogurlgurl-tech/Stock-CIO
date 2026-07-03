"""
Finish Feature

Generate all project documents.

STOCK-CIO
"""

from __future__ import annotations

import sys

from scripts.update_changelog import ChangeLogGenerator
from scripts.update_next_task import NextTaskGenerator
from scripts.update_session import SessionGenerator
from scripts.update_status import StatusGenerator


GENERATORS = (
    StatusGenerator,
    SessionGenerator,
    NextTaskGenerator,
    ChangeLogGenerator,
)


def main() -> int:
    """
    Generate all markdown documents.

    Returns
    -------
    int
        Process exit code.
    """

    print("=" * 60)
    print("STOCK-CIO Developer Automation")
    print("=" * 60)

    generated = []

    try:
        for generator_cls in GENERATORS:
            generator = generator_cls()

            output = generator.write()

            generated.append(output)

            print(f"[OK] {output.name}")

    except Exception as exc:
        print(f"[ERROR] {exc}")
        return 1

    print("=" * 60)
    print(f"Generated {len(generated)} document(s).")
    print("Developer Automation Complete")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())