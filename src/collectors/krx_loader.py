"""
KRX Loader

Stock-CIO
"""

from datetime import datetime, timedelta

from pykrx import stock

from src.collectors.base_loader import BaseLoader
from src.models.market_snapshot import MarketSnapshot


class KRXLoader(BaseLoader):
    """한국 시장 데이터 로더"""

    INDEX = {
        "kospi": "1001",
        "kosdaq": "2001",
    }

    def _market_data(self, ticker: str) -> tuple[float, float]:
        """현재가와 전일 대비 등락률 조회"""

        try:

            today = datetime.now()
            from_date = (today - timedelta(days=10)).strftime("%Y%m%d")
            to_date = today.strftime("%Y%m%d")

            df = stock.get_index_ohlcv_by_date(
                fromdate=from_date,
                todate=to_date,
                ticker=ticker,
            )

            if not self.has_enough_data(df):
                return 0.0, 0.0

            today_close = float(df["종가"].iloc[-1])
            yesterday_close = float(df["종가"].iloc[-2])

            price = self.safe_round(today_close)
            change = self.calculate_change(
                today_close,
                yesterday_close,
            )

            return price, change

        except Exception as e:

            print(f"KRX Loader Error ({ticker}) : {e}")

            return 0.0, 0.0

    def load(self) -> MarketSnapshot:
        """한국 시장 데이터 조회"""

        kospi, kospi_change = self._market_data(
            self.INDEX["kospi"]
        )

        kosdaq, kosdaq_change = self._market_data(
            self.INDEX["kosdaq"]
        )

        return MarketSnapshot(
            market="KRX",
            timestamp=datetime.now(),

            kospi=kospi,
            kospi_change=kospi_change,

            kosdaq=kosdaq,
            kosdaq_change=kosdaq_change,
        )