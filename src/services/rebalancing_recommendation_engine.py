"""
Rebalancing Recommendation Engine

Generates portfolio rebalancing recommendations from a
Portfolio and RiskReport.
"""

from src.constants.rebalancing_action import (
    RebalancingAction,
)
from src.models.portfolio import Portfolio
from src.models.rebalancing_recommendation import (
    RebalancingRecommendation,
)
from src.models.risk_report import RiskReport


class RebalancingRecommendationEngine:
    """Portfolio rebalancing recommendation service."""

    def generate(
        self,
        portfolio: Portfolio,
        risk_report: RiskReport,
    ) -> list[RebalancingRecommendation]:
        """
        Generate portfolio rebalancing recommendations.

        Parameters
        ----------
        portfolio : Portfolio

        risk_report : RiskReport

        Returns
        -------
        list[RebalancingRecommendation]
        """

        if portfolio.is_empty:
            return []

        recommendations: list[
            RebalancingRecommendation
        ] = []

        largest_weight = max(
            position.weight
            for position in portfolio.positions
        )

        for position in portfolio.positions:

            action = self._determine_action(
                position.weight,
                largest_weight,
                risk_report,
            )

            recommendations.append(
                RebalancingRecommendation(
                    ticker=position.ticker,
                    action=action,
                    current_weight=position.weight,
                    target_weight=position.weight,
                    weight_difference=0.0,
                    reason=self._build_reason(
                        action,
                    ),
                )
            )

        return recommendations

    def _determine_action(
        self,
        current_weight: float,
        largest_weight: float,
        risk_report: RiskReport,
    ) -> RebalancingAction:
        """
        Determine portfolio action.
        """

        if (
            current_weight == largest_weight
            and risk_report.largest_weight > 60
        ):
            return RebalancingAction.SELL

        if (
            risk_report.cash_ratio > 60
            and current_weight < 20
        ):
            return RebalancingAction.BUY

        return RebalancingAction.HOLD

    @staticmethod
    def _build_reason(
        action: RebalancingAction,
    ) -> str:
        """
        Build recommendation reason.
        """

        if action == RebalancingAction.SELL:
            return (
                "Reduce concentration in the largest position."
            )

        if action == RebalancingAction.BUY:
            return (
                "Utilize excess cash to improve allocation."
            )

        return (
            "Current allocation is appropriate."
        )