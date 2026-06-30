"""
Stock Screener

Stock-CIO
"""

from dataclasses import dataclass

from src.models.score import Score


@dataclass(slots=True)
class ScreenResult:
    """Stock Screener 결과"""

    top_sectors: list[str]
    watch_list: list[str]


class StockScreener:
    """추천 섹터 및 관심종목 생성"""

    def screen(self, score: Score) -> ScreenResult:

        total = score.total

        # ==========================================================
        # Strong Bull Market
        # ==========================================================

        if total >= 80:

            sectors = [
                "AI",
                "Semiconductor",
                "Power Infrastructure",
                "Defense",
            ]

            watch = [
                "Samsung Electronics",
                "SK Hynix",
                "Hanmi Semiconductor",
                "ISC",
                "Leeno Industrial",
            ]

        # ==========================================================
        # Neutral Market
        # ==========================================================

        elif total >= 60:

            sectors = [
                "Semiconductor",
                "IT",
                "Healthcare",
                "Internet",
            ]

            watch = [
                "Samsung Electronics",
                "LG Energy Solution",
                "NAVER",
                "Hyundai Motor",
                "Kakao",
            ]

        # ==========================================================
        # Defensive Market
        # ==========================================================

        else:

            sectors = [
                "Utilities",
                "Dividend",
                "Consumer Staples",
                "Cash Equivalent",
            ]

            watch = [
                "KODEX 200",
                "TIGER US S&P500",
                "KOSEF Dividend",
            ]

        return ScreenResult(
            top_sectors=sectors,
            watch_list=watch,
        )