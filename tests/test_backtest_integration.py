"""
Backtest Integration Test

Stock-CIO
"""

from datetime import datetime

from src.analyzers.performance_analyzer import PerformanceAnalyzer
from src.core.backtest_engine import BacktestEngine
from src.models.historical_price import HistoricalPrice
from src.strategies.buy_and_hold_strategy import BuyAndHoldStrategy


def create_prices() -> list[HistoricalPrice]:
    """통합 테스트용 가격 데이터"""

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
            open=70500,
            high=72000,
            low=70000,
            close=72000,
            volume=1200000,
        ),
        HistoricalPrice(
            symbol="005930",
            date=datetime(2024, 1, 4),
            open=72000,
            high=73500,
            low=71500,
            close=73000,
            volume=1400000,
        ),
        HistoricalPrice(
            symbol="005930",
            date=datetime(2024, 1, 5),
            open=73000,
            high=74000,
            low=72500,
            close=74000,
            volume=1500000,
        ),
    ]


def test_backtest_integration():
    """Backtest 전체 통합 테스트"""

    engine = BacktestEngine(
        initial_cash=1_000_000,
    )

    strategy = BuyAndHoldStrategy()

    analyzer = PerformanceAnalyzer()

    result = engine.run(
        prices=create_prices(),
        strategy=strategy,
    )

    metrics = analyzer.analyze(result)

    # 거래 검증
    assert len(result.trades) == 2

    assert result.trades[0].side == "BUY"
    assert result.trades[1].side == "SELL"

    # 포지션 종료
    assert len(result.positions) == 0

    # 최종 자산 증가
    assert result.final_value > result.initial_cash

    # Equity Curve
    assert len(result.equity_curve) == len(create_prices())

    # Daily Returns
    assert len(result.daily_returns) == len(create_prices()) - 1

    # 성과지표
    assert metrics.trade_count == 2

    assert metrics.total_return > 0

    assert metrics.win_rate == 100.0

    assert metrics.mdd >= 0

    assert metrics.sharpe_ratio >= 0