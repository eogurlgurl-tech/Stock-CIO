"""
Performance Analyzer Tests

Stock-CIO
"""

from datetime import datetime

from src.analyzers.performance_analyzer import PerformanceAnalyzer
from src.models.backtest_result import BacktestResult
from src.models.trade import Trade


def create_result() -> BacktestResult:
    """테스트용 BacktestResult"""

    return BacktestResult(
        initial_cash=1_000_000,
        final_cash=1_040_000,
        final_value=1_040_000,
        start_date=datetime(2024, 1, 1),
        end_date=datetime(2025, 1, 1),
        trades=[
            Trade(
                ticker="005930",
                trade_date=datetime(2024, 1, 1),
                side="BUY",
                price=100000,
                quantity=10,
            ),
            Trade(
                ticker="005930",
                trade_date=datetime(2025, 1, 1),
                side="SELL",
                price=104000,
                quantity=10,
                realized_profit=40000,
            ),
        ],
        equity_curve=[
            1_000_000,
            980_000,
            1_010_000,
            1_020_000,
            1_040_000,
        ],
        daily_returns=[
            -0.02,
            0.030612,
            0.009901,
            0.019608,
        ],
    )


def test_total_return():
    """총 수익률"""

    analyzer = PerformanceAnalyzer()

    result = analyzer.total_return(
        create_result()
    )

    assert result == 4.0


def test_win_rate():
    """승률"""

    analyzer = PerformanceAnalyzer()

    result = analyzer.win_rate(
        create_result()
    )

    assert result == 100.0


def test_profit_factor():
    """Profit Factor"""

    analyzer = PerformanceAnalyzer()

    result = analyzer.profit_factor(
        create_result()
    )

    assert result == float("inf")


def test_max_drawdown():
    """최대 낙폭"""

    analyzer = PerformanceAnalyzer()

    result = analyzer.max_drawdown(
        create_result()
    )

    assert round(result, 2) == 2.00


def test_cagr():
    """CAGR"""

    analyzer = PerformanceAnalyzer()

    result = analyzer.cagr(
        create_result()
    )

    assert result > 3.0


def test_sharpe_ratio():
    """Sharpe Ratio"""

    analyzer = PerformanceAnalyzer()

    result = analyzer.sharpe_ratio(
        create_result()
    )

    assert result > 0


def test_analyze():
    """종합 분석"""

    analyzer = PerformanceAnalyzer()

    metrics = analyzer.analyze(
        create_result()
    )

    assert metrics.total_return == 4.0
    assert metrics.trade_count == 2
    assert metrics.win_rate == 100.0
    assert metrics.mdd > 0
    assert metrics.cagr > 0
    assert metrics.sharpe_ratio > 0