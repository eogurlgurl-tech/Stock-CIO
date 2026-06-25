"""
Decision Engine

Stock-CIO
"""

from models.cio_decision import CIODecision
from models.score import Score


class DecisionEngine:
    """Score를 투자 의사결정으로 변환"""

    def make_decision(self, score: Score) -> CIODecision:

        decision = CIODecision()

        if score.total >= 90:
            decision.market_status = "BULLISH"
            decision.action = "STRONG BUY"
            decision.cash_ratio = 10
            decision.stock_ratio = 90

        elif score.total >= 80:
            decision.market_status = "BULLISH"
            decision.action = "BUY"
            decision.cash_ratio = 20
            decision.stock_ratio = 80

        elif score.total >= 60:
            decision.market_status = "NEUTRAL"
            decision.action = "HOLD"
            decision.cash_ratio = 40
            decision.stock_ratio = 60

        else:
            decision.market_status = "BEARISH"
            decision.action = "DEFENSE"
            decision.cash_ratio = 70
            decision.stock_ratio = 30

        return decision