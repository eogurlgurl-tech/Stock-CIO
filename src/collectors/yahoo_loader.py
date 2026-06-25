"""
Yahoo Market Loader

Stock-CIO
"""

from datetime import datetime

import yfinance as yf

from models.market_snapshot import MarketSnapshot


class YahooLoader:
    """Yahoo Finance 시장 데이터 로더"""

    def load(self) -> MarketSnapshot:

        symbols = {
            "kospi": "^KS11",
            "kosdaq": "^KQ11",
            "sp500": "^GSPC",
            "nasdaq": "^IXIC",
            "vix": "^VIX",
        }

        result = {}

        for key, ticker in symbols.items():

            try:
                data = yf.Ticker(ticker).history(period="5d")

                result[key] = float(data["Close"].iloc[-1])

            except Exception:

                result[key] = 0.0

        return MarketSnapshot(
            market="GLOBAL",
            timestamp=datetime.now(),
            kospi=result["kospi"],
            kosdaq=result["kosdaq"],
            sp500=result["sp500"],
            nasdaq=result["nasdaq"],
            vix=result["vix"],
        )