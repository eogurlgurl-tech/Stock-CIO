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
        Apply market value based allocation
        to the target portfolio.
        """

        total_asset = portfolio.stock_asset

        if total_asset <= 0:

            for position in portfolio.positions:
                position.weight = 0.0

            return portfolio

        for position in portfolio.positions:

            position.weight = round(
                (
                    position.market_value
                    / total_asset
                )
                * 100,
                2,
            )

        return portfolio