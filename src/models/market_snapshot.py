"""
Market Snapshot Model

Stock-CIO
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class MarketSnapshot:
    """시장 정보를 저장하는 데이터 모델"""

    # ======================================================
    # Basic Information
    # ======================================================

    market: str
    timestamp: datetime

    # ======================================================
    # Korea Market
    # ======================================================

    kospi: float | None = None
    kosdaq: float | None = None

    kospi_change: float | None = None
    kosdaq_change: float | None = None

    # ======================================================
    # US Market
    # ======================================================

    dow: float | None = None
    sp500: float | None = None
    nasdaq: float | None = None

    dow_change: float | None = None
    sp500_change: float | None = None
    nasdaq_change: float | None = None

    # ======================================================
    # Semiconductor
    # ======================================================

    sox: float | None = None
    sox_change: float | None = None

    # ======================================================
    # Volatility
    # ======================================================

    vix: float | None = None
    vix_change: float | None = None

    # ======================================================
    # Currency
    # ======================================================

    usdkrw: float | None = None
    usdkrw_change: float | None = None