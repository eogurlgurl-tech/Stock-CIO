"""
Morning Brief Tests

Stock-CIO
"""

from src.reports.morning_brief import MorningBrief
from src.models.score import Score
from src.models.cio_decision import CIODecision


def test_generate_cio_comment_buy():
    """BUY Comment"""

    brief = MorningBrief()

    score = Score(
        macro=90,
        total=85,
    )

    decision = CIODecision(
        action="BUY",
        cash_ratio=30,
    )

    comment = brief._generate_cio_comment(
        score,
        decision,
    )

    assert "Global macro environment remains favorable." in comment
    assert "Overall investment score is strong." in comment
    assert "Consider increasing equity exposure." in comment
    assert "30%" in comment


def test_generate_cio_comment_sell():
    """SELL Comment"""

    brief = MorningBrief()

    score = Score(
        macro=40,
        total=45,
    )

    decision = CIODecision(
        action="SELL",
        cash_ratio=80,
    )

    comment = brief._generate_cio_comment(
        score,
        decision,
    )

    assert "Macro environment remains cautious." in comment
    assert "Overall investment score remains weak." in comment
    assert "Maintain defensive allocation." in comment
    assert "80%" in comment


def test_generate_cio_comment_hold():
    """HOLD Comment"""

    brief = MorningBrief()

    score = Score(
        macro=70,
        total=70,
    )

    decision = CIODecision(
        action="HOLD",
        cash_ratio=50,
    )

    comment = brief._generate_cio_comment(
        score,
        decision,
    )

    assert "Macro environment remains stable." in comment
    assert "Overall investment score is neutral." in comment
    assert "Maintain current allocation." in comment
    assert "50%" in comment