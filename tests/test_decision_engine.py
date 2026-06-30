"""
Test DecisionEngine

Stock-CIO
"""

from src.core.decision_engine import DecisionEngine
from src.models.score import Score


def create_score(total: float) -> Score:

    score = Score()

    score.total = total

    return score


def test_strong_buy():

    engine = DecisionEngine()

    decision = engine.make_decision(create_score(95))

    assert decision.market_status == "VERY BULLISH"
    assert decision.action == "STRONG BUY"
    assert decision.cash_ratio == 5
    assert decision.stock_ratio == 95


def test_buy():

    engine = DecisionEngine()

    decision = engine.make_decision(create_score(85))

    assert decision.market_status == "BULLISH"
    assert decision.action == "BUY"


def test_accumulate():

    engine = DecisionEngine()

    decision = engine.make_decision(create_score(75))

    assert decision.market_status == "NEUTRAL"
    assert decision.action == "ACCUMULATE"


def test_hold():

    engine = DecisionEngine()

    decision = engine.make_decision(create_score(65))

    assert decision.market_status == "NEUTRAL"
    assert decision.action == "HOLD"


def test_reduce():

    engine = DecisionEngine()

    decision = engine.make_decision(create_score(45))

    assert decision.market_status == "BEARISH"
    assert decision.action == "REDUCE"


def test_defense():

    engine = DecisionEngine()

    decision = engine.make_decision(create_score(20))

    assert decision.market_status == "VERY BEARISH"
    assert decision.action == "DEFENSE"


def test_ratio_sum():

    engine = DecisionEngine()

    for total in (95, 85, 75, 65, 45, 20):

        decision = engine.make_decision(create_score(total))

        assert (
            decision.cash_ratio
            + decision.stock_ratio
        ) == 100


def test_summary_created():

    engine = DecisionEngine()

    decision = engine.make_decision(create_score(95))

    assert decision.summary != ""
    assert "Overall Score" in decision.summary