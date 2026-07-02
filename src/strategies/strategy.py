"""
Strategy Interface

Stock-CIO
"""

from abc import ABC, abstractmethod

from src.models.historical_price import HistoricalPrice
from src.models.position import Position
from src.models.signal import Signal


class Strategy(ABC):
    """백테스트 전략 인터페이스"""

    def prepare(
        self,
        prices: list[HistoricalPrice],
    ) -> None:
        """
        전략 초기화.

        필요한 지표(MA, RSI, MACD 등)를
        미리 계산한다.
        """

    @abstractmethod
    def next(
        self,
        index: int,
        prices: list[HistoricalPrice],
        position: Position | None,
    ) -> Signal:
        """
        현재 시점의 매매 신호 반환.
        """

        raise NotImplementedError