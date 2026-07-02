"""
Historical Price Model

Stock-CIO
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class HistoricalPrice:
    """일별 주가 데이터"""

    symbol: str

    date: datetime

    open: float

    high: float

    low: float

    close: float

    volume: int