"""
Backtest Engine

Stock-CIO
"""

from src.models.backtest_result import BacktestResult
from src.models.historical_price import HistoricalPrice
from src.models.position import Position
from src.models.signal import Signal
from src.models.trade import Trade
from src.strategies.strategy import Strategy


class BacktestEngine:
    """백테스트 엔진"""

    def __init__(
        self,
        initial_cash: float = 10_000_000,
    ):
        self.initial_cash = initial_cash

    def run(
        self,
        prices: list[HistoricalPrice],
        strategy: Strategy,
    ) -> BacktestResult:
        """백테스트 실행"""

        # 빈 데이터 처리
        if not prices:
            return BacktestResult(
                initial_cash=self.initial_cash,
                final_cash=self.initial_cash,
                final_value=self.initial_cash,
                start_date=None,
                end_date=None,
                trades=[],
                positions=[],
                equity_curve=[],
                daily_returns=[],
            )

        # 전략 초기화
        strategy.prepare(prices)

        cash = self.initial_cash

        position: Position | None = None

        trades: list[Trade] = []
        equity_curve: list[float] = []
        daily_returns: list[float] = []

        previous_equity: float | None = None

        start_date = None
        end_date = None

        for index, price in enumerate(prices):

            if start_date is None:
                start_date = price.date

            end_date = price.date

            signal = strategy.next(
                index=index,
                prices=prices,
                position=position,
            )

            # BUY
            if signal == Signal.BUY and position is None:

                if price.close > 0:

                    quantity = int(cash // price.close)

                    if quantity > 0:

                        cash -= quantity * price.close

                        position = Position(
                            ticker=price.symbol,
                            quantity=quantity,
                            average_price=price.close,
                            current_price=price.close,
                        )

                        trades.append(
                            Trade(
                                ticker=price.symbol,
                                trade_date=price.date,
                                side="BUY",
                                price=price.close,
                                quantity=quantity,
                            )
                        )

            # 현재가 갱신
            if position is not None:
                position.current_price = price.close

            # SELL
            if signal == Signal.SELL and position is not None:

                realized_profit = (
                    price.close
                    - position.average_price
                ) * position.quantity

                cash += (
                    position.quantity
                    * price.close
                )

                trades.append(
                    Trade(
                        ticker=position.ticker,
                        trade_date=price.date,
                        side="SELL",
                        price=price.close,
                        quantity=position.quantity,
                        realized_profit=realized_profit,
                    )
                )

                position = None

            # Equity 계산
            equity = cash

            if position is not None:
                equity += position.market_value

            equity_curve.append(equity)

            if (
                previous_equity is not None
                and previous_equity > 0
            ):
                daily_returns.append(
                    (equity - previous_equity)
                    / previous_equity
                )

            previous_equity = equity

        final_value = cash

        positions: list[Position] = []

        if position is not None:

            final_value += position.market_value
            positions.append(position)

        return BacktestResult(
            initial_cash=self.initial_cash,
            final_cash=cash,
            final_value=final_value,
            start_date=start_date,
            end_date=end_date,
            trades=trades,
            positions=positions,
            equity_curve=equity_curve,
            daily_returns=daily_returns,
        )