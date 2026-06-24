"""
Market Data Loader
"""

from collectors.krx_loader import KRXLoader
from collectors.us_loader import USLoader
from models.market_snapshot import MarketSnapshot


class MarketDataLoader:
    """시장 데이터 통합 로더"""

    def __init__(self) -> None:
        self.krx_loader = KRXLoader()
        self.us_loader = USLoader()

    def load(self) -> MarketSnapshot:
        """한국시장 + 미국시장 데이터를 합친다."""

        kr = self.krx_loader.load()
        us = self.us_loader.load()

        return MarketSnapshot(
            market="GLOBAL",
            timestamp=kr.timestamp,

            kospi=kr.kospi,
            kosdaq=kr.kosdaq,

            sp500=us.sp500,
            nasdaq=us.nasdaq,
            vix=us.vix,
        )