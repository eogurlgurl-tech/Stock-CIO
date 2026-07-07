"""
Morning Brief Report Generator

Stock-CIO
"""

from datetime import datetime
from pathlib import Path

from src.models.market_snapshot import MarketSnapshot
from src.models.cio_decision import CIODecision
from src.models.news import News
from src.models.score import Score


class MorningBrief:
    """Morning Brief Report Generator."""

    VERSION = "v1.0.0-rc"

    def _generate_global_summary(self, market: MarketSnapshot) -> str:

        nasdaq_status = "Bullish" if market.nasdaq >= 0 else "Bearish"
        sp500_status = "Positive" if market.sp500 >= 0 else "Negative"

        if market.vix < 20:
            vix_status = "Low Volatility"
        elif market.vix < 30:
            vix_status = "Moderate Volatility"
        else:
            vix_status = "High Volatility"

        if (
            market.nasdaq >= 0
            and market.sp500 >= 0
            and market.vix < 20
        ):
            overall = "Risk-On"
        elif (
            market.nasdaq < 0
            and market.sp500 < 0
            and market.vix >= 30
        ):
            overall = "Risk-Off"
        else:
            overall = "Neutral"

        return f"""| Item | Status |
|------|--------|
| NASDAQ | {nasdaq_status} |
| S&P500 | {sp500_status} |
| VIX | {vix_status} |
| Overall | {overall} |"""

    def _generate_korea_summary(self, market: MarketSnapshot) -> str:

        if market.kospi == 0 and market.kosdaq == 0:
            kospi = "N/A"
            kosdaq = "N/A"
            overall = "KRX Data Unavailable"
        else:
            kospi = f"{market.kospi:.2f}"
            kosdaq = f"{market.kosdaq:.2f}"
            overall = "Market Data Available"

        return f"""| Item | Status |
|------|--------|
| KOSPI | {kospi} |
| KOSDAQ | {kosdaq} |
| Overall | {overall} |"""

    def _generate_news_summary(
        self,
        news_list: list[News],
    ) -> str:

        news_count = len(news_list)

        overall = (
            "News Data Available"
            if news_count
            else "No News Available"
        )

        return f"""| Item | Status |
|------|--------|
| News Count | {news_count} |
| Overall | {overall} |"""

    def _generate_risk_summary(
        self,
        score: Score,
    ) -> str:

        if score.risk >= 80:
            overall = "High Risk"
            recommendation = "Reduce Stock Position"
        elif score.risk >= 50:
            overall = "Moderate Risk"
            recommendation = "Maintain Current Position"
        else:
            overall = "Low Risk"
            recommendation = "Normal Investment"

        return f"""| Item | Status |
|------|--------|
| Risk Score | {score.risk:.2f} |
| Overall | {overall} |
| Recommendation | {recommendation} |"""

    def _generate_watch_list(
        self,
        score: Score,
    ) -> str:

        if score.market >= 70:
            sectors = [
                ("AI", "Watch"),
                ("Semiconductor", "Watch"),
                ("Battery", "Neutral"),
            ]
        else:
            sectors = [
                ("Dividend ETF", "Watch"),
                ("Defense", "Watch"),
                ("Cash", "Increase"),
            ]

        rows = "\n".join(
            f"| {sector} | {status} |"
            for sector, status in sectors
        )

        return f"""| Sector | Status |
|--------|--------|
{rows}"""

    def _generate_cio_comment(
        self,
        score: Score,
        decision: CIODecision,
    ) -> str:

        comments: list[str] = []

        if score.macro >= 80:
            comments.append(
                "- Global macro environment remains favorable."
            )
        elif score.macro >= 60:
            comments.append(
                "- Macro environment remains stable."
            )
        else:
            comments.append(
                "- Macro environment remains cautious."
            )

        if score.total >= 80:
            comments.append(
                "- Overall investment score is strong."
            )
        elif score.total >= 60:
            comments.append(
                "- Overall investment score is neutral."
            )
        else:
            comments.append(
                "- Overall investment score remains weak."
            )

        action = decision.action.lower()

        if "buy" in action:
            comments.append(
                "- Consider increasing equity exposure."
            )
        elif (
            "reduce" in action
            or "defense" in action
            or "sell" in action
        ):
            comments.append(
                "- Maintain defensive allocation."
            )
        else:
            comments.append(
                "- Maintain current allocation."
            )

        comments.append(
            f"- Recommended cash ratio : {decision.cash_ratio}%."
        )

        return "\n".join(comments)

    def generate(
        self,
        market: MarketSnapshot,
        score: Score,
        decision: CIODecision,
        news_list: list[News],
    ) -> Path:

        today = datetime.now().strftime("%Y-%m-%d")

        report_dir = Path("04_REPORT/DAILY")
        report_dir.mkdir(parents=True, exist_ok=True)

        report_path = report_dir / f"{today}.md"

        headlines = (
            "\n".join(
                f"- {news.title}"
                for news in news_list[:5]
            )
            if news_list
            else "- No news available."
        )

        global_summary = self._generate_global_summary(market)
        korea_summary = self._generate_korea_summary(market)
        news_summary = self._generate_news_summary(news_list)
        risk_summary = self._generate_risk_summary(score)
        watch_list = self._generate_watch_list(score)
        cio_comment = self._generate_cio_comment(
            score,
            decision,
        )

        report = f"""# 📈 STOCK-CIO Morning Brief

생성시간 : {datetime.now():%Y-%m-%d %H:%M:%S}

---

# 🌎 Global Market

| 항목 | 값 |
|------|------:|
| NASDAQ | {market.nasdaq:.2f} |
| S&P500 | {market.sp500:.2f} |
| VIX | {market.vix:.2f} |

### Market Summary

{global_summary}

---

# 🇰🇷 Korea Market

| 항목 | 값 |
|------|------:|
| KOSPI | {market.kospi:.2f} |
| KOSDAQ | {market.kosdaq:.2f} |

### Market Summary

{korea_summary}

---

# 📊 CIO Score

| 항목 | 점수 |
|------|------:|
| Macro | {score.macro:.2f} |
| Market | {score.market:.2f} |
| Sector | {score.sector:.2f} |
| Money Flow | {score.money_flow:.2f} |
| News | {score.news:.2f} |
| Portfolio | {score.portfolio:.2f} |
| Risk | {score.risk:.2f} |

### TOTAL SCORE

**{score.total:.2f}**

### GRADE

**{score.grade}**

### RATING

**{score.stars}**

---

# 🎯 Today's Decision

| 항목 | 내용 |
|------|------|
| Market Status | {decision.market_status} |
| Action | {decision.action} |
| Cash Ratio | {decision.cash_ratio}% |
| Stock Ratio | {decision.stock_ratio}% |

### Today's CIO Comment

{cio_comment}

---

# 👀 Watch List

{watch_list}

---

# ⚠ Risk Check

{risk_summary}

---

# 📰 Today's News

### News Score

**{score.news:.2f}**

### News Summary

{news_summary}

### Top Headlines

{headlines}

---

Generated by STOCK-CIO

Version : {self.VERSION}
"""

        report_path.write_text(report, encoding="utf-8")

        return report_path