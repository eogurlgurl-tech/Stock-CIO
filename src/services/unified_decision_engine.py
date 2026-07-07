"""
Unified Decision Engine

Stock-CIO
"""

from src.constants.decision_type import DecisionType
from src.models.cio_decision import CIODecision
from src.models.decision import Decision
from src.models.unified_decision import UnifiedDecision


class UnifiedDecisionEngine:
    """Combine market and portfolio decisions conservatively."""

    RISK_REDUCTION_ACTIONS = {
        "DEFENSE",
        "REDUCE",
    }

    ACCUMULATION_ACTIONS = {
        "STRONG BUY",
        "BUY",
        "ACCUMULATE",
    }

    def generate(
        self,
        market_decision: CIODecision,
        portfolio_decision: Decision,
    ) -> UnifiedDecision:
        """Generate one final action and reason."""

        market_action = market_decision.action
        portfolio_action = portfolio_decision.decision.name

        if market_action in self.RISK_REDUCTION_ACTIONS:
            final_action = "REDUCE_RISK"
            reason = (
                "시장 위험 축소를 신규 매수보다 우선합니다."
            )
        elif portfolio_decision.decision == DecisionType.SELL:
            final_action = "REBALANCE"
            reason = (
                "전량 매도가 아니라 집중 종목을 목표 비중까지 "
                "조정합니다."
            )
        elif (
            portfolio_decision.decision == DecisionType.BUY
            and market_action in self.ACCUMULATION_ACTIONS
        ):
            final_action = "ACCUMULATE"
            reason = (
                "시장과 포트폴리오 신호가 모두 분할매수를 "
                "지지합니다."
            )
        else:
            final_action = "HOLD"
            reason = (
                "즉시 변경이 필요한 일치 신호가 없습니다."
            )

        return UnifiedDecision(
            market_action=market_action,
            portfolio_action=portfolio_action,
            final_action=final_action,
            reason=reason,
        )
