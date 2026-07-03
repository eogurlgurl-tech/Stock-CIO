"""
Update Session Document

Updates docs/SESSION.md with the latest development session
information.

STOCK-CIO
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from src.scripts.utils.project_info import get_project_info


class SessionUpdater:
    """Updates SESSION.md."""

    def __init__(self) -> None:
        self.project = get_project_info()

    @property
    def session_file(self) -> Path:
        """Return SESSION.md path."""
        return self.project.docs / "SESSION.md"

    def build_content(self) -> str:
        """Build SESSION.md contents."""

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        return f"""# Development Session

## Version

{self.project.version}

## Updated

{timestamp}

## Current Sprint

Sprint D1-HF01

## Current Task

Developer Automation Rebuild

## Completed

- ProjectInfo rebuilt
- Status updater rebuilt
- Session updater rebuilt

## Next

- update_next_task.py
- update_changelog.py
- finish_feature.py
- pytest

"""

    def update(self) -> None:
        """Write SESSION.md."""

        self.session_file.write_text(
            self.build_content(),
            encoding="utf-8",
        )


def main() -> None:
    """Program entry point."""
    SessionUpdater().update()


if __name__ == "__main__":
    main()