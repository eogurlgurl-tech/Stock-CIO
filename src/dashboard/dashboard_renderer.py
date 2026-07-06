"""
Dashboard Renderer

Stock-CIO
"""

from src.models.cio_decision import CIODecision
from src.models.market_snapshot import MarketSnapshot
from src.models.news import News
from src.models.score import Score


class DashboardRenderer:
    """Console Dashboard Renderer."""

    def render(
        self,
        market: MarketSnapshot,
        score: Score,
        decision: CIODecision,
        news_list: list[News],
    ) -> str:
        """Render dashboard."""

        watch_list = self._render_watch_list(
            decision.watch_list,
        )

        headlines = self._render_news(
            news_list,
        )

        return f"""
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

🎯 MARKET DECISION
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
""".strip()

    def _render_watch_list(
        self,
        watch_list: list[str],
    ) -> str:

        if not watch_list:
            return "• No Watch List"

        return "\n".join(
            f"• {item}"
            for item in watch_list
        )

    def _render_news(
        self,
        news_list: list[News],
    ) -> str:

        if not news_list:
            return "• No News"

        return "\n".join(
            f"• {news.title}"
            for news in news_list[:5]
        )