"""
Project Information Utility

Provides project metadata and commonly used paths for
Developer Automation scripts.

STOCK-CIO
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ProjectInfo:
    """Immutable project information."""

    root: Path
    docs: Path
    src: Path
    tests: Path
    scripts: Path
    utils: Path

    version: str = "v0.4.0-alpha"


def find_project_root(start: Path | None = None) -> Path:
    """
    Locate the project root.

    Starting from this file (or a supplied path), walk upward until a
    directory containing src/, tests/, and docs/ is found.

    Raises
    ------
    RuntimeError
        If the project root cannot be located.
    """

    current = (start or Path(__file__).resolve()).parent

    while True:
        if (
            (current / "src").is_dir()
            and (current / "tests").is_dir()
            and (current / "docs").is_dir()
        ):
            return current

        if current.parent == current:
            break

        current = current.parent

    raise RuntimeError("Unable to locate STOCK-CIO project root.")


def get_project_info() -> ProjectInfo:
    """
    Return immutable project information.

    Returns
    -------
    ProjectInfo
        Commonly used project paths.
    """

    root = find_project_root()

    src = root / "src"
    scripts = src / "scripts"

    return ProjectInfo(
        root=root,
        docs=root / "docs",
        src=src,
        tests=root / "tests",
        scripts=scripts,
        utils=scripts / "utils",
    )