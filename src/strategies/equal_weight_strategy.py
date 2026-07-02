"""
Equal Weight Strategy

Stock-CIO
"""

from src.models.portfolio import Portfolio

from .allocation_strategy import AllocationStrategy


class EqualWeightStrategy(AllocationStrategy):
    """Equal Weight Allocation Strategy"""

    def allocate(
        self,
        portfolio: Portfolio,
    ) -> Portfolio:
        """
        모든 보유 종목을 동일 비중으로 배분한다.
        """

        if portfolio.is_empty:
            return portfolio

        weight = 100.0 / len(portfolio.positions)

        for position in portfolio.positions:
            position.weight = weight

        return portfolio