"""
CIO Engine

Generates the final CIO investment report from
the investment decision.

STOCK-CIO
"""

from __future__ import annotations

from src.constants.decision_type import DecisionType
from src.models.cio_report import CIOReport
from src.models.decision import Decision


class CIOEngine:
    """Final CIO report generation service."""

    def generate(
        self,
        decision: Decision,
    ) -> CIOReport:
        """
        Generate the final CIO investment report.
        """

        portfolio_summary = self._build_portfolio_summary()

        recommended_action = self._build_action(
            decision.decision,
        )

        investment_comment = self._build_comment(
            decision,
        )

        return CIOReport(
            decision=decision,
            portfolio_summary=portfolio_summary,
            recommended_action=recommended_action,
            investment_comment=investment_comment,
        )

    @staticmethod
    def _build_portfolio_summary() -> str:
        """Build portfolio summary."""

        return (
            "Portfolio allocation has been evaluated "
            "based on the latest analysis."
        )

    @staticmethod
    def _build_action(
        decision: DecisionType,
    ) -> str:
        """Build recommended action."""

        if decision == DecisionType.BUY:
            return "Increase equity exposure."

        if decision == DecisionType.SELL:
            return "Reduce equity exposure."

        return "Maintain current allocation."

    @staticmethod
    def _build_comment(
        decision: Decision,
    ) -> str:
        """Build CIO investment comment."""

        if decision.decision == DecisionType.BUY:
            return (
                "Current market conditions support "
                "gradual accumulation."
            )

        if decision.decision == DecisionType.SELL:
            return (
                "Risk factors have increased. "
                "Consider reducing exposure."
            )

        return (
            "Current portfolio remains balanced. "
            "Continue monitoring market conditions."
        )