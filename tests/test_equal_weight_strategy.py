"""
Unit Tests for Equal Weight Strategy

Feature : FEATURE-018
Module  : Equal Weight Strategy
"""

from src.models.portfolio import Portfolio
from src.models.position import Position
from src.strategies.equal_weight_strategy import (
    EqualWeightStrategy,
)


def test_empty_portfolio():
    """빈 Portfolio"""

    portfolio = Portfolio()

    strategy = EqualWeightStrategy()

    result = strategy.allocate(portfolio)

    assert result.positions == []


def test_single_position():
    """단일 종목"""

    portfolio = Portfolio(
        positions=[
            Position(
                ticker="005930",
                quantity=10,
                current_price=75000,
            )
        ]
    )

    strategy = EqualWeightStrategy()

    strategy.allocate(portfolio)

    assert portfolio.positions[0].weight == 100.0


def test_two_positions():
    """2개 종목"""

    portfolio = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                quantity=10,
                current_price=100,
            ),
            Position(
                ticker="BBB",
                quantity=20,
                current_price=100,
            ),
        ]
    )

    strategy = EqualWeightStrategy()

    strategy.allocate(portfolio)

    assert portfolio.positions[0].weight == 50.0
    assert portfolio.positions[1].weight == 50.0


def test_three_positions():
    """3개 종목"""

    portfolio = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                quantity=10,
                current_price=100,
            ),
            Position(
                ticker="BBB",
                quantity=20,
                current_price=100,
            ),
            Position(
                ticker="CCC",
                quantity=30,
                current_price=100,
            ),
        ]
    )

    strategy = EqualWeightStrategy()

    strategy.allocate(portfolio)

    expected = 100.0 / 3

    for position in portfolio.positions:
        assert position.weight == expected


def test_total_weight():
    """총 비중은 100%"""

    portfolio = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                quantity=1,
                current_price=100,
            ),
            Position(
                ticker="BBB",
                quantity=1,
                current_price=100,
            ),
            Position(
                ticker="CCC",
                quantity=1,
                current_price=100,
            ),
            Position(
                ticker="DDD",
                quantity=1,
                current_price=100,
            ),
        ]
    )

    strategy = EqualWeightStrategy()

    strategy.allocate(portfolio)

    total = sum(
        position.weight
        for position in portfolio.positions
    )

    assert total == 100.0