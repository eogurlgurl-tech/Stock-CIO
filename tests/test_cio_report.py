"""
Unit tests for CIOReport.

STOCK-CIO
"""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest

from src.constants.decision_type import DecisionType
from src.models.cio_report import CIOReport
from src.models.decision import Decision


def test_create_cio_report() -> None:
    """CIOReport should store all values correctly."""

    decision = Decision(
        decision=DecisionType.BUY,
        confidence=0.91,
        summary="Portfolio outlook is positive.",
        reason="Macro trend remains favorable.",
    )

    report = CIOReport(
        decision=decision,
        portfolio_summary="Portfolio is well diversified.",
        recommended_action="Increase equity exposure.",
        investment_comment="Gradual accumulation is recommended.",
    )

    assert report.decision is decision
    assert report.decision.decision == DecisionType.BUY
    assert report.decision.confidence == 0.91
    assert (
        report.portfolio_summary
        == "Portfolio is well diversified."
    )
    assert (
        report.recommended_action
        == "Increase equity exposure."
    )
    assert (
        report.investment_comment
        == "Gradual accumulation is recommended."
    )


def test_cio_report_is_immutable() -> None:
    """CIOReport should be immutable."""

    decision = Decision(
        decision=DecisionType.HOLD,
        confidence=0.50,
        summary="Neutral market.",
        reason="No significant signal detected.",
    )

    report = CIOReport(
        decision=decision,
        portfolio_summary="Balanced portfolio.",
        recommended_action="Maintain current allocation.",
        investment_comment="Continue monitoring.",
    )

    with pytest.raises(FrozenInstanceError):
        report.portfolio_summary = "Modified"