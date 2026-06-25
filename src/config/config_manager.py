"""
Configuration Manager

Stock-CIO
"""

from pathlib import Path

import yaml


class ConfigManager:
    """YAML 설정 관리"""

    CONFIG_DIR = Path("10_CONFIG")

    def load(self, name: str) -> dict:

        path = self.CONFIG_DIR / f"{name}.yaml"

        if not path.exists():
            raise FileNotFoundError(path)

        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)