"""
Unit Tests for Portfolio Allocation Output

Module : Portfolio Dashboard Renderer
"""

from src.constants.decision_type import DecisionType
from src.constants.rebalance_action import RebalanceAction
from src.constants.risk_level import RiskLevel
from src.dashboard.portfolio_dashboard_renderer import (
    PortfolioDashboardRenderer,
)
from src.models.decision import Decision
from src.models.portfolio import Portfolio
from src.models.rebalance_item import RebalanceItem
from src.models.rebalance_plan import RebalancePlan
from src.models.risk_report import RiskReport
from src.models.unified_decision import UnifiedDecision


def test_allocation_plan_and_final_decision_are_rendered():
    """Current, target, difference and final action are visible."""

    output = PortfolioDashboardRenderer().render(
        Portfolio(),
        RiskReport(
            portfolio_score=80.0,
            concentration_score=80.0,
            diversification_score=80.0,
            cash_score=80.0,
            largest_weight=40.0,
            position_count=1,
            cash_ratio=20.0,
            risk_level=RiskLevel.LOW,
        ),
        Decision(
            decision=DecisionType.SELL,
            confidence=0.8,
            summary="Summary",
            reason="Reason",
        ),
        RebalancePlan(
            items=[
                RebalanceItem(
                    ticker="AAA",
                    current_weight=50.0,
                    target_weight=30.0,
                    action=RebalanceAction.SELL,
                )
            ]
        ),
        UnifiedDecision(
            market_action="ACCUMULATE",
            portfolio_action="SELL",
            final_action="REBALANCE",
            reason="집중 비중을 조정합니다.",
        ),
    )

    assert "Final Action    : REBALANCE" in output
    assert "AAA" in output
    assert "50.00%" in output
    assert "30.00%" in output
    assert "-20.00%p" in output
