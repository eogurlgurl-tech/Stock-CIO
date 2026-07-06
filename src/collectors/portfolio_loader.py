"""
Portfolio Loader

Stock-CIO
"""

from typing import Any

from src.config.config_manager import ConfigManager
from src.models.portfolio import Portfolio
from src.models.position import Position


class PortfolioLoader:
    """Load the current portfolio from configuration."""

    def __init__(
        self,
        config_manager: ConfigManager | None = None,
    ) -> None:
        """Initialize the loader with a configuration manager."""

        self._config_manager = (
            config_manager
            if config_manager is not None
            else ConfigManager()
        )

    def load(self) -> Portfolio:
        """Load and validate the current portfolio."""

        config = self._config_manager.load("portfolio")

        if not isinstance(config, dict):
            raise ValueError(
                "Portfolio configuration must be a mapping."
            )

        cash = self._non_negative_float(
            config.get("cash", 0.0),
            "cash",
        )
        position_configs = config.get("positions", [])

        if not isinstance(position_configs, list):
            raise ValueError(
                "Portfolio positions must be a list."
            )

        positions = [
            self._build_position(position_config, index)
            for index, position_config in enumerate(
                position_configs
            )
        ]

        return Portfolio(
            cash=cash,
            positions=positions,
        )

    def _build_position(
        self,
        config: Any,
        index: int,
    ) -> Position:
        """Build and validate one configured position."""

        prefix = f"positions[{index}]"

        if not isinstance(config, dict):
            raise ValueError(
                f"{prefix} must be a mapping."
            )

        ticker = config.get("ticker")

        if not isinstance(ticker, str) or not ticker.strip():
            raise ValueError(
                f"{prefix}.ticker must be a non-empty string."
            )

        name = config.get("name", "")

        if not isinstance(name, str):
            raise ValueError(
                f"{prefix}.name must be a string."
            )

        return Position(
            ticker=ticker.strip(),
            name=name.strip(),
            quantity=self._non_negative_int(
                config.get("quantity", 0),
                f"{prefix}.quantity",
            ),
            average_price=self._non_negative_float(
                config.get("average_price", 0.0),
                f"{prefix}.average_price",
            ),
            current_price=self._non_negative_float(
                config.get("current_price", 0.0),
                f"{prefix}.current_price",
            ),
        )

    @staticmethod
    def _non_negative_float(
        value: Any,
        field: str,
    ) -> float:
        """Return a validated non-negative float."""

        if isinstance(value, bool):
            raise ValueError(
                f"{field} must be a non-negative number."
            )

        try:
            result = float(value)
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"{field} must be a non-negative number."
            ) from error

        if result < 0:
            raise ValueError(
                f"{field} must be a non-negative number."
            )

        return result

    @staticmethod
    def _non_negative_int(
        value: Any,
        field: str,
    ) -> int:
        """Return a validated non-negative integer."""

        if (
            isinstance(value, bool)
            or not isinstance(value, int)
            or value < 0
        ):
            raise ValueError(
                f"{field} must be a non-negative integer."
            )

        return value
