"""
Unit tests for CIOEngine.

STOCK-CIO
"""

from __future__ import annotations

from src.constants.decision_type import DecisionType
from src.models.decision import Decision
from src.services.cio_engine import CIOEngine


def test_generate_buy_report() -> None:
    """Generate BUY CIO report."""

    engine = CIOEngine()

    decision = Decision(
        decision=DecisionType.BUY,
        confidence=0.90,
        summary="Positive market outlook.",
        reason="Macro trend is improving.",
    )

    report = engine.generate(decision)

    assert report.decision == decision
    assert (
        report.recommended_action
        == "Increase equity exposure."
    )
    assert (
        report.investment_comment
        == "Current market conditions support "
        "gradual accumulation."
    )


def test_generate_sell_report() -> None:
    """Generate SELL CIO report."""

    engine = CIOEngine()

    decision = Decision(
        decision=DecisionType.SELL,
        confidence=0.80,
        summary="Risk is increasing.",
        reason="Market momentum weakened.",
    )

    report = engine.generate(decision)

    assert report.decision == decision
    assert (
        report.recommended_action
        == "Reduce equity exposure."
    )
    assert (
        report.investment_comment
        == "Risk factors have increased. "
        "Consider reducing exposure."
    )


def test_generate_hold_report() -> None:
    """Generate HOLD CIO report."""

    engine = CIOEngine()

    decision = Decision(
        decision=DecisionType.HOLD,
        confidence=0.60,
        summary="Neutral market.",
        reason="No significant signal.",
    )

    report = engine.generate(decision)

    assert report.decision == decision
    assert (
        report.recommended_action
        == "Maintain current allocation."
    )
    assert (
        report.investment_comment
        == "Current portfolio remains balanced. "
        "Continue monitoring market conditions."
    )


def test_portfolio_summary_is_generated() -> None:
    """Portfolio summary should always be generated."""

    engine = CIOEngine()

    decision = Decision(
        decision=DecisionType.HOLD,
        confidence=0.50,
        summary="Summary",
        reason="Reason",
    )

    report = engine.generate(decision)

    assert (
        report.portfolio_summary
        == "Portfolio allocation has been evaluated "
        "based on the latest analysis."
    )


def test_decision_is_preserved() -> None:
    """Decision object should be preserved."""

    engine = CIOEngine()

    decision = Decision(
        decision=DecisionType.BUY,
        confidence=0.95,
        summary="Strong outlook.",
        reason="Excellent market conditions.",
    )

    report = engine.generate(decision)

    assert report.decision is decision
    assert report.decision.confidence == 0.95
    assert report.decision.summary == "Strong outlook."
    assert (
        report.decision.reason
        == "Excellent market conditions."
    )