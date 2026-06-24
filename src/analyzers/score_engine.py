"""
Score Engine

Stock-CIO
"""

from analyzers.macro_analyzer import MacroAnalyzer
from models.market_snapshot import MarketSnapshot
from models.score import Score


class ScoreEngine:

    def __init__(self):

        self.macro = MacroAnalyzer()

    def calculate(self, market: MarketSnapshot) -> Score:

        score = Score()

        score.macro = self.macro.analyze(market)

        score.sector = 0
        score.money_flow = 0
        score.news = 0
        score.portfolio = 0
        score.risk = 0

        return score