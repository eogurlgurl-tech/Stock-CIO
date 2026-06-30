"""
Test ScoreEngine

Stock-CIO
"""

from src.analyzers.score_engine import ScoreEngine


def test_score_calculation():
    """Weighted score should be calculated correctly."""

    engine = ScoreEngine()

    score = engine.calculate(
        macro=100,
        market=100,
        sector=100,
        money_flow=100,
        news=100,
        portfolio=100,
        risk=100,
    )

    assert score.total == 100
    assert score.grade == "S"
    assert score.stars == "★★★★★"


def test_score_empty():
    """Empty score should be zero."""

    engine = ScoreEngine()

    score = engine.calculate()

    assert score.total == 0
    assert score.grade == "D"


def test_score_grade_a():
    """80 points should be grade A."""

    engine = ScoreEngine()

    score = engine.calculate(
        macro=80,
        market=80,
        sector=80,
        money_flow=80,
        news=80,
        portfolio=80,
        risk=80,
    )

    assert score.total == 80
    assert score.grade == "A"
    assert score.stars == "★★★★☆"


def test_score_grade_b():
    """70 points should be grade B."""

    engine = ScoreEngine()

    score = engine.calculate(
        macro=70,
        market=70,
        sector=70,
        money_flow=70,
        news=70,
        portfolio=70,
        risk=70,
    )

    assert score.total == 70
    assert score.grade == "B"


def test_score_grade_c():
    """60 points should be grade C."""

    engine = ScoreEngine()

    score = engine.calculate(
        macro=60,
        market=60,
        sector=60,
        money_flow=60,
        news=60,
        portfolio=60,
        risk=60,
    )

    assert score.total == 60
    assert score.grade == "C"


def test_score_is_score_model():
    """ScoreEngine should return Score model."""

    engine = ScoreEngine()

    score = engine.calculate()

    assert hasattr(score, "total")
    assert hasattr(score, "grade")
    assert hasattr(score, "stars")