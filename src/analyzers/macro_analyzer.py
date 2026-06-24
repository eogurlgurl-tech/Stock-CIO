"""
Macro Analyzer

Stock-CIO
"""

from models.market_snapshot import MarketSnapshot


class MacroAnalyzer:
    """거시경제 분석"""

    def analyze(self, market: MarketSnapshot) -> int:
        """
        Macro Score 계산

        최대 30점
        """

        score = 0

        # NASDAQ
        if market.nasdaq > 20000:
            score += 10

        # S&P500
        if market.sp500 > 6000:
            score += 10

        # VIX
        if market.vix < 20:
            score += 10

        return score