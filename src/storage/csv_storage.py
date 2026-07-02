"""
CSV Storage

Stock-CIO
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.models.historical_price import HistoricalPrice


class CSVStorage:
    """Historical Data CSV Storage"""

    def __init__(
        self,
        data_dir: str | Path = Path("20_DATA") / "historical",
    ):

        self.data_dir = Path(data_dir)

        self.data_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def exists(
        self,
        symbol: str,
    ) -> bool:
        """CSV 존재 여부"""

        return self._file(symbol).exists()

    def save(
        self,
        history: list[HistoricalPrice],
    ) -> None:
        """HistoricalPrice List 저장"""

        if not history:
            return

        df = pd.DataFrame(
            {
                "Date": [item.date for item in history],
                "Open": [item.open for item in history],
                "High": [item.high for item in history],
                "Low": [item.low for item in history],
                "Close": [item.close for item in history],
                "Volume": [item.volume for item in history],
            }
        )

        df.to_csv(
            self._file(history[0].symbol),
            index=False,
        )

    def load(
        self,
        symbol: str,
    ) -> list[HistoricalPrice]:
        """CSV 로드"""

        file = self._file(symbol)

        if not file.exists():
            return []

        df = pd.read_csv(
            file,
            parse_dates=["Date"],
        )

        history: list[HistoricalPrice] = []

        for _, row in df.iterrows():

            history.append(
                HistoricalPrice(
                    symbol=symbol,
                    date=row["Date"].to_pydatetime(),
                    open=float(row["Open"]),
                    high=float(row["High"]),
                    low=float(row["Low"]),
                    close=float(row["Close"]),
                    volume=int(row["Volume"]),
                )
            )

        return history

    def _file(
        self,
        symbol: str,
    ) -> Path:
        """CSV 파일 경로"""

        return self.data_dir / f"{symbol}.csv"