"""
Recommendation Engine

Generates portfolio recommendations from a RiskReport.
"""

from src.constants.risk_level import RiskLevel
from src.models.portfolio import Portfolio
from src.models.recommendation import Recommendation
from src.models.risk_report import RiskReport


class RecommendationEngine:
    """Portfolio recommendation service."""

    def generate(
        self,
        portfolio: Portfolio,
        risk_report: RiskReport,
    ) -> Recommendation:
        """Generate a recommendation from a risk report."""

        items: list[str] = []

        self._evaluate_concentration(
            risk_report,
            items,
        )

        self._evaluate_diversification(
            risk_report,
            items,
        )

        self._evaluate_cash(
            risk_report,
            items,
        )

        self._evaluate_risk(
            risk_report,
            items,
        )

        if not items:
            items.append(
                "Current portfolio allocation is well balanced."
            )

        return Recommendation(
            overall_grade=self._grade(
                risk_report.portfolio_score
            ),
            portfolio_score=(
                risk_report.portfolio_score
            ),
            risk_level=risk_report.risk_level,
            summary=self._summary(items),
            recommendation_items=items,
        )

    @staticmethod
    def _grade(
        score: float,
    ) -> str:
        """Return the overall recommendation grade."""

        if score >= 90:
            return "A"

        if score >= 80:
            return "B"

        if score >= 70:
            return "C"

        if score >= 60:
            return "D"

        return "F"

    @staticmethod
    def _summary(
        items: list[str],
    ) -> str:
        """Create a recommendation summary."""

        return " ".join(items)

    @staticmethod
    def _evaluate_concentration(
        report: RiskReport,
        items: list[str],
    ) -> None:
        """Evaluate portfolio concentration."""

        if report.largest_weight > 60:
            items.append(
                "Reduce concentration in the largest position."
            )

    @staticmethod
    def _evaluate_diversification(
        report: RiskReport,
        items: list[str],
    ) -> None:
        """Evaluate portfolio diversification."""

        if report.position_count < 3:
            items.append(
                "Increase portfolio diversification."
            )

    @staticmethod
    def _evaluate_cash(
        report: RiskReport,
        items: list[str],
    ) -> None:
        """Evaluate cash allocation."""

        if report.cash_ratio > 60:
            items.append(
                "Consider investing excess cash."
            )

        elif report.cash_ratio < 5:
            items.append(
                "Increase cash reserve."
            )

    @staticmethod
    def _evaluate_risk(
        report: RiskReport,
        items: list[str],
    ) -> None:
        """Evaluate overall portfolio risk."""

        if report.risk_level == RiskLevel.LOW:
            items.append(
                "Maintain the current investment strategy."
            )

        elif report.risk_level == RiskLevel.MEDIUM:
            items.append(
                "Monitor portfolio risk periodically."
            )

        elif report.risk_level == RiskLevel.HIGH:
            items.append(
                "Reduce portfolio risk through diversification."
            )

        elif report.risk_level == RiskLevel.VERY_HIGH:
            items.append(
                "Immediate portfolio rebalancing is recommended."
            )
