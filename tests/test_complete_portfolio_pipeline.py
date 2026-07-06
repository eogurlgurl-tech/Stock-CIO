"""
Integration Tests for the Complete Portfolio Pipeline

Feature : FEATURE-026
Module  : Portfolio Pipeline
"""

from src.constants.decision_type import DecisionType
from src.constants.rebalancing_action import RebalancingAction
from src.core.cio_engine import CIOEngine
from src.models.portfolio import Portfolio
from src.models.position import Position
from src.strategies.equal_weight_strategy import EqualWeightStrategy


class CompletePipelinePortfolioLoader:
    """Return a predefined portfolio for integration testing."""

    def __init__(self, portfolio: Portfolio) -> None:
        self._portfolio = portfolio

    def load(self) -> Portfolio:
        """Return the predefined portfolio."""

        return self._portfolio


def test_complete_portfolio_pipeline():
    """All portfolio workflow results are stored in context."""

    portfolio = Portfolio(
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
    engine.portfolio_loader = CompletePipelinePortfolioLoader(
        portfolio
    )
    engine.target_portfolio_builder.set_strategy(
        EqualWeightStrategy()
    )

    engine.run_portfolio_pipeline()

    context = engine.context["portfolio"]
    recommendations = context[
        "rebalancing_recommendations"
    ]

    assert context["analysis"] is not None
    assert context["recommendation"] is not None
    assert len(context["rebalancing"].items) == 2
    assert len(recommendations) == 2
    assert recommendations[0].action == RebalancingAction.SELL
    assert recommendations[1].action == RebalancingAction.BUY
    assert context["decision"].decision == DecisionType.SELL


def test_complete_empty_portfolio_pipeline():
    """An empty portfolio still completes the workflow."""

    engine = CIOEngine()
    engine.portfolio_loader = CompletePipelinePortfolioLoader(
        Portfolio()
    )

    engine.run_portfolio_pipeline()

    context = engine.context["portfolio"]

    assert context["analysis"].position_count == 0
    assert context["rebalancing"].items == []
    assert context["rebalancing_recommendations"] == []
    assert context["decision"].decision == DecisionType.HOLD
