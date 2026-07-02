"""
Unit Tests for Portfolio Optimizer

Feature : FEATURE-018
Module  : Portfolio Optimizer
"""

from src.core.portfolio_optimizer import PortfolioOptimizer
from src.models.portfolio import Portfolio
from src.models.position import Position


def test_empty_portfolio():
    """빈 Portfolio"""

    portfolio = Portfolio()

    optimizer = PortfolioOptimizer()

    optimizer.update_weights(portfolio)

    assert portfolio.positions == []


def test_single_position_weight():
    """단일 종목"""

    portfolio = Portfolio(
        positions=[
            Position(
                ticker="005930",
                name="Samsung",
                quantity=10,
                average_price=70000,
                current_price=75000,
            )
        ]
    )

    optimizer = PortfolioOptimizer()

    optimizer.update_weights(portfolio)

    assert portfolio.positions[0].weight == 100.0


def test_two_position_weight():
    """2개 종목"""

    portfolio = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                quantity=75,
                current_price=100,
            ),
            Position(
                ticker="BBB",
                quantity=25,
                current_price=100,
            ),
        ]
    )

    optimizer = PortfolioOptimizer()

    optimizer.update_weights(portfolio)

    assert portfolio.positions[0].weight == 75.0
    assert portfolio.positions[1].weight == 25.0


def test_three_position_weight():
    """3개 종목"""

    portfolio = Portfolio(
        positions=[
            Position(
                ticker="A",
                quantity=50,
                current_price=100,
            ),
            Position(
                ticker="B",
                quantity=30,
                current_price=100,
            ),
            Position(
                ticker="C",
                quantity=20,
                current_price=100,
            ),
        ]
    )

    optimizer = PortfolioOptimizer()

    optimizer.update_weights(portfolio)

    assert portfolio.positions[0].weight == 50.0
    assert portfolio.positions[1].weight == 30.0
    assert portfolio.positions[2].weight == 20.0


def test_zero_asset():
    """평가금액 0"""

    portfolio = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                quantity=0,
                current_price=0,
            )
        ]
    )

    optimizer = PortfolioOptimizer()

    optimizer.update_weights(portfolio)

    assert portfolio.positions[0].weight == 0.0