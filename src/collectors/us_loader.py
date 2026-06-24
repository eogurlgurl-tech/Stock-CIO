"""
US Loader

미국 시장 데이터를 Yahoo Finance에서 가져온다.
"""

from datetime import datetime

import yfinance as yf

from models.market_snapshot import MarketSnapshot


class USLoader:
    """미국 시장 데이터 로더"""

    def load(self) -> MarketSnapshot:
        """미국 주요 지수를 조회한다."""

        try:
            sp500 = yf.Ticker("^GSPC").history(period="5d")
            nasdaq = yf.Ticker("^IXIC").history(period="5d")
            vix = yf.Ticker("^VIX").history(period="5d")

            sp500_close = float(sp500["Close"].iloc[-1])
            nasdaq_close = float(nasdaq["Close"].iloc[-1])
            vix_close = float(vix["Close"].iloc[-1])

        except Exception as e:
            print(f"US Loader Error : {e}")

            sp500_close = 0.0
            nasdaq_close = 0.0
            vix_close = 0.0

        return MarketSnapshot(
            market="US",
            timestamp=datetime.now(),
            sp500=sp500_close,
            nasdaq=nasdaq_close,
            vix=vix_close,
        )