"""
US Market Loader

Stock-CIO
"""

from datetime import datetime

import yfinance as yf

from src.collectors.base_loader import BaseLoader
from src.models.market_snapshot import MarketSnapshot


class YahooLoader(BaseLoader):
    """미국 시장 데이터 로더"""

    SYMBOLS = {
        "dow": "^DJI",
        "sp500": "^GSPC",
        "nasdaq": "^IXIC",
        "sox": "^SOX",
        "vix": "^VIX",
    }

    def _market_data(self, symbol: str) -> tuple[float, float]:
        """현재가와 전일 대비 등락률 조회"""

        try:

            df = yf.Ticker(symbol).history(period="5d")

            if not self.has_enough_data(df):
                return 0.0, 0.0

            today = float(df["Close"].iloc[-1])
            yesterday = float(df["Close"].iloc[-2])

            price = self.safe_round(today)
            change = self.calculate_change(today, yesterday)

            return price, change

        except Exception as e:

            print(f"Yahoo Loader Error ({symbol}) : {e}")

            return 0.0, 0.0

    def load(self) -> MarketSnapshot:
        """미국 시장 데이터 조회"""

        dow, dow_change = self._market_data(self.SYMBOLS["dow"])
        sp500, sp500_change = self._market_data(self.SYMBOLS["sp500"])
        nasdaq, nasdaq_change = self._market_data(self.SYMBOLS["nasdaq"])
        sox, sox_change = self._market_data(self.SYMBOLS["sox"])
        vix, vix_change = self._market_data(self.SYMBOLS["vix"])

        return MarketSnapshot(
            market="US",
            timestamp=datetime.now(),

            dow=dow,
            dow_change=dow_change,

            sp500=sp500,
            sp500_change=sp500_change,

            nasdaq=nasdaq,
            nasdaq_change=nasdaq_change,

            sox=sox,
            sox_change=sox_change,

            vix=vix,
            vix_change=vix_change,
        )