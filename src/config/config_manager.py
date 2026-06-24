from pathlib import Path
import yaml


class ConfigManager:
    """Application configuration manager."""

    def __init__(self) -> None:
        self.config_path = Path("10_CONFIG/app.yaml")
        self.config = {}

    def load(self) -> None:
        """Load configuration file."""

        with open(self.config_path, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

    def get(self, key: str):
        """Return config value."""

        return self.config.get(key)