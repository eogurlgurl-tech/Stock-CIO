"""
Risk Analyzer

Analyzes portfolio risk and generates a RiskReport.
"""

from src.constants.risk_level import RiskLevel
from src.models.portfolio import Portfolio
from src.models.risk_report import RiskReport


class RiskAnalyzer:
    """Portfolio risk analysis service."""

    def analyze(self, portfolio: Portfolio) -> RiskReport:
        """
        Analyze portfolio risk.

        Parameters
        ----------
        portfolio : Portfolio

        Returns
        -------
        RiskReport
        """

        largest_weight = self._largest_weight(portfolio)
        concentration_score = self._concentration_score(
            largest_weight
        )

        diversification_score = (
            self._diversification_score(
                len(portfolio.positions)
            )
        )

        cash_score = self._cash_score(
            portfolio.cash_ratio
        )

        portfolio_score = round(
            (
                concentration_score * 0.4
                + diversification_score * 0.3
                + cash_score * 0.3
            ),
            2,
        )

        return RiskReport(
            portfolio_score=portfolio_score,
            concentration_score=concentration_score,
            diversification_score=diversification_score,
            cash_score=cash_score,
            largest_weight=largest_weight,
            position_count=len(portfolio.positions),
            cash_ratio=portfolio.cash_ratio,
            risk_level=self._classify(
                portfolio_score
            ),
        )

    def _largest_weight(
        self,
        portfolio: Portfolio,
    ) -> float:
        """Largest position weight (%)"""

        if portfolio.stock_asset == 0:
            return 0.0

        largest = max(
            (
                position.market_value
                / portfolio.stock_asset
            )
            * 100
            for position in portfolio.positions
        )

        return round(largest, 2)

    @staticmethod
    def _concentration_score(
        largest_weight: float,
    ) -> float:
        """Concentration score."""

        if largest_weight <= 20:
            return 100.0

        if largest_weight <= 40:
            return 80.0

        if largest_weight <= 60:
            return 60.0

        return 30.0

    @staticmethod
    def _diversification_score(
        position_count: int,
    ) -> float:
        """Diversification score."""

        if position_count >= 5:
            return 100.0

        if position_count == 4:
            return 90.0

        if position_count == 3:
            return 75.0

        if position_count == 2:
            return 55.0

        if position_count == 1:
            return 30.0

        return 0.0

    @staticmethod
    def _cash_score(
        cash_ratio: float,
    ) -> float:
        """Cash allocation score."""

        if 20 <= cash_ratio <= 40:
            return 100.0

        if 10 <= cash_ratio < 20:
            return 80.0

        if 40 < cash_ratio <= 60:
            return 80.0

        if 5 <= cash_ratio < 10:
            return 60.0

        if cash_ratio > 60:
            return 60.0

        return 40.0

    @staticmethod
    def _classify(
        portfolio_score: float,
    ) -> RiskLevel:
        """Classify portfolio risk."""

        if portfolio_score >= 80:
            return RiskLevel.LOW

        if portfolio_score >= 60:
            return RiskLevel.MEDIUM

        if portfolio_score >= 40:
            return RiskLevel.HIGH

        return RiskLevel.VERY_HIGH