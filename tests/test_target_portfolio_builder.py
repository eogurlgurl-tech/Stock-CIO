"""
Unit Tests for Target Portfolio Builder

Feature : FEATURE-026
Module  : Target Portfolio Builder
"""

from src.models.portfolio import Portfolio
from src.models.position import Position
from src.services.target_portfolio_builder import TargetPortfolioBuilder
from src.strategies.equal_weight_strategy import EqualWeightStrategy
from src.strategies.rule_based_strategy import RuleBasedStrategy


def test_default_strategy():
    """RuleBasedStrategy is used by default."""

    builder = TargetPortfolioBuilder()

    assert isinstance(builder.strategy, RuleBasedStrategy)


def test_build_returns_new_portfolio():
    """Build returns a new portfolio and new positions."""

    current = Portfolio(
        cash=1000.0,
        positions=[
            Position(
                ticker="AAA",
                quantity=10,
                current_price=100.0,
            )
        ],
    )

    target = TargetPortfolioBuilder().build(current)

    assert target is not current
    assert target.positions[0] is not current.positions[0]
    assert target.cash == current.cash


def test_build_does_not_change_current_portfolio():
    """Allocation does not change the current portfolio."""

    current = Portfolio(
        positions=[
            Position(ticker="AAA", weight=70.0),
            Position(ticker="BBB", weight=30.0),
        ]
    )
    builder = TargetPortfolioBuilder(
        strategy=EqualWeightStrategy()
    )

    target = builder.build(current)

    assert current.positions[0].weight == 70.0
    assert current.positions[1].weight == 30.0
    assert target.positions[0].weight == 50.0
    assert target.positions[1].weight == 50.0


def test_set_strategy():
    """Allocation strategy can be changed."""

    builder = TargetPortfolioBuilder()
    strategy = EqualWeightStrategy()

    builder.set_strategy(strategy)

    assert builder.strategy is strategy


def test_empty_portfolio():
    """An empty current portfolio creates an empty target portfolio."""

    current = Portfolio(cash=1000.0)

    target = TargetPortfolioBuilder().build(current)

    assert target is not current
    assert target.cash == 1000.0
    assert target.positions == []
