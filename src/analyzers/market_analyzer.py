"""
Market Analyzer

Stock-CIO
"""

from src.models.market_snapshot import MarketSnapshot


class MarketAnalyzer:
    """국내 시장 분석"""

    def analyze(self, market: MarketSnapshot) -> float:
        """
        KOSPI / KOSDAQ 기반 Market Score 계산

        Returns
        -------
        float
            0 ~ 100
        """

        score = 0.0

        # ==========================
        # KOSPI (50)
        # ==========================

        score += self._score_change(
            market.kospi_change,
            weight=50,
        )

        # ==========================
        # KOSDAQ (50)
        # ==========================

        score += self._score_change(
            market.kosdaq_change,
            weight=50,
        )

        return round(score, 2)

    # ======================================================

    @staticmethod
    def _score_change(
        change: float | None,
        weight: float,
    ) -> float:

        if change is None:
            return weight * 0.5

        if change >= 2.0:
            return weight

        if change >= 1.0:
            return weight * 0.8

        if change >= 0.0:
            return weight * 0.6

        if change >= -1.0:
            return weight * 0.4

        return weight * 0.2