"""
Buy & Hold Strategy Tests

Stock-CIO
"""

from datetime import datetime

from src.models.historical_price import HistoricalPrice
from src.models.position import Position
from src.models.signal import Signal
from src.strategies.buy_and_hold_strategy import BuyAndHoldStrategy


def create_prices() -> list[HistoricalPrice]:
    """테스트용 가격 데이터"""

    return [
        HistoricalPrice(
            symbol="005930",
            date=datetime(2024, 1, 2),
            open=70000,
            high=71000,
            low=69500,
            close=70500,
            volume=1000000,
        ),
        HistoricalPrice(
            symbol="005930",
            date=datetime(2024, 1, 3),
            open=70500,
            high=71500,
            low=70000,
            close=71000,
            volume=1200000,
        ),
        HistoricalPrice(
            symbol="005930",
            date=datetime(2024, 1, 4),
            open=71000,
            high=72000,
            low=70500,
            close=71500,
            volume=1300000,
        ),
    ]


def create_position() -> Position:
    """테스트용 포지션"""

    return Position(
        ticker="005930",
        quantity=10,
        average_price=70500,
        current_price=70500,
    )


def test_prepare():
    """prepare()는 예외 없이 수행된다."""

    strategy = BuyAndHoldStrategy()

    strategy.prepare(create_prices())


def test_first_day_buy_signal():
    """첫 거래일에는 BUY"""

    strategy = BuyAndHoldStrategy()

    signal = strategy.next(
        index=0,
        prices=create_prices(),
        position=None,
    )

    assert signal == Signal.BUY


def test_middle_day_hold_signal():
    """중간 거래일에는 HOLD"""

    strategy = BuyAndHoldStrategy()

    signal = strategy.next(
        index=1,
        prices=create_prices(),
        position=create_position(),
    )

    assert signal == Signal.HOLD


def test_last_day_sell_signal():
    """마지막 거래일에는 SELL"""

    prices = create_prices()

    strategy = BuyAndHoldStrategy()

    signal = strategy.next(
        index=len(prices) - 1,
        prices=prices,
        position=create_position(),
    )

    assert signal == Signal.SELL


def test_last_day_without_position_hold():
    """포지션이 없으면 마지막 날도 HOLD"""

    prices = create_prices()

    strategy = BuyAndHoldStrategy()

    signal = strategy.next(
        index=len(prices) - 1,
        prices=prices,
        position=None,
    )

    assert signal == Signal.HOLD


def test_empty_price_hold():
    """가격 데이터가 없으면 HOLD"""

    strategy = BuyAndHoldStrategy()

    signal = strategy.next(
        index=0,
        prices=[],
        position=None,
    )

    assert signal == Signal.HOLD