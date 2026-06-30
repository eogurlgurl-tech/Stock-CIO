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

        score.macro = macro or 0.0
        score.market = market or 0.0
        score.sector = sector or 0.0
        score.money_flow = money_flow or 0.0
        score.news = news or 0.0
        score.portfolio = portfolio or 0.0
        score.risk = risk or 0.0

        score.total = round(
            score.macro * self.weights["macro"]
            + score.market * self.weights["market"]
            + score.sector * self.weights["sector"]
            + score.money_flow * self.weights["money_flow"]
            + score.news * self.weights["news"]
            + score.portfolio * self.weights["portfolio"]
            + score.risk * self.weights["risk"],
            2,
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