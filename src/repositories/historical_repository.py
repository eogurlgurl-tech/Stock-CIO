"""
Historical Repository

Stock-CIO
"""

from __future__ import annotations

from src.collectors.historical_data_loader import HistoricalDataLoader
from src.models.historical_price import HistoricalPrice
from src.storage.csv_storage import CSVStorage


class HistoricalRepository:
    """Historical Data Repository"""

    def __init__(
        self,
        loader: HistoricalDataLoader | None = None,
        storage: CSVStorage | None = None,
    ):
        """
        Parameters
        ----------
        loader : HistoricalDataLoader | None
            Historical Data Loader

        storage : CSVStorage | None
            CSV Storage
        """

        self.loader = (
            loader
            if loader is not None
            else HistoricalDataLoader()
        )

        self.storage = (
            storage
            if storage is not None
            else CSVStorage()
        )

    def load(
        self,
        symbol: str,
        period: str = "1y",
    ) -> list[HistoricalPrice]:
        """
        Historical Data 조회

        CSV가 존재하면 CSV를 사용하고,
        없으면 Yahoo Finance에서 다운로드 후 저장한다.
        """

        if self.storage.exists(symbol):
            return self.storage.load(symbol)

        history = self.loader.load(
            symbol=symbol,
            period=period,
        )

        if history:
            self.storage.save(history)

        return history