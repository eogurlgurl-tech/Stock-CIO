"""
Unit Tests for Portfolio Loader

Feature : FEATURE-027
Module  : Portfolio Loader
"""

import pytest

from src.collectors.portfolio_loader import PortfolioLoader


class PortfolioConfigStub:
    """Return predefined portfolio configuration."""

    def __init__(self, config):
        self._config = config

    def load(self, name: str):
        """Return the predefined configuration."""

        assert name == "portfolio"
        return self._config


def test_load_empty_portfolio():
    """Default configuration creates an empty portfolio."""

    loader = PortfolioLoader(
        PortfolioConfigStub(
            {
                "cash": 0.0,
                "positions": [],
            }
        )
    )

    portfolio = loader.load()

    assert portfolio.cash == 0.0
    assert portfolio.positions == []


def test_load_configured_portfolio():
    """Configured cash and positions are mapped."""

    loader = PortfolioLoader(
        PortfolioConfigStub(
            {
                "cash": 100000.0,
                "positions": [
                    {
                        "ticker": "005930",
                        "name": "Samsung Electronics",
                        "quantity": 10,
                        "average_price": 70000.0,
                        "current_price": 75000.0,
                    }
                ],
            }
        )
    )

    portfolio = loader.load()
    position = portfolio.positions[0]

    assert portfolio.cash == 100000.0
    assert position.ticker == "005930"
    assert position.name == "Samsung Electronics"
    assert position.quantity == 10
    assert position.average_price == 70000.0
    assert position.current_price == 75000.0


@pytest.mark.parametrize(
    "cash",
    [-1, "invalid", None, True],
)
def test_invalid_cash(cash):
    """Invalid cash values are rejected."""

    loader = PortfolioLoader(
        PortfolioConfigStub(
            {
                "cash": cash,
                "positions": [],
            }
        )
    )

    with pytest.raises(ValueError, match="cash"):
        loader.load()


def test_positions_must_be_list():
    """Positions must be configured as a list."""

    loader = PortfolioLoader(
        PortfolioConfigStub(
            {
                "cash": 0.0,
                "positions": {},
            }
        )
    )

    with pytest.raises(ValueError, match="positions"):
        loader.load()


@pytest.mark.parametrize(
    "position",
    [
        {},
        {"ticker": ""},
        {"ticker": "AAA", "quantity": -1},
        {"ticker": "AAA", "quantity": 1.5},
        {"ticker": "AAA", "average_price": -1},
        {"ticker": "AAA", "current_price": "invalid"},
    ],
)
def test_invalid_position(position):
    """Invalid position fields are rejected."""

    loader = PortfolioLoader(
        PortfolioConfigStub(
            {
                "cash": 0.0,
                "positions": [position],
            }
        )
    )

    with pytest.raises(ValueError, match=r"positions\[0\]"):
        loader.load()
