"""
Update Next Task Document

Updates docs/NEXT_TASK.md with the next planned development task.

STOCK-CIO
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from src.scripts.utils.project_info import get_project_info


class NextTaskUpdater:
    """Updates NEXT_TASK.md."""

    def __init__(self) -> None:
        self.project = get_project_info()

    @property
    def next_task_file(self) -> Path:
        """Return NEXT_TASK.md path."""
        return self.project.docs / "NEXT_TASK.md"

    def build_content(self) -> str:
        """Build NEXT_TASK.md contents."""

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        return f"""# Next Development Task

## Version

{self.project.version}

## Updated

{timestamp}

## Current Sprint

Sprint D1-HF01

## Current Feature

Developer Automation Rebuild

## Next Tasks

1. Rebuild update_changelog.py
2. Rebuild finish_feature.py
3. Execute all automation scripts
4. Run full pytest
5. Fix regression if detected
6. Complete Sprint D1-HF01

## Notes

- Use actual project structure (src/scripts)
- Use get_project_info() for all paths
- Keep pytest compatibility
- Full-file replacement only
"""

    def update(self) -> None:
        """Write NEXT_TASK.md."""
        self.next_task_file.write_text(
            self.build_content(),
            encoding="utf-8",
        )


def main() -> None:
    """Program entry point."""
    NextTaskUpdater().update()


if __name__ == "__main__":
    main()