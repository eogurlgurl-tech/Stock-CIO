"""
Historical Data Loader

Stock-CIO
"""

from __future__ import annotations

import yfinance as yf

from src.collectors.base_loader import BaseLoader
from src.models.historical_price import HistoricalPrice


class HistoricalDataLoader(BaseLoader):
    """과거 주가 데이터 로더"""

    def load(
        self,
        symbol: str,
        period: str = "1y",
    ) -> list[HistoricalPrice]:
        """
        과거 주가 조회

        Parameters
        ----------
        symbol : str
            Yahoo Finance Symbol

        period : str
            ex)
            6mo
            1y
            2y
            5y

        Returns
        -------
        list[HistoricalPrice]
        """

        try:

            df = yf.Ticker(symbol).history(period=period)

            if not self.has_enough_data(df):
                return []

            history: list[HistoricalPrice] = []

            for date, row in df.iterrows():

                history.append(
                    HistoricalPrice(
                        symbol=symbol,
                        date=date.to_pydatetime(),

                        open=self.safe_round(row["Open"]),
                        high=self.safe_round(row["High"]),
                        low=self.safe_round(row["Low"]),
                        close=self.safe_round(row["Close"]),

                        volume=int(row["Volume"]),
                    )
                )

            return history

        except Exception as e:

            print(
                f"Historical Data Loader Error ({symbol}) : {e}"
            )

            return []