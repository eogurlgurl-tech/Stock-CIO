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

        # ==========================
        # NASDAQ (0 ~ 10)
        # ==========================

        if market.nasdaq >= 25000:
            score += 10
        elif market.nasdaq >= 24000:
            score += 8
        elif market.nasdaq >= 23000:
            score += 6
        elif market.nasdaq >= 22000:
            score += 4
        else:
            score += 2

        # ==========================
        # S&P500 (0 ~ 10)
        # ==========================

        if market.sp500 >= 7000:
            score += 10
        elif market.sp500 >= 6500:
            score += 8
        elif market.sp500 >= 6000:
            score += 6
        elif market.sp500 >= 5500:
            score += 4
        else:
            score += 2

        # ==========================
        # VIX (0 ~ 10)
        # 낮을수록 좋음
        # ==========================

        if market.vix <= 15:
            score += 10
        elif market.vix <= 18:
            score += 8
        elif market.vix <= 20:
            score += 6
        elif market.vix <= 25:
            score += 4
        else:
            score += 2

        return score