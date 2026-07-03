"""
Git Helper Utility

Provides Git information for Developer Automation scripts.

STOCK-CIO
"""

from __future__ import annotations

import subprocess
from pathlib import Path


class GitHelper:
    """Utility wrapper around Git commands."""

    def __init__(self, root: Path):
        self._root = root

    def _run(self, *args: str) -> str | None:
        """
        Execute a Git command.

        Returns
        -------
        str | None
            Command output, or None if unavailable.
        """

        try:
            result = subprocess.run(
                ["git", *args],
                cwd=self._root,
                capture_output=True,
                text=True,
                check=False,
            )
        except OSError:
            return None

        if result.returncode != 0:
            return None

        return result.stdout.strip()

    def has_git(self) -> bool:
        """Return whether current directory is a Git repository."""

        output = self._run(
            "rev-parse",
            "--is-inside-work-tree",
        )

        return output == "true"

    def branch(self) -> str:
        """Return current branch."""

        return (
            self._run("branch", "--show-current")
            or "unknown"
        )

    def commit_hash(self, short: bool = True) -> str:
        """Return current commit hash."""

        args = ["rev-parse"]

        if short:
            args.append("--short")

        args.append("HEAD")

        return self._run(*args) or "unknown"

    def last_commit_message(self) -> str:
        """Return latest commit message."""

        return (
            self._run(
                "log",
                "-1",
                "--pretty=%s",
            )
            or "unknown"
        )

    def is_clean(self) -> bool:
        """Return True if working tree is clean."""

        output = self._run(
            "status",
            "--porcelain",
        )

        if output is None:
            return False

        return output == ""

    def changed_files(self) -> list[str]:
        """Return changed file list."""

        output = self._run(
            "status",
            "--porcelain",
        )

        if not output:
            return []

        files: list[str] = []

        for line in output.splitlines():
            if len(line) < 4:
                continue

            files.append(line[3:])

        return files

    def tracked_files(self) -> list[str]:
        """Return tracked files."""

        output = self._run("ls-files")

        if not output:
            return []

        return output.splitlines()

    def tag(self) -> str | None:
        """Return current tag if available."""

        return self._run(
            "describe",
            "--tags",
            "--exact-match",
        )