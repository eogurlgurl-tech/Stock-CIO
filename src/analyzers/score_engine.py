"""
Score Engine

Stock-CIO
"""

from src.config.config_manager import ConfigManager
from src.models.score import Score


class ScoreEngine:
    """각 Analyzer의 점수를 하나의 Score 객체로 통합"""

    def __init__(self):

        config = ConfigManager().load("weight")

        self.weights = config["weights"]

    def calculate(
        self,
        macro: float,
        market: float,
        sector: float,
        money_flow: float,
        news: float,
        portfolio: float,
        risk: float,
    ) -> Score:

        score = Score()

        score.macro = macro
        score.market = market
        score.sector = sector
        score.money_flow = money_flow
        score.news = news
        score.portfolio = portfolio
        score.risk = risk

        score.total = (
            macro * self.weights["macro"]
            + market * self.weights["market"]
            + sector * self.weights["sector"]
            + money_flow * self.weights["money_flow"]
            + news * self.weights["news"]
            + portfolio * self.weights["portfolio"]
            + risk * self.weights["risk"]
        )

        return score