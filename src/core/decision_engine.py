"""
Decision Engine

Stock-CIO
"""

from src.models.cio_decision import CIODecision
from src.models.score import Score


class DecisionEngine:
    """Score를 CIO 투자 의사결정으로 변환"""

    def make_decision(self, score: Score) -> CIODecision:

        decision = CIODecision()

        total = score.total

        # ==========================================================
        # Market Status / Action / Portfolio Allocation
        # ==========================================================

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

        # ==========================================================
        # Risk Analysis
        # ==========================================================

        if score.risk >= 70:
            decision.risks.append("High Market Risk")

        if score.risk >= 85:
            decision.risks.append("Capital Preservation Recommended")

        if score.macro < 50:
            decision.risks.append("Weak Macro Environment")

        if score.market < 50:
            decision.risks.append("Weak Market Momentum")

        if total < 60:
            decision.risks.append("Defensive Position Recommended")

        if not decision.risks:
            decision.risks.append("No Significant Risk")

        # ==========================================================
        # Recommended Sectors
        # (Temporary - FEATURE-012에서 자동화 예정)
        # ==========================================================

        if total >= 80:

            decision.top_sectors = [
                "AI",
                "Semiconductor",
                "Power Infrastructure",
                "Defense",
            ]

        elif total >= 60:

            decision.top_sectors = [
                "Semiconductor",
                "IT",
                "Healthcare",
                "Internet",
            ]

        else:

            decision.top_sectors = [
                "Utilities",
                "Dividend",
                "Consumer Staples",
                "Cash Equivalent",
            ]

        # ==========================================================
        # Watch List
        # (Temporary - FEATURE-012에서 Screener 연동 예정)
        # ==========================================================

        if total >= 80:

            decision.watch_list = [
                "Samsung Electronics",
                "SK Hynix",
                "ISC",
                "Leeno Industrial",
            ]

        elif total >= 60:

            decision.watch_list = [
                "Samsung Electronics",
                "LG Energy Solution",
                "NAVER",
                "Hyundai Motor",
            ]

        else:

            decision.watch_list = [
                "KODEX 200",
                "TIGER US S&P500",
            ]

        # ==========================================================
        # Summary
        # ==========================================================

        summary = []

        summary.append(
            f"Overall Score : {total:.2f}"
        )

        summary.append(
            f"Market Status : {decision.market_status}"
        )

        summary.append(
            f"Recommended Action : {decision.action}"
        )

        summary.append(
            f"Portfolio Allocation : "
            f"Stock {decision.stock_ratio}% / "
            f"Cash {decision.cash_ratio}%"
        )

        if decision.risks[0] == "No Significant Risk":
            summary.append("Market risk remains manageable.")
        else:
            summary.append(
                f"Primary Risk : {decision.risks[0]}"
            )

        decision.summary = "\n".join(summary)

        return decision