"""
Unit tests for Decision model.
"""

from src.constants.decision_type import DecisionType
from src.models.decision import Decision


class TestDecision:

    def test_create(self):
        decision = Decision(
            decision=DecisionType.BUY,
            confidence=0.85,
            summary="Portfolio is healthy.",
            reason="Risk level is acceptable.",
        )

        assert decision.decision == DecisionType.BUY
        assert decision.confidence == 0.85
        assert decision.summary == "Portfolio is healthy."
        assert decision.reason == "Risk level is acceptable."