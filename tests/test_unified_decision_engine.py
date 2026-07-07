"""
Unit Tests for Unified Decision Engine

Module : Unified Decision Engine
"""

from src.constants.decision_type import DecisionType
from src.models.cio_decision import CIODecision
from src.models.decision import Decision
from src.services.unified_decision_engine import UnifiedDecisionEngine


def _portfolio_decision(action: DecisionType) -> Decision:
    return Decision(
        decision=action,
        confidence=0.8,
        summary="Portfolio summary.",
        reason="Portfolio reason.",
    )


def test_market_risk_reduction_has_priority():
    """Defensive market conditions block new buying."""

    result = UnifiedDecisionEngine().generate(
        CIODecision(action="REDUCE"),
        _portfolio_decision(DecisionType.BUY),
    )

    assert result.final_action == "REDUCE_RISK"


def test_portfolio_sell_becomes_rebalance():
    """A portfolio SELL signal is presented as rebalancing."""

    result = UnifiedDecisionEngine().generate(
        CIODecision(action="ACCUMULATE"),
        _portfolio_decision(DecisionType.SELL),
    )

    assert result.final_action == "REBALANCE"


def test_aligned_buy_signals_accumulate():
    """Aligned market and portfolio signals support accumulation."""

    result = UnifiedDecisionEngine().generate(
        CIODecision(action="BUY"),
        _portfolio_decision(DecisionType.BUY),
    )

    assert result.final_action == "ACCUMULATE"


def test_unaligned_signals_hold():
    """No aligned action results in HOLD."""

    result = UnifiedDecisionEngine().generate(
        CIODecision(action="HOLD"),
        _portfolio_decision(DecisionType.BUY),
    )

    assert result.final_action == "HOLD"
