"""
Unit tests for DecisionEngine.
"""

from src.constants.decision_type import DecisionType
from src.constants.rebalancing_action import (
    RebalancingAction,
)
from src.constants.risk_level import RiskLevel
from src.models.rebalancing_recommendation import (
    RebalancingRecommendation,
)
from src.models.recommendation import Recommendation
from src.services.decision_engine import DecisionEngine


class TestDecisionEngine:

    def setup_method(self):
        self.engine = DecisionEngine()

    def _recommendation(self) -> Recommendation:
        return Recommendation(
            overall_grade="A",
            portfolio_score=90.0,
            risk_level=RiskLevel.LOW,
            summary="Portfolio is healthy.",
        )

    def test_buy_decision(self):
        recommendations = [
            RebalancingRecommendation(
                ticker="AAPL",
                action=RebalancingAction.BUY,
                current_weight=10.0,
                target_weight=20.0,
                weight_difference=10.0,
                reason="Buy recommendation.",
            )
        ]

        decision = self.engine.generate(
            self._recommendation(),
            recommendations,
        )

        assert decision.decision == DecisionType.BUY

    def test_sell_decision(self):
        recommendations = [
            RebalancingRecommendation(
                ticker="AAPL",
                action=RebalancingAction.SELL,
                current_weight=70.0,
                target_weight=40.0,
                weight_difference=-30.0,
                reason="Sell recommendation.",
            )
        ]

        decision = self.engine.generate(
            self._recommendation(),
            recommendations,
        )

        assert decision.decision == DecisionType.SELL

    def test_hold_decision(self):
        recommendations = [
            RebalancingRecommendation(
                ticker="AAPL",
                action=RebalancingAction.HOLD,
                current_weight=40.0,
                target_weight=40.0,
                weight_difference=0.0,
                reason="Hold recommendation.",
            )
        ]

        decision = self.engine.generate(
            self._recommendation(),
            recommendations,
        )

        assert decision.decision == DecisionType.HOLD

    def test_mixed_recommendation(self):
        recommendations = [
            RebalancingRecommendation(
                ticker="AAA",
                action=RebalancingAction.BUY,
                current_weight=10.0,
                target_weight=20.0,
                weight_difference=10.0,
                reason="Buy.",
            ),
            RebalancingRecommendation(
                ticker="BBB",
                action=RebalancingAction.SELL,
                current_weight=70.0,
                target_weight=40.0,
                weight_difference=-30.0,
                reason="Sell.",
            ),
        ]

        decision = self.engine.generate(
            self._recommendation(),
            recommendations,
        )

        assert decision.decision == DecisionType.SELL

    def test_confidence(self):
        decision = self.engine.generate(
            self._recommendation(),
            [],
        )

        assert decision.confidence == 0.9

    def test_empty_recommendation(self):
        decision = self.engine.generate(
            self._recommendation(),
            [],
        )

        assert decision.decision == DecisionType.HOLD