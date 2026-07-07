"""
Portfolio Morning Brief Appender

Stock-CIO
"""

from pathlib import Path

from src.models.decision import Decision
from src.models.portfolio import Portfolio
from src.models.rebalance_plan import RebalancePlan
from src.models.risk_report import RiskReport
from src.models.unified_decision import UnifiedDecision


class PortfolioMorningBriefAppender:
    """Append portfolio results to a Morning Brief."""

    def append(
        self,
        report_path: Path,
        portfolio: Portfolio,
        risk_report: RiskReport,
        decision: Decision,
        rebalancing_plan: RebalancePlan,
        unified_decision: UnifiedDecision | None = None,
    ) -> Path:
        """Append a Korean portfolio decision section."""

        final_action = (
            unified_decision.final_action
            if unified_decision is not None
            else "N/A"
        )
        reason = (
            unified_decision.reason
            if unified_decision is not None
            else "통합 판단 정보가 없습니다."
        )
        allocation_rows = self._allocation_rows(
            rebalancing_plan
        )

        section = f"""

---

# Portfolio / 포트폴리오

| 항목 | 결과 |
|------|------|
| Positions | {len(portfolio.positions)} |
| Total Asset | {portfolio.total_asset:,.0f}원 |
| Cash Ratio | {portfolio.cash_ratio:.2f}% |
| Portfolio Score | {risk_report.portfolio_score:.2f} |
| Risk Level | {risk_report.risk_level.value} |
| Decision | {decision.decision.name} |
| Final Decision | {final_action} |
| Reason | {reason} |
| Rebalance Count | {rebalancing_plan.rebalance_count}개 |
| 보유 종목 수 | {len(portfolio.positions)} |
| 총자산 | {portfolio.total_asset:,.0f}원 |
| 현금 비중 | {portfolio.cash_ratio:.2f}% |
| 포트폴리오 점수 | {risk_report.portfolio_score:.2f} |
| 위험 수준 | {risk_report.risk_level.value} |
| 포트폴리오 판단 | {decision.decision.name} |
| 최종 판단 | {final_action} |
| 판단 근거 | {reason} |
| 리밸런싱 대상 | {rebalancing_plan.rebalance_count}개 |

## 종목별 비중 계획

| 종목 | 현재 비중 | 목표 비중 | 차이 | 조치 |
|------|----------:|----------:|-----:|------|
{allocation_rows}
"""

        with report_path.open(
            "a",
            encoding="utf-8",
        ) as report_file:
            report_file.write(section)

        return report_path

    @staticmethod
    def _allocation_rows(
        plan: RebalancePlan,
    ) -> str:
        """Create allocation rows for the report."""

        if not plan.items:
            return "| - | 0.00% | 0.00% | 0.00%p | HOLD |"

        return "\n".join(
            (
                f"| {item.name or item.ticker} | "
                f"{item.current_weight:.2f}% | "
                f"{item.target_weight:.2f}% | "
                f"{item.difference:+.2f}%p | "
                f"{item.action.value} |"
            )
            for item in plan.items
        )
