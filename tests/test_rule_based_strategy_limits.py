"""
Unit Tests for Rule Based Strategy Limits

Module : Rule Based Strategy
"""

from src.models.portfolio import Portfolio
from src.models.position import Position
from src.strategies.rule_based_strategy import RuleBasedStrategy


def test_max_weight_is_preserved_after_redistribution():
    """Repeated redistribution cannot recreate an overweight position."""

    portfolio = Portfolio(
        positions=[
            Position(ticker="A", quantity=50, current_price=100),
            Position(ticker="B", quantity=30, current_price=100),
            Position(ticker="C", quantity=15, current_price=100),
            Position(ticker="D", quantity=5, current_price=100),
        ]
    )

    target = RuleBasedStrategy().allocate(portfolio)

    assert all(
        position.weight <= RuleBasedStrategy.MAX_WEIGHT
        for position in target.positions
    )
    assert sum(
        position.weight
        for position in target.positions
    ) == 100.0


def test_infeasible_limit_uses_equal_weight():
    """A three-position portfolio uses mathematically feasible weights."""

    portfolio = Portfolio(
        positions=[
            Position(ticker="A", quantity=8, current_price=100),
            Position(ticker="B", quantity=1, current_price=100),
            Position(ticker="C", quantity=1, current_price=100),
        ]
    )

    target = RuleBasedStrategy().allocate(portfolio)

    assert [
        position.weight
        for position in target.positions
    ] == [33.34, 33.33, 33.33]
