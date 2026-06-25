"""
Market Data Loader

Stock-CIO
"""

from collectors.yahoo_loader import YahooLoader
from models.market_snapshot import MarketSnapshot


class MarketDataLoader:
    """통합 시장 데이터 로더"""

    def __init__(self):

        self.loader = YahooLoader()

    def load(self) -> MarketSnapshot:

        return self.loader.load()