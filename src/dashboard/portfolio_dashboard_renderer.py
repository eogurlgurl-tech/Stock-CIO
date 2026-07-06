"""
Portfolio Dashboard Renderer

Stock-CIO
"""

from src.models.decision import Decision
from src.models.portfolio import Portfolio
from src.models.rebalance_plan import RebalancePlan
from src.models.risk_report import RiskReport


class PortfolioDashboardRenderer:
    """Render portfolio workflow results for the dashboard."""

    def render(
        self,
        portfolio: Portfolio,
        risk_report: RiskReport,
        decision: Decision,
        rebalancing_plan: RebalancePlan,
    ) -> str:
        """Render the portfolio dashboard section."""

        return f"""
PORTFOLIO
------------------------------------------------------------
Positions       : {len(portfolio.positions)}
Total Asset     : {portfolio.total_asset:.2f}
Cash Ratio      : {portfolio.cash_ratio:.2f}%
Portfolio Score : {risk_report.portfolio_score:.2f}
Risk Level      : {risk_report.risk_level.value}
Decision        : {decision.decision.name}
Rebalance Count : {rebalancing_plan.rebalance_count}
""".strip()
