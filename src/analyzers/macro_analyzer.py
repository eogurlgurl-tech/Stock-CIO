"""
Macro Analyzer

Stock-CIO
"""

from src.models.market_snapshot import MarketSnapshot


class MacroAnalyzer:
    """거시경제 분석"""

    def analyze(self, market: MarketSnapshot) -> float:
        """
        Macro Score 계산

        Returns
        -------
        float
            0 ~ 100
        """

        score = 0.0

        # ==========================
        # NASDAQ (30)
        # ==========================

        score += self._score_change(market.nasdaq_change)

        # ==========================
        # S&P500 (30)
        # ==========================

        score += self._score_change(market.sp500_change)

        # ==========================
        # SOX (20)
        # ==========================

        score += self._score_change(
            market.sox_change,
            weight=20,
        )

        # ==========================
        # VIX (20)
        # 낮을수록 좋음
        # ==========================

        score += self._score_vix(market.vix_change)

        return round(score, 2)

    # ======================================================

    @staticmethod
    def _score_change(
        change: float | None,
        weight: float = 30,
    ) -> float:

        if change is None:
            return weight * 0.5

        if change >= 2:
            return weight

        if change >= 1:
            return weight * 0.8

        if change >= 0:
            return weight * 0.6

        if change >= -1:
            return weight * 0.4

        return weight * 0.2

    # ======================================================

    @staticmethod
    def _score_vix(change: float | None) -> float:

        weight = 20

        if change is None:
            return weight * 0.5

        if change <= -5:
            return weight

        if change <= -2:
            return weight * 0.8

        if change <= 0:
            return weight * 0.6

        if change <= 5:
            return weight * 0.4

        return weight * 0.2