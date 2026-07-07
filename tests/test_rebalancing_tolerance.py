"""
Unit Tests for Rebalancing Tolerance

Module : Rebalancing Engine
"""

import pytest

from src.constants.rebalance_action import RebalanceAction
from src.models.portfolio import Portfolio
from src.models.position import Position
from src.services.rebalancing_engine import RebalancingEngine


def test_difference_below_tolerance_is_hold():
    """Small weight differences do not trigger trades."""

    current = Portfolio(
        positions=[Position(ticker="A", weight=30.0)]
    )
    target = Portfolio(
        positions=[Position(ticker="A", weight=30.5)]
    )

    plan = RebalancingEngine(tolerance=1.0).create_plan(
        current,
        target,
    )

    assert plan.items[0].action == RebalanceAction.HOLD


def test_negative_tolerance_is_rejected():
    """Tolerance cannot be negative."""

    with pytest.raises(ValueError, match="tolerance"):
        RebalancingEngine(tolerance=-1.0)
