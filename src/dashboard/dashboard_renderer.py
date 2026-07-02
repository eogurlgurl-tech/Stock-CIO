"""
Dashboard Renderer

Stock-CIO
"""

from src.models.market_snapshot import MarketSnapshot
from src.models.score import Score
from src.models.cio_decision import CIODecision
from src.models.news import News


class DashboardRenderer:
    """Console Dashboard Renderer"""

    def render(
        self,
        market: MarketSnapshot,
        score: Score,
        decision: CIODecision,
        news_list: list[News],
    ) -> str:
        """Dashboard 문자열 생성"""

        # -------------------------
        # Watch List
        # -------------------------

        if decision.watch_list:
            watch_list = "\n".join(
                f"• {item}"
                for item in decision.watch_list
            )
        else:
            watch_list = "• No Watch List"

        # -------------------------
        # News
        # -------------------------

        if news_list:
            headlines = "\n".join(
                f"• {news.title}"
                for news in news_list[:5]
            )
        else:
            headlines = "• No News"

        dashboard = f"""
============================================================
                    STOCK-CIO DASHBOARD
============================================================

📋 TODAY'S SUMMARY
------------------------------------------------------------
Market Status  : {decision.market_status}
Investment     : {decision.action}
Overall Grade  : {score.grade} {score.stars}
Cash Ratio     : {decision.cash_ratio}%
Stock Ratio    : {decision.stock_ratio}%

🌎 MARKET
------------------------------------------------------------
KOSPI          {market.kospi:.2f}
KOSDAQ         {market.kosdaq:.2f}
NASDAQ         {market.nasdaq:.2f}
S&P500         {market.sp500:.2f}
VIX            {market.vix:.2f}

📊 CIO SCORE
------------------------------------------------------------
TOTAL SCORE    {score.total:.2f}
GRADE          {score.grade}
RATING         {score.stars}

🎯 DECISION
------------------------------------------------------------
STATUS         {decision.market_status}
ACTION         {decision.action}
CASH           {decision.cash_ratio}%
STOCK          {decision.stock_ratio}%

👀 WATCH LIST
------------------------------------------------------------
{watch_list}

💬 CIO COMMENT
------------------------------------------------------------
• Market Status : {decision.market_status}
• Recommended Action : {decision.action}
• Recommended Cash Ratio : {decision.cash_ratio}%

📰 TOP NEWS
------------------------------------------------------------
{headlines}

============================================================
"""

        return dashboard.strip()