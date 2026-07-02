"""
Market Value Weight Strategy

Stock-CIO
"""

from src.models.portfolio import Portfolio

from .allocation_strategy import AllocationStrategy


class MarketValueWeightStrategy(AllocationStrategy):
    """Market Value Weight Allocation Strategy"""

    def allocate(
        self,
        portfolio: Portfolio,
    ) -> Portfolio:
        """
        평가금액 기준 비중 계산
        """

        total_asset = portfolio.stock_asset

        if total_asset == 0:
            for position in portfolio.positions:
                position.weight = 0.0

            return portfolio

        for position in portfolio.positions:
            position.weight = (
                position.market_value
                / total_asset
            ) * 100

        return portfolio