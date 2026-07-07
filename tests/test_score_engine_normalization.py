"""
Unit Tests for Score Normalization

Module : Score Engine
"""

from src.analyzers.score_engine import ScoreEngine


def test_missing_scores_are_excluded_from_weight():
    """Unavailable score categories do not create penalties."""

    score = ScoreEngine().calculate(
        macro=50.0,
        market=30.0,
        news=50.0,
    )

    assert score.total == 42.0


def test_zero_score_is_available_score():
    """An explicit zero remains part of the calculation."""

    score = ScoreEngine().calculate(
        macro=0.0,
        market=100.0,
    )

    assert score.total == 50.0
