"""
Decision Engine

Stock-CIO
"""

from src.config.config_manager import ConfigManager
from src.models.cio_decision import CIODecision
from src.models.score import Score


class DecisionEngine:
    """Score를 투자 의사결정으로 변환"""

    def __init__(self):

        config = ConfigManager().load("strategy")

        self.strategy = config["decision"]
        self.portfolio = config["portfolio"]

    def make_decision(self, score: Score) -> CIODecision:

        decision = CIODecision()

        total = score.total

        if total >= self.strategy["strong_buy"]:

            decision.market_status = "BULLISH"
            decision.action = "STRONG BUY"

            decision.cash_ratio = 100 - self.portfolio["max_position"]
            decision.stock_ratio = self.portfolio["max_position"]

        elif total >= self.strategy["buy"]:

            decision.market_status = "BULLISH"
            decision.action = "BUY"

            decision.cash_ratio = 100 - (
                self.portfolio["initial_position"]
                + self.portfolio["add_position"]
            )

            decision.stock_ratio = (
                self.portfolio["initial_position"]
                + self.portfolio["add_position"]
            )

        elif total >= self.strategy["watch"]:

            decision.market_status = "NEUTRAL"
            decision.action = "HOLD"

            decision.cash_ratio = 50
            decision.stock_ratio = 50

        elif total >= self.strategy["reduce"]:

            decision.market_status = "CAUTION"
            decision.action = "REDUCE"

            decision.cash_ratio = 70
            decision.stock_ratio = 30

        else:

            decision.market_status = "BEARISH"
            decision.action = "SELL"

            decision.cash_ratio = 100
            decision.stock_ratio = 0

        return decision