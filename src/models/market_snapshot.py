"""
Market Snapshot Model

Stock-CIO
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class MarketSnapshot:
    """시장 정보를 저장하는 데이터 모델"""

    market: str
    timestamp: datetime

    kospi: float | None = None
    kosdaq: float | None = None

    dow: float | None = None
    sp500: float | None = None
    nasdaq: float | None = None

    vix: float | None = None
    sox: float | None = None

    usdkrw: float | None = None