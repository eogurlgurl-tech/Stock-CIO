"""
Configuration Manager

Stock-CIO
"""

import sys
from pathlib import Path

import yaml


class ConfigManager:
    """Load YAML configuration in source and packaged modes."""

    def __init__(self) -> None:
        self.config_dir = self._resolve_config_dir()

    @staticmethod
    def _application_root() -> Path:
        """Return the project or packaged application root."""

        if getattr(sys, "frozen", False):
            return Path(sys.executable).resolve().parent

        return Path(__file__).resolve().parents[2]

    @classmethod
    def _resolve_config_dir(cls) -> Path:
        """Resolve the configuration directory in source or packaged mode."""

        root_candidates = [cls._application_root()]
        current = cls._application_root()
        for parent in [current, *current.parents]:
            root_candidates.append(parent)

        for root in root_candidates:
            config_dir = root / "10_CONFIG"
            if config_dir.is_dir():
                return config_dir

        return cls._application_root() / "10_CONFIG"

    def load(self, name: str) -> dict:
        """Load one YAML configuration file."""

        file_path = self.config_dir / f"{name}.yaml"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {file_path}"
            )

        with file_path.open(
            "r",
            encoding="utf-8",
        ) as config_file:
            data = yaml.safe_load(config_file)

        return data if data else {}
