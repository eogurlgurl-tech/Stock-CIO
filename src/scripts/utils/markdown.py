"""
Markdown Builder Utility

Utility for building consistently formatted markdown documents.

STOCK-CIO
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


@dataclass(slots=True)
class MarkdownBuilder:
    """Utility class for generating markdown text."""

    _lines: list[str] = field(default_factory=list)

    def heading(self, text: str, level: int = 1) -> "MarkdownBuilder":
        """
        Add a markdown heading.

        Parameters
        ----------
        text:
            Heading text.
        level:
            Heading level (1~6).
        """

        if not 1 <= level <= 6:
            raise ValueError("Heading level must be between 1 and 6.")

        self._lines.append(f'{"#" * level} {text}')
        self._lines.append("")
        return self

    def text(self, text: str = "") -> "MarkdownBuilder":
        """Add a paragraph."""

        self._lines.append(text)
        return self

    def blank(self) -> "MarkdownBuilder":
        """Insert one blank line."""

        self._lines.append("")
        return self

    def bullet(self, text: str) -> "MarkdownBuilder":
        """Add a bullet item."""

        self._lines.append(f"- {text}")
        return self

    def bullets(self, items: Iterable[str]) -> "MarkdownBuilder":
        """Add multiple bullet items."""

        for item in items:
            self.bullet(item)

        return self

    def numbered(self, items: Iterable[str]) -> "MarkdownBuilder":
        """Add numbered list."""

        for index, item in enumerate(items, start=1):
            self._lines.append(f"{index}. {item}")

        return self

    def quote(self, text: str) -> "MarkdownBuilder":
        """Add block quote."""

        self._lines.append(f"> {text}")
        return self

    def code(
        self,
        code: str,
        language: str = "",
    ) -> "MarkdownBuilder":
        """Add fenced code block."""

        self._lines.append(f"```{language}")
        self._lines.extend(code.splitlines())
        self._lines.append("```")
        return self

    def table(
        self,
        headers: list[str],
        rows: Iterable[Iterable[str]],
    ) -> "MarkdownBuilder":
        """
        Add markdown table.
        """

        self._lines.append("| " + " | ".join(headers) + " |")
        self._lines.append("| " + " | ".join("---" for _ in headers) + " |")

        for row in rows:
            self._lines.append(
                "| " + " | ".join(str(value) for value in row) + " |"
            )

        return self

    def horizontal_rule(self) -> "MarkdownBuilder":
        """Insert horizontal rule."""

        self._lines.append("---")
        return self

    def build(self) -> str:
        """Return markdown string."""

        text = "\n".join(self._lines).rstrip()
        return text + "\n"

    def clear(self) -> None:
        """Reset builder."""

        self._lines.clear()