"""
Buy & Hold Strategy

Stock-CIO
"""

from src.models.historical_price import HistoricalPrice
from src.models.position import Position
from src.models.signal import Signal
from src.strategies.strategy import Strategy


class BuyAndHoldStrategy(Strategy):
    """
    가장 단순한 백테스트 전략.

    첫 번째 거래일 매수
    마지막 거래일 매도
    """

    def prepare(
        self,
        prices: list[HistoricalPrice],
    ) -> None:
        """
        사전 계산 없음.
        """

        return

    def next(
        self,
        index: int,
        prices: list[HistoricalPrice],
        position: Position | None,
    ) -> Signal:
        """
        현재 시점의 매매 신호를 반환한다.
        """

        if not prices:
            return Signal.HOLD

        # 첫 거래일 매수
        if index == 0 and position is None:
            return Signal.BUY

        # 마지막 거래일 매도
        if (
            index == len(prices) - 1
            and position is not None
        ):
            return Signal.SELL

        return Signal.HOLD