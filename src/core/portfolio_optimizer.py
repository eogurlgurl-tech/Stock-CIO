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
    """Portfolio Optimizer"""

    def __init__(
        self,
        strategy: AllocationStrategy | None = None,
    ) -> None:
        """
        Portfolio Optimizer

        Parameters
        ----------
        strategy : AllocationStrategy, optional
            Allocation strategy.
            Defaults to MarketValueWeightStrategy.
        """

        self._strategy = (
            strategy
            if strategy is not None
            else MarketValueWeightStrategy()
        )

    @property
    def strategy(self) -> AllocationStrategy:
        """Current Allocation Strategy"""

        return self._strategy

    def set_strategy(
        self,
        strategy: AllocationStrategy,
    ) -> None:
        """Change allocation strategy"""

        self._strategy = strategy

    def update_weights(
        self,
        portfolio: Portfolio,
    ) -> Portfolio:
        """Apply allocation strategy"""

        return self._strategy.allocate(portfolio)