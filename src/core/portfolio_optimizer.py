"""
Portfolio Optimizer

Stock-CIO
"""

from src.models.portfolio import Portfolio


class PortfolioOptimizer:
    """Portfolio Optimizer"""

    def update_weights(
        self,
        portfolio: Portfolio,
    ) -> Portfolio:
        """
        보유 종목 비중 계산
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