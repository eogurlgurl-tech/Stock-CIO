"""
Update Status Document

Updates docs/STATUS.md.

STOCK-CIO
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from src.scripts.base import AutomationTask
from src.scripts.utils.project_info import get_project_info


class StatusUpdater(AutomationTask):
    """Updates STATUS.md."""

    def __init__(self) -> None:
        self._project = get_project_info()

    @property
    def status_file(self) -> Path:
        """Return STATUS.md path."""
        return self._project.docs / "STATUS.md"

    def build_content(self) -> str:
        """Build STATUS.md."""

        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        return f"""# Project Status

## Version

{self._project.version}

## Updated

{now}

## Developer Automation

- Framework Ready
- AutomationTask
- AutomationRunner
- Production Quality

"""

    def run(self) -> None:
        """Execute automation task."""

        self.status_file.write_text(
            self.build_content(),
            encoding="utf-8",
        )


def main() -> None:
    """Program entry."""

    StatusUpdater().run()


if __name__ == "__main__":
    main()