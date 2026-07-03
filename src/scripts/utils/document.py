"""
Document Utility

Provides document read/write helpers for
Developer Automation scripts.

STOCK-CIO
"""

from __future__ import annotations

from pathlib import Path


class Document:
    """Utility class for text document operations."""

    def __init__(self, path: Path):
        self._path = path

    @property
    def path(self) -> Path:
        """Return document path."""

        return self._path

    @property
    def exists(self) -> bool:
        """Return whether document exists."""

        return self._path.exists()

    def read(self, encoding: str = "utf-8") -> str:
        """
        Read document.

        Raises
        ------
        FileNotFoundError
            If the document does not exist.
        """

        return self._path.read_text(encoding=encoding)

    def write(
        self,
        text: str,
        encoding: str = "utf-8",
    ) -> None:
        """
        Overwrite document.
        """

        self._path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self._path.write_text(
            text,
            encoding=encoding,
            newline="\n",
        )

    def append(
        self,
        text: str,
        encoding: str = "utf-8",
    ) -> None:
        """
        Append text to document.
        """

        self._path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with self._path.open(
            "a",
            encoding=encoding,
            newline="\n",
        ) as file:
            file.write(text)

    def replace(
        self,
        old: str,
        new: str,
        encoding: str = "utf-8",
    ) -> bool:
        """
        Replace text.

        Returns
        -------
        bool
            True if replacement occurred.
        """

        content = self.read(encoding)

        if old not in content:
            return False

        content = content.replace(old, new)

        self.write(
            content,
            encoding=encoding,
        )

        return True

    def ensure_exists(
        self,
        default: str = "",
        encoding: str = "utf-8",
    ) -> None:
        """
        Create document if missing.
        """

        if self.exists:
            return

        self.write(
            default,
            encoding=encoding,
        )