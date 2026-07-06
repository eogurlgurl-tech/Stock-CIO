"""
Unit Tests for Portfolio Outputs

Feature : FEATURE-026
Module  : Portfolio Outputs
"""

from src.constants.decision_type import DecisionType
from src.constants.rebalance_action import RebalanceAction
from src.constants.risk_level import RiskLevel
from src.dashboard.portfolio_dashboard_renderer import (
    PortfolioDashboardRenderer,
)
from src.models.decision import Decision
from src.models.portfolio import Portfolio
from src.models.position import Position
from src.models.rebalance_item import RebalanceItem
from src.models.rebalance_plan import RebalancePlan
from src.models.risk_report import RiskReport
from src.reports.portfolio_morning_brief_appender import (
    PortfolioMorningBriefAppender,
)


def _portfolio() -> Portfolio:
    return Portfolio(
        cash=100.0,
        positions=[
            Position(
                ticker="AAA",
                quantity=1,
                current_price=900.0,
            )
        ],
    )


def _risk_report() -> RiskReport:
    return RiskReport(
        portfolio_score=55.0,
        concentration_score=30.0,
        diversification_score=30.0,
        cash_score=80.0,
        largest_weight=100.0,
        position_count=1,
        cash_ratio=10.0,
        risk_level=RiskLevel.HIGH,
    )


def _decision() -> Decision:
    return Decision(
        decision=DecisionType.SELL,
        confidence=0.55,
        summary="Reduce risk.",
        reason="Concentration is high.",
    )


def _plan() -> RebalancePlan:
    return RebalancePlan(
        items=[
            RebalanceItem(
                ticker="AAA",
                current_weight=100.0,
                target_weight=50.0,
                action=RebalanceAction.SELL,
            )
        ]
    )


def test_portfolio_dashboard_renderer():
    """Portfolio results are rendered for the dashboard."""

    output = PortfolioDashboardRenderer().render(
        _portfolio(),
        _risk_report(),
        _decision(),
        _plan(),
    )

    assert "PORTFOLIO" in output
    assert "55.00" in output
    assert "HIGH" in output
    assert "SELL" in output
    assert "Rebalance Count : 1" in output


def test_portfolio_morning_brief_appender(tmp_path):
    """Portfolio results are appended to a Morning Brief."""

    report_path = tmp_path / "brief.md"
    report_path.write_text(
        "# Morning Brief\n",
        encoding="utf-8",
    )

    result = PortfolioMorningBriefAppender().append(
        report_path,
        _portfolio(),
        _risk_report(),
        _decision(),
        _plan(),
    )
    content = report_path.read_text(encoding="utf-8")

    assert result == report_path
    assert "# Morning Brief" in content
    assert "# Portfolio" in content
    assert "| Portfolio Score | 55.00 |" in content
    assert "| Decision | SELL |" in content
