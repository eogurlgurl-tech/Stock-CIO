"""
Portfolio Analyzer

Stock-CIO
"""

from src.models.portfolio import Portfolio


class PortfolioAnalyzer:
    """포트폴리오 분석"""

    def analyze(self, portfolio: Portfolio) -> float:
        """Portfolio Score 계산"""

        score = 0.0

        # ==========================
        # Cash Ratio (25)
        # ==========================

        score += self._cash_score(
            portfolio.cash_ratio
        )

        # ==========================
        # Stock Ratio (25)
        # ==========================

        score += self._stock_score(
            portfolio.stock_ratio
        )

        # ==========================
        # Diversification (20)
        # ==========================

        score += self._diversification_score(
            len(portfolio.positions)
        )

        # ==========================
        # Profit Rate (20)
        # ==========================

        score += self._profit_score(
            portfolio.total_profit_rate
        )

        # ==========================
        # Loss Risk (10)
        # ==========================

        score += self._risk_score(
            portfolio.total_profit_rate
        )

        return round(score, 2)

    # ==================================================

    @staticmethod
    def _cash_score(cash_ratio: float) -> float:

        if 20 <= cash_ratio <= 40:
            return 25

        if 10 <= cash_ratio < 20:
            return 20

        if 40 < cash_ratio <= 60:
            return 20

        return 10

    # ==================================================

    @staticmethod
    def _stock_score(stock_ratio: float) -> float:

        if 60 <= stock_ratio <= 80:
            return 25

        if 40 <= stock_ratio < 60:
            return 20

        if 80 < stock_ratio <= 90:
            return 20

        return 10

    # ==================================================

    @staticmethod
    def _diversification_score(count: int) -> float:

        if 5 <= count <= 10:
            return 20

        if 3 <= count <= 4:
            return 15

        if count >= 11:
            return 15

        return 10

    # ==================================================

    @staticmethod
    def _profit_score(profit_rate: float) -> float:

        if profit_rate >= 20:
            return 20

        if profit_rate >= 10:
            return 16

        if profit_rate >= 0:
            return 12

        return 6

    # ==================================================

    @staticmethod
    def _risk_score(profit_rate: float) -> float:

        if profit_rate >= 0:
            return 10

        if profit_rate >= -5:
            return 8

        if profit_rate >= -10:
            return 5

        return 2