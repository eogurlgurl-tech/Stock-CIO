"""
Score Engine

Stock-CIO
"""

from src.config.config_manager import ConfigManager
from src.models.score import Score


class ScoreEngine:
    """Analyzer 점수를 하나의 CIO Score로 통합"""

    def __init__(self):

        config = ConfigManager().load("weight")

        self.weights = config["weights"]

    def calculate(
        self,
        macro: float | None = None,
        market: float | None = None,
        sector: float | None = None,
        money_flow: float | None = None,
        news: float | None = None,
        portfolio: float | None = None,
        risk: float | None = None,
    ) -> Score:

        score = Score()

        values = {
            "macro": macro,
            "market": market,
            "sector": sector,
            "money_flow": money_flow,
            "news": news,
            "portfolio": portfolio,
            "risk": risk,
        }

        score.macro = macro if macro is not None else 0.0
        score.market = market if market is not None else 0.0
        score.sector = sector if sector is not None else 0.0
        score.money_flow = (
            money_flow if money_flow is not None else 0.0
        )
        score.news = news if news is not None else 0.0
        score.portfolio = (
            portfolio if portfolio is not None else 0.0
        )
        score.risk = risk if risk is not None else 0.0

        available_weight = sum(
            self.weights[name]
            for name, value in values.items()
            if value is not None
        )

        weighted_score = sum(
            value * self.weights[name]
            for name, value in values.items()
            if value is not None
        )

        score.total = (
            round(weighted_score / available_weight, 2)
            if available_weight > 0
            else 0.0
        )

        if score.total >= 90:
            score.grade = "S"
            score.stars = "★★★★★"

        elif score.total >= 80:
            score.grade = "A"
            score.stars = "★★★★☆"

        elif score.total >= 70:
            score.grade = "B"
            score.stars = "★★★☆☆"

        elif score.total >= 60:
            score.grade = "C"
            score.stars = "★★☆☆☆"

        else:
            score.grade = "D"
            score.stars = "★☆☆☆☆"

        return score
