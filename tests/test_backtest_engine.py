"""
Backtest Engine Tests

Stock-CIO
"""

from datetime import datetime

from src.core.backtest_engine import BacktestEngine
from src.models.historical_price import HistoricalPrice
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
            close=70000,
            volume=1000000,
        ),
        HistoricalPrice(
            symbol="005930",
            date=datetime(2024, 1, 3),
            open=71000,
            high=72000,
            low=70500,
            close=72000,
            volume=1200000,
        ),
        HistoricalPrice(
            symbol="005930",
            date=datetime(2024, 1, 4),
            open=72000,
            high=73000,
            low=71500,
            close=73000,
            volume=1300000,
        ),
    ]


def test_backtest_buy_and_hold():
    """Buy & Hold 백테스트"""

    engine = BacktestEngine(
        initial_cash=1_000_000,
    )

    strategy = BuyAndHoldStrategy()

    result = engine.run(
        prices=create_prices(),
        strategy=strategy,
    )

    # 거래 확인
    assert len(result.trades) == 2

    assert result.trades[0].side == "BUY"
    assert result.trades[1].side == "SELL"

    # 포지션 종료
    assert len(result.positions) == 0

    # 시작/종료일
    assert result.start_date == datetime(2024, 1, 2)
    assert result.end_date == datetime(2024, 1, 4)

    # 자산 증가
    assert result.final_value > result.initial_cash

    # 현금 == 최종자산 (포지션 없음)
    assert result.final_cash == result.final_value

    # Equity Curve
    assert len(result.equity_curve) == 3

    # Daily Return
    assert len(result.daily_returns) == 2


def test_empty_price():
    """빈 데이터"""

    engine = BacktestEngine()

    strategy = BuyAndHoldStrategy()

    result = engine.run(
        prices=[],
        strategy=strategy,
    )

    assert result.initial_cash == engine.initial_cash
    assert result.final_cash == engine.initial_cash
    assert result.final_value == engine.initial_cash

    assert result.trades == []
    assert result.positions == []

    assert result.equity_curve == []
    assert result.daily_returns == []


def test_position_closed():
    """백테스트 종료 후 포지션이 없어야 한다."""

    engine = BacktestEngine()

    strategy = BuyAndHoldStrategy()

    result = engine.run(
        prices=create_prices(),
        strategy=strategy,
    )

    assert len(result.positions) == 0


def test_trade_order():
    """거래 순서"""

    engine = BacktestEngine()

    strategy = BuyAndHoldStrategy()

    result = engine.run(
        prices=create_prices(),
        strategy=strategy,
    )

    assert result.trades[0].trade_date < result.trades[1].trade_date

    assert result.trades[0].side == "BUY"

    assert result.trades[1].side == "SELL"