"""
Decision Engine

Generates the final investment decision by integrating
portfolio recommendations and rebalancing recommendations.

STOCK-CIO
"""

from __future__ import annotations

from src.constants.decision_type import DecisionType
from src.constants.rebalancing_action import RebalancingAction
from src.models.decision import Decision
from src.models.rebalancing_recommendation import (
    RebalancingRecommendation,
)
from src.models.recommendation import Recommendation


class DecisionEngine:
    """Final investment decision service."""

    def generate(
        self,
        recommendation: Recommendation,
        rebalancing_recommendations: list[
            RebalancingRecommendation
        ],
    ) -> Decision:
        """
        Generate the final investment decision.
        """

        decision = self._determine_decision(
            rebalancing_recommendations,
        )

        confidence = (
            recommendation.portfolio_score / 100.0
        )

        summary = recommendation.summary

        reason = self._build_reason(
            rebalancing_recommendations,
        )

        return Decision(
            decision=decision,
            confidence=confidence,
            summary=summary,
            reason=reason,
        )

    @staticmethod
    def _determine_decision(
        recommendations: list[
            RebalancingRecommendation
        ],
    ) -> DecisionType:
        """Determine the final decision."""

        if any(
            item.action == RebalancingAction.SELL
            for item in recommendations
        ):
            return DecisionType.SELL

        if any(
            item.action == RebalancingAction.BUY
            for item in recommendations
        ):
            return DecisionType.BUY

        return DecisionType.HOLD

    @staticmethod
    def _build_reason(
        recommendations: list[
            RebalancingRecommendation
        ],
    ) -> str:
        """Build the decision reason."""

        reasons: list[str] = []

        for item in recommendations:
            if item.reason not in reasons:
                reasons.append(item.reason)

        return " ".join(reasons)