"""
Project State Utility

Loads the project automation state from docs/project_state.json.

STOCK-CIO
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .project_info import discover_project_root


@dataclass(frozen=True, slots=True)
class Project:
    """Project metadata."""

    name: str
    version: str


@dataclass(frozen=True, slots=True)
class Current:
    """Current sprint information."""

    sprint: str
    feature: str


@dataclass(frozen=True, slots=True)
class Build:
    """Build information."""

    status: str
    tests: str


@dataclass(frozen=True, slots=True)
class ProjectState:
    """Immutable project automation state."""

    project: Project
    current: Current
    build: Build

    architecture: tuple[str, ...]
    completed: tuple[str, ...]
    next: tuple[str, ...]

    @classmethod
    def load(
        cls,
        path: Path | None = None,
    ) -> "ProjectState":
        """
        Load project state from JSON.

        Parameters
        ----------
        path
            Optional explicit JSON file.

        Raises
        ------
        FileNotFoundError
            If the state file does not exist.

        ValueError
            If required fields are missing.
        """

        if path is None:
            root = discover_project_root()
            path = root / "docs" / "project_state.json"

        with path.open(
            "r",
            encoding="utf-8",
        ) as fp:
            data = json.load(fp)

        try:
            return cls(
                project=Project(**data["project"]),
                current=Current(**data["current"]),
                build=Build(**data["build"]),
                architecture=tuple(data["architecture"]),
                completed=tuple(data["completed"]),
                next=tuple(data["next"]),
            )

        except KeyError as exc:
            raise ValueError(
                f"Missing required section: {exc.args[0]}"
            ) from exc

    def to_dict(self) -> dict:
        """Convert state to serializable dictionary."""

        return {
            "project": {
                "name": self.project.name,
                "version": self.project.version,
            },
            "current": {
                "sprint": self.current.sprint,
                "feature": self.current.feature,
            },
            "build": {
                "status": self.build.status,
                "tests": self.build.tests,
            },
            "architecture": list(self.architecture),
            "completed": list(self.completed),
            "next": list(self.next),
        }

    def save(
        self,
        path: Path | None = None,
    ) -> None:
        """
        Save state back to JSON.
        """

        if path is None:
            root = discover_project_root()
            path = root / "docs" / "project_state.json"

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with path.open(
            "w",
            encoding="utf-8",
            newline="\n",
        ) as fp:
            json.dump(
                self.to_dict(),
                fp,
                indent=4,
                ensure_ascii=False,
            )
            fp.write("\n")