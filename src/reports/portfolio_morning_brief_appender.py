"""
Portfolio Morning Brief Appender

Stock-CIO
"""

from pathlib import Path

from src.models.decision import Decision
from src.models.portfolio import Portfolio
from src.models.rebalance_plan import RebalancePlan
from src.models.risk_report import RiskReport


class PortfolioMorningBriefAppender:
    """Append portfolio workflow results to a Morning Brief."""

    def append(
        self,
        report_path: Path,
        portfolio: Portfolio,
        risk_report: RiskReport,
        decision: Decision,
        rebalancing_plan: RebalancePlan,
    ) -> Path:
        """Append a portfolio section and return the report path."""

        section = f"""

---

# Portfolio

| Item | Status |
|------|--------|
| Positions | {len(portfolio.positions)} |
| Total Asset | {portfolio.total_asset:.2f} |
| Cash Ratio | {portfolio.cash_ratio:.2f}% |
| Portfolio Score | {risk_report.portfolio_score:.2f} |
| Risk Level | {risk_report.risk_level.value} |
| Decision | {decision.decision.name} |
| Rebalance Count | {rebalancing_plan.rebalance_count} |
"""

        with report_path.open(
            "a",
            encoding="utf-8",
        ) as report_file:
            report_file.write(section)

        return report_path
