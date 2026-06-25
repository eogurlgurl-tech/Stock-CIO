"""
Yahoo Market Loader

Stock-CIO
"""

from datetime import datetime

import yfinance as yf

from models.market_snapshot import MarketSnapshot


class YahooLoader:
    """Yahoo Finance 통합 시장 데이터"""

    SYMBOLS = {
        "kospi": "^KS11",
        "kosdaq": "^KQ11",
        "sp500": "^GSPC",
        "nasdaq": "^IXIC",
        "vix": "^VIX",
        "sox": "^SOX",
    }

    def _price(self, symbol: str) -> float:

        try:

            df = yf.Ticker(symbol).history(period="5d")

            return float(df["Close"].iloc[-1])

        except Exception as e:

            print(f"Yahoo Loader Error ({symbol}) : {e}")

            return 0.0

    def load(self) -> MarketSnapshot:

        return MarketSnapshot(

            market="GLOBAL",

            timestamp=datetime.now(),

            kospi=self._price("^KS11"),

            kosdaq=self._price("^KQ11"),

            sp500=self._price("^GSPC"),

            nasdaq=self._price("^IXIC"),

            vix=self._price("^VIX"),

            sox=self._price("^SOX"),

        )