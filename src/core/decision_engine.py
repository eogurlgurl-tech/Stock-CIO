"""
Decision Engine

Stock-CIO
"""

from src.analyzers.stock_screener import StockScreener
from src.models.cio_decision import CIODecision
from src.models.score import Score


class DecisionEngine:
    """Convert market score into market decision."""

    def __init__(self) -> None:

        self.screener = StockScreener()

    def make_decision(self, score: Score) -> CIODecision:
        """Create market decision from integrated score."""

        decision = CIODecision()

        screen = self.screener.screen(score)

        self._evaluate_market(score, decision)
        self._evaluate_risk(score, decision)

        decision.top_sectors = screen.top_sectors
        decision.watch_list = screen.watch_list

        decision.summary = self._build_summary(score, decision)

        return decision

    def _evaluate_market(
        self,
        score: Score,
        decision: CIODecision,
    ) -> None:

        total = score.total

        if total >= 90:

            decision.market_status = "VERY BULLISH"
            decision.action = "STRONG BUY"
            decision.cash_ratio = 5
            decision.stock_ratio = 95

        elif total >= 80:

            decision.market_status = "BULLISH"
            decision.action = "BUY"
            decision.cash_ratio = 20
            decision.stock_ratio = 80

        elif total >= 70:

            decision.market_status = "NEUTRAL"
            decision.action = "ACCUMULATE"
            decision.cash_ratio = 30
            decision.stock_ratio = 70

        elif total >= 60:

            decision.market_status = "NEUTRAL"
            decision.action = "HOLD"
            decision.cash_ratio = 40
            decision.stock_ratio = 60

        elif total >= 40:

            decision.market_status = "BEARISH"
            decision.action = "REDUCE"
            decision.cash_ratio = 60
            decision.stock_ratio = 40

        else:

            decision.market_status = "VERY BEARISH"
            decision.action = "DEFENSE"
            decision.cash_ratio = 80
            decision.stock_ratio = 20

    def _evaluate_risk(
        self,
        score: Score,
        decision: CIODecision,
    ) -> None:

        if score.risk >= 70:
            decision.risks.append("High Market Risk")

        if score.risk >= 85:
            decision.risks.append("Capital Preservation Recommended")

        if score.macro < 50:
            decision.risks.append("Weak Macro Environment")

        if score.market < 50:
            decision.risks.append("Weak Market Momentum")

        if score.total < 60:
            decision.risks.append("Defensive Position Recommended")

        if not decision.risks:
            decision.risks.append("No Significant Risk")

    def _build_summary(
        self,
        score: Score,
        decision: CIODecision,
    ) -> str:

        summary: list[str] = [
            f"Overall Score : {score.total:.2f}",
            f"Market Status : {decision.market_status}",
            f"Recommended Action : {decision.action}",
            (
                f"Portfolio Allocation : "
                f"Stock {decision.stock_ratio}% / "
                f"Cash {decision.cash_ratio}%"
            ),
        ]

        if decision.risks[0] == "No Significant Risk":
            summary.append("Market risk remains manageable.")
        else:
            summary.append(f"Primary Risk : {decision.risks[0]}")

        return "\n".join(summary)