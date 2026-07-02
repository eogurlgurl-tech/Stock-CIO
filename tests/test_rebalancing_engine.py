"""
Unit Tests for Rebalancing Engine

Feature : FEATURE-018
Module  : Rebalancing Engine
"""

from src.constants.rebalance_action import RebalanceAction
from src.models.portfolio import Portfolio
from src.models.position import Position
from src.services.rebalancing_engine import RebalancingEngine


def test_hold_action():
    """현재와 목표가 동일"""

    current = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                weight=50.0,
            )
        ]
    )

    target = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                weight=50.0,
            )
        ]
    )

    engine = RebalancingEngine()

    plan = engine.create_plan(
        current=current,
        target=target,
    )

    assert len(plan.items) == 1
    assert plan.items[0].action == RebalanceAction.HOLD


def test_buy_action():
    """현재보다 목표가 큼"""

    current = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                weight=40.0,
            )
        ]
    )

    target = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                weight=60.0,
            )
        ]
    )

    engine = RebalancingEngine()

    plan = engine.create_plan(
        current=current,
        target=target,
    )

    assert plan.items[0].action == RebalanceAction.BUY


def test_sell_action():
    """현재보다 목표가 작음"""

    current = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                weight=80.0,
            )
        ]
    )

    target = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                weight=20.0,
            )
        ]
    )

    engine = RebalancingEngine()

    plan = engine.create_plan(
        current=current,
        target=target,
    )

    assert plan.items[0].action == RebalanceAction.SELL


def test_current_only_position():
    """현재만 존재 → SELL"""

    current = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                weight=100.0,
            )
        ]
    )

    target = Portfolio()

    engine = RebalancingEngine()

    plan = engine.create_plan(
        current=current,
        target=target,
    )

    assert len(plan.items) == 1
    assert plan.items[0].action == RebalanceAction.SELL
    assert plan.items[0].target_weight == 0.0


def test_target_only_position():
    """목표만 존재 → BUY"""

    current = Portfolio()

    target = Portfolio(
        positions=[
            Position(
                ticker="AAA",
                weight=100.0,
            )
        ]
    )

    engine = RebalancingEngine()

    plan = engine.create_plan(
        current=current,
        target=target,
    )

    assert len(plan.items) == 1
    assert plan.items[0].action == RebalanceAction.BUY
    assert plan.items[0].current_weight == 0.0
    assert plan.items[0].target_weight == 100.0