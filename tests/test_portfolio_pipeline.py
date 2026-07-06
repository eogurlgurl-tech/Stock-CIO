"""
Unit Tests for Portfolio Pipeline

Feature : FEATURE-026
Module  : Portfolio Pipeline
"""

from src.constants.rebalance_action import RebalanceAction
from src.core.cio_engine import CIOEngine
from src.models.portfolio import Portfolio
from src.models.position import Position
from src.strategies.equal_weight_strategy import EqualWeightStrategy


class StubPortfolioLoader:
    """Return a predefined current portfolio."""

    def __init__(self, portfolio: Portfolio) -> None:
        self._portfolio = portfolio

    def load(self) -> Portfolio:
        """Return the predefined portfolio."""

        return self._portfolio


def test_portfolio_pipeline_builds_target_and_rebalance_plan():
    """Pipeline creates current weights, target, and plan."""

    current = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                quantity=3,
                current_price=100.0,
            ),
            Position(
                ticker="BBB",
                quantity=1,
                current_price=100.0,
            ),
        ]
    )
    engine = CIOEngine()
    engine.portfolio_loader = StubPortfolioLoader(current)
    engine.target_portfolio_builder.set_strategy(
        EqualWeightStrategy()
    )

    engine.run_portfolio_pipeline()

    context = engine.context["portfolio"]
    target = context["target"]
    plan = context["rebalancing"]

    assert context["portfolio"] is current
    assert current.positions[0].weight == 75.0
    assert current.positions[1].weight == 25.0
    assert target is not current
    assert target.positions[0].weight == 50.0
    assert target.positions[1].weight == 50.0
    assert plan.items[0].action == RebalanceAction.SELL
    assert plan.items[1].action == RebalanceAction.BUY


def test_empty_portfolio_pipeline():
    """Empty portfolio creates an empty target and plan."""

    current = Portfolio()
    engine = CIOEngine()
    engine.portfolio_loader = StubPortfolioLoader(current)

    engine.run_portfolio_pipeline()

    context = engine.context["portfolio"]

    assert context["portfolio"] is current
    assert context["target"] is not current
    assert context["target"].positions == []
    assert context["rebalancing"].items == []
