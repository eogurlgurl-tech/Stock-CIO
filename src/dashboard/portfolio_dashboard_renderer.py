"""
Portfolio Dashboard Renderer

Stock-CIO
"""

from src.models.decision import Decision
from src.models.portfolio import Portfolio
from src.models.rebalance_plan import RebalancePlan
from src.models.risk_report import RiskReport
from src.models.unified_decision import UnifiedDecision


class PortfolioDashboardRenderer:
    """Render portfolio workflow results for the dashboard."""

    def render(
        self,
        portfolio: Portfolio,
        risk_report: RiskReport,
        decision: Decision,
        rebalancing_plan: RebalancePlan,
        unified_decision: UnifiedDecision | None = None,
    ) -> str:
        """Render portfolio summary and allocation plan."""

        final_section = self._render_final_decision(
            unified_decision
        )
        allocation = self._render_allocation_plan(
            rebalancing_plan
        )

        return f"""
PORTFOLIO
------------------------------------------------------------
Positions       : {len(portfolio.positions)}
Total Asset     : {portfolio.total_asset:,.0f}
Cash Ratio      : {portfolio.cash_ratio:.2f}%
Portfolio Score : {risk_report.portfolio_score:.2f}
Risk Level      : {risk_report.risk_level.value}
Decision        : {decision.decision.name}
Rebalance Count : {rebalancing_plan.rebalance_count}

{final_section}

ALLOCATION PLAN
------------------------------------------------------------
{allocation}
""".strip()

    @staticmethod
    def _render_final_decision(
        decision: UnifiedDecision | None,
    ) -> str:
        """Render the unified final action."""

        if decision is None:
            return "FINAL DECISION\nNot available"

        return (
            "FINAL DECISION\n"
            "------------------------------------------------------------\n"
            f"Final Action    : {decision.final_action}\n"
            f"Reason          : {decision.reason}"
        )

    @staticmethod
    def _render_allocation_plan(
        plan: RebalancePlan,
    ) -> str:
        """Render current and target weights for each position."""

        if not plan.items:
            return "No portfolio positions available."

        header = (
            "Ticker       Name                 Current   Target    Difference   Action"
        )
        rows = [header]

        for item in plan.items:
            rows.append(
                f"{item.ticker:<12} "
                f"{item.name:<20} "
                f"{item.current_weight:>6.2f}%   "
                f"{item.target_weight:>6.2f}%   "
                f"{item.difference:>+8.2f}%p   "
                f"{item.action.value}"
            )

        return "\n".join(rows)
