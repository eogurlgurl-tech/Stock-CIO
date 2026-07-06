"""
Target Portfolio Builder

Stock-CIO
"""

from src.models.portfolio import Portfolio
from src.models.position import Position
from src.strategies.allocation_strategy import AllocationStrategy
from src.strategies.rule_based_strategy import RuleBasedStrategy


class TargetPortfolioBuilder:
    """Build a target portfolio without changing the current portfolio."""

    def __init__(
        self,
        strategy: AllocationStrategy | None = None,
    ) -> None:
        """Initialize the builder with an allocation strategy."""

        self._strategy = (
            strategy
            if strategy is not None
            else RuleBasedStrategy()
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

    def build(
        self,
        current: Portfolio,
    ) -> Portfolio:
        """Build a target portfolio from the current portfolio."""

        target = self._clone_portfolio(current)

        return self._strategy.allocate(target)

    @staticmethod
    def _clone_portfolio(
        portfolio: Portfolio,
    ) -> Portfolio:
        """Clone a portfolio and its positions."""

        return Portfolio(
            cash=portfolio.cash,
            positions=[
                Position(
                    ticker=position.ticker,
                    name=position.name,
                    quantity=position.quantity,
                    average_price=position.average_price,
                    current_price=position.current_price,
                    weight=position.weight,
                )
                for position in portfolio.positions
            ],
        )
