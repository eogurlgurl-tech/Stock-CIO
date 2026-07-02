"""
Performance Analyzer

Stock-CIO
"""

from math import sqrt

from src.models.backtest_result import BacktestResult
from src.models.performance_metrics import PerformanceMetrics


class PerformanceAnalyzer:
    """백테스트 성과 분석"""

    TRADING_DAYS = 252

    def analyze(
        self,
        result: BacktestResult,
    ) -> PerformanceMetrics:
        """백테스트 결과 분석"""

        total_return = self.total_return(result)
        cagr = self.cagr(result)
        mdd = self.max_drawdown(result)
        win_rate = self.win_rate(result)
        profit_factor = self.profit_factor(result)
        sharpe_ratio = self.sharpe_ratio(result)
        trade_count = len(result.trades)

        return PerformanceMetrics(
            total_return=total_return,
            cagr=cagr,
            mdd=mdd,
            win_rate=win_rate,
            profit_factor=profit_factor,
            sharpe_ratio=sharpe_ratio,
            trade_count=trade_count,
        )

    @staticmethod
    def total_return(
        result: BacktestResult,
    ) -> float:
        """총 수익률 (%)"""

        if result.initial_cash <= 0:
            return 0.0

        return (
            (result.final_value - result.initial_cash)
            / result.initial_cash
        ) * 100

    @staticmethod
    def win_rate(
        result: BacktestResult,
    ) -> float:
        """승률 (%)"""

        sell_trades = [
            trade
            for trade in result.trades
            if trade.side == "SELL"
        ]

        if not sell_trades:
            return 0.0

        wins = sum(
            1
            for trade in sell_trades
            if trade.realized_profit > 0
        )

        return (wins / len(sell_trades)) * 100

    @staticmethod
    def profit_factor(
        result: BacktestResult,
    ) -> float:
        """Profit Factor"""

        gross_profit = sum(
            trade.realized_profit
            for trade in result.trades
            if trade.realized_profit > 0
        )

        gross_loss = abs(
            sum(
                trade.realized_profit
                for trade in result.trades
                if trade.realized_profit < 0
            )
        )

        if gross_loss == 0:
            return 0.0 if gross_profit == 0 else float("inf")

        return gross_profit / gross_loss

    @staticmethod
    def max_drawdown(
        result: BacktestResult,
    ) -> float:
        """최대 낙폭(MDD, %)"""

        if not result.equity_curve:
            return 0.0

        peak = result.equity_curve[0]
        max_dd = 0.0

        for equity in result.equity_curve:

            if equity > peak:
                peak = equity

            if peak == 0:
                continue

            drawdown = (peak - equity) / peak

            if drawdown > max_dd:
                max_dd = drawdown

        return max_dd * 100

    def cagr(
        self,
        result: BacktestResult,
    ) -> float:
        """연평균 복리수익률(CAGR, %)"""

        if result.initial_cash <= 0:
            return 0.0

        if (
            result.start_date is None
            or result.end_date is None
        ):
            return 0.0

        days = (result.end_date - result.start_date).days

        if days <= 0:
            return 0.0

        years = days / 365.25

        if years <= 0:
            return 0.0

        return (
            (
                result.final_value
                / result.initial_cash
            ) ** (1 / years)
            - 1
        ) * 100

    def sharpe_ratio(
        self,
        result: BacktestResult,
    ) -> float:
        """Sharpe Ratio (Risk Free = 0%)"""

        returns = result.daily_returns

        if len(returns) < 2:
            return 0.0

        mean = sum(returns) / len(returns)

        variance = sum(
            (r - mean) ** 2
            for r in returns
        ) / (len(returns) - 1)

        if variance == 0:
            return 0.0

        std = sqrt(variance)

        return (
            mean / std
        ) * sqrt(self.TRADING_DAYS)