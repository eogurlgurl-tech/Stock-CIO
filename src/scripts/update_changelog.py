"""
Update CHANGELOG.md

Prepends a new changelog entry while preserving existing history.

STOCK-CIO
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path

from src.scripts.utils.project_info import get_project_info


@dataclass(frozen=True, slots=True)
class ChangelogEntry:
    """Represents a changelog entry."""

    version: str
    title: str
    items: tuple[str, ...]


class ChangelogUpdater:
    """Updates CHANGELOG.md."""

    def __init__(self) -> None:
        self._project = get_project_info()

    @property
    def changelog_file(self) -> Path:
        """Return CHANGELOG.md path."""
        return self._project.docs / "CHANGELOG.md"

    def _read_existing(self) -> str:
        """Read existing changelog if present."""
        if not self.changelog_file.exists():
            return ""

        return self.changelog_file.read_text(
            encoding="utf-8",
        )

    @staticmethod
    def _build_entry(entry: ChangelogEntry) -> str:
        """Build markdown entry."""

        today = date.today().isoformat()

        bullet_text = "\n".join(
            f"- {item}" for item in entry.items
        )

        return (
            f"## {entry.version} ({today})\n\n"
            f"### {entry.title}\n\n"
            f"{bullet_text}\n\n"
        )

    def update(self, entry: ChangelogEntry) -> None:
        """Update CHANGELOG.md."""

        existing = self._read_existing()

        if f"## {entry.version}" in existing:
            return

        header = "# CHANGELOG\n\n"

        if existing.startswith("# CHANGELOG"):
            _, _, body = existing.partition("\n\n")
            existing = body

        content = (
            header
            + self._build_entry(entry)
            + existing
        )

        self.changelog_file.write_text(
            content,
            encoding="utf-8",
        )


def main() -> None:
    """Program entry."""

    updater = ChangelogUpdater()

    updater.update(
        ChangelogEntry(
            version="v0.4.0-alpha",
            title="Sprint D1-HF01",
            items=(
                "Rebuilt project path detection.",
                "Updated developer automation.",
                "Aligned scripts with src/scripts layout.",
                "Improved portability.",
            ),
        )
    )


if __name__ == "__main__":
    main()