"""
Portfolio Optimizer

Stock-CIO
"""

from src.models.portfolio import Portfolio
from src.strategies.allocation_strategy import AllocationStrategy
from src.strategies.market_value_weight_strategy import (
    MarketValueWeightStrategy,
)


class PortfolioOptimizer:
    """Calculate weights for the current portfolio."""

    def __init__(
        self,
        strategy: AllocationStrategy | None = None,
    ) -> None:
        """Initialize the optimizer with an allocation strategy."""

        self._strategy = (
            strategy
            if strategy is not None
            else MarketValueWeightStrategy()
        )

    @property
    def strategy(self) -> AllocationStrategy:
        """Return the current allocation strategy."""

        return self._strategy

    def set_strategy(
        self,
        strategy: AllocationStrategy,
    ) -> None:
        """Change the allocation strategy."""

        self._strategy = strategy

    def update_weights(
        self,
        portfolio: Portfolio,
    ) -> Portfolio:
        """Calculate and update current portfolio weights."""

        return self._strategy.allocate(portfolio)
