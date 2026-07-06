"""
Unit Tests for Rebalancing Recommendations from a Plan

Feature : FEATURE-026
Module  : Rebalancing Recommendation Engine
"""

from src.constants.rebalance_action import RebalanceAction
from src.constants.rebalancing_action import RebalancingAction
from src.models.rebalance_item import RebalanceItem
from src.models.rebalance_plan import RebalancePlan
from src.services.rebalancing_recommendation_engine import (
    RebalancingRecommendationEngine,
)


def test_empty_plan_returns_empty_recommendations():
    """An empty plan creates no recommendations."""

    recommendations = (
        RebalancingRecommendationEngine()
        .generate_from_plan(RebalancePlan())
    )

    assert recommendations == []


def test_plan_item_is_converted_to_recommendation():
    """Plan values are preserved in the recommendation."""

    plan = RebalancePlan(
        items=[
            RebalanceItem(
                ticker="AAA",
                current_weight=75.0,
                target_weight=50.0,
                action=RebalanceAction.SELL,
            )
        ]
    )

    recommendation = (
        RebalancingRecommendationEngine()
        .generate_from_plan(plan)[0]
    )

    assert recommendation.ticker == "AAA"
    assert recommendation.action == RebalancingAction.SELL
    assert recommendation.current_weight == 75.0
    assert recommendation.target_weight == 50.0
    assert recommendation.weight_difference == -25.0
    assert "Reduce concentration" in recommendation.reason


def test_buy_plan_item_is_converted():
    """A BUY plan item creates a BUY recommendation."""

    plan = RebalancePlan(
        items=[
            RebalanceItem(
                ticker="BBB",
                current_weight=25.0,
                target_weight=50.0,
                action=RebalanceAction.BUY,
            )
        ]
    )

    recommendation = (
        RebalancingRecommendationEngine()
        .generate_from_plan(plan)[0]
    )

    assert recommendation.action == RebalancingAction.BUY
    assert recommendation.weight_difference == 25.0
    assert "Utilize excess cash" in recommendation.reason


def test_hold_plan_item_is_converted():
    """A HOLD plan item creates a HOLD recommendation."""

    plan = RebalancePlan(
        items=[
            RebalanceItem(
                ticker="CCC",
                current_weight=50.0,
                target_weight=50.0,
                action=RebalanceAction.HOLD,
            )
        ]
    )

    recommendation = (
        RebalancingRecommendationEngine()
        .generate_from_plan(plan)[0]
    )

    assert recommendation.action == RebalancingAction.HOLD
    assert recommendation.weight_difference == 0.0
    assert (
        recommendation.reason
        == "Current allocation is appropriate."
    )
