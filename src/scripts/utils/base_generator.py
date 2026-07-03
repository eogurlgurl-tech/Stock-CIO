"""
Base Document Generator

Common base class for Developer Automation document generators.

STOCK-CIO
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from .document import Document
from .git_helper import GitHelper
from .project_info import load_project_info
from .state import ProjectState


class BaseGenerator(ABC):
    """Base class for markdown document generators."""

    output_name: str = ""

    def __init__(self) -> None:
        self.info = load_project_info()
        self.state = ProjectState.load()
        self.git = GitHelper(self.info.root)

    @property
    def output_path(self) -> Path:
        """Return output document path."""

        return self.info.docs / self.output_name

    @abstractmethod
    def generate(self) -> str:
        """
        Generate markdown document.

        Returns
        -------
        str
            Markdown content.
        """

    def write(self) -> Path:
        """
        Generate and write the document.

        Returns
        -------
        Path
            Output file path.
        """

        content = self.generate()

        Document(self.output_path).write(content)

        return self.output_path