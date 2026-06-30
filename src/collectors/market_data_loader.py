"""
Market Data Loader

Stock-CIO
"""

from src.collectors.krx_loader import KRXLoader
from src.collectors.us_loader import YahooLoader
from src.models.market_snapshot import MarketSnapshot


class MarketDataLoader:
    """통합 시장 데이터 로더"""

    def __init__(self):

        self.krx_loader = KRXLoader()
        self.us_loader = YahooLoader()

    def load(self) -> MarketSnapshot:
        """국내 + 미국 시장 데이터를 병합"""

        krx = self.krx_loader.load()
        us = self.us_loader.load()

        return MarketSnapshot(
            market="GLOBAL",
            timestamp=krx.timestamp,

            # Korea
            kospi=krx.kospi,
            kospi_change=krx.kospi_change,

            kosdaq=krx.kosdaq,
            kosdaq_change=krx.kosdaq_change,

            # US
            dow=us.dow,
            dow_change=us.dow_change,

            sp500=us.sp500,
            sp500_change=us.sp500_change,

            nasdaq=us.nasdaq,
            nasdaq_change=us.nasdaq_change,

            # Semiconductor
            sox=us.sox,
            sox_change=us.sox_change,

            # Volatility
            vix=us.vix,
            vix_change=us.vix_change,
        )