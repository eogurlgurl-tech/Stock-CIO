"""
KRX Loader

Stock-CIO
"""

from datetime import datetime, timedelta

import yfinance as yf

from src.collectors.base_loader import BaseLoader
from src.models.market_snapshot import MarketSnapshot


class KRXLoader(BaseLoader):
    """Load Korean market index data with fallback support."""

    INDEX = {
        "kospi": "1001",
        "kosdaq": "2001",
    }

    SYMBOLS = {
        "kospi": "^KS11",
        "kosdaq": "^KQ11",
    }

    def _market_data(
        self,
        ticker: str,
        symbol: str,
    ) -> tuple[float, float | None]:
        """Load index data from Yahoo and then pykrx."""

        yahoo_result = self._yahoo_market_data(symbol)

        if yahoo_result is not None:
            return yahoo_result

        pykrx_result = self._pykrx_market_data(ticker)

        if pykrx_result is not None:
            return pykrx_result

        print(
            f"KRX data unavailable: {ticker} / {symbol}"
        )

        return 0.0, None

    def _yahoo_market_data(
        self,
        symbol: str,
    ) -> tuple[float, float] | None:
        """Load a Korean index through Yahoo Finance."""

        try:
            frame = yf.Ticker(symbol).history(period="10d")

            if not self.has_enough_data(frame):
                return None

            current_close = float(frame["Close"].iloc[-1])
            previous_close = float(frame["Close"].iloc[-2])

            return (
                self.safe_round(current_close),
                self.calculate_change(
                    current_close,
                    previous_close,
                ),
            )

        except Exception as error:
            print(
                f"Yahoo KRX Loader Error ({symbol}) : {error}"
            )
            return None

    def _pykrx_market_data(
        self,
        ticker: str,
    ) -> tuple[float, float] | None:
        """Load a Korean index through pykrx as fallback."""

        try:
            from pykrx import stock

            today = datetime.now()
            from_date = (
                today - timedelta(days=10)
            ).strftime("%Y%m%d")
            to_date = today.strftime("%Y%m%d")

            frame = stock.get_index_ohlcv_by_date(
                fromdate=from_date,
                todate=to_date,
                ticker=ticker,
            )

            if not self.has_enough_data(frame):
                return None

            current_close = float(frame["종가"].iloc[-1])
            previous_close = float(frame["종가"].iloc[-2])

            return (
                self.safe_round(current_close),
                self.calculate_change(
                    current_close,
                    previous_close,
                ),
            )

        except Exception as error:
            print(
                f"pykrx Loader Error ({ticker}) : {error}"
            )
            return None

    def load(self) -> MarketSnapshot:
        """Load KOSPI and KOSDAQ index data."""

        kospi, kospi_change = self._market_data(
            self.INDEX["kospi"],
            self.SYMBOLS["kospi"],
        )
        kosdaq, kosdaq_change = self._market_data(
            self.INDEX["kosdaq"],
            self.SYMBOLS["kosdaq"],
        )

        return MarketSnapshot(
            market="KRX",
            timestamp=datetime.now(),
            kospi=kospi,
            kospi_change=kospi_change,
            kosdaq=kosdaq,
            kosdaq_change=kosdaq_change,
        )
