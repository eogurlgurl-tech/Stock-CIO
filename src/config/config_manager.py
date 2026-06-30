"""
Configuration Manager

Stock-CIO
"""

from pathlib import Path

import yaml


class ConfigManager:
    """YAML Configuration Loader"""

    def __init__(self) -> None:

        self.config_dir = (
            Path(__file__).resolve().parents[2] / "10_CONFIG"
        )

    def load(self, name: str) -> dict:

        file_path = self.config_dir / f"{name}.yaml"

        if not file_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {file_path}"
            )

        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        return data if data else {}