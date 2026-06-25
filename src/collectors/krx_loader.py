"""
KRX Loader

Stock-CIO
"""

from datetime import datetime

from pykrx import stock

from models.market_snapshot import MarketSnapshot


class KRXLoader:
    """한국 시장 데이터 로더"""

    def load(self) -> MarketSnapshot:
        """KOSPI / KOSDAQ 데이터를 조회"""

        today = datetime.now().strftime("%Y%m%d")

        try:
            kospi = stock.get_index_ohlcv_by_date(
                fromdate=today,
                todate=today,
                ticker="1001",
            )

            kosdaq = stock.get_index_ohlcv_by_date(
                fromdate=today,
                todate=today,
                ticker="2001",
            )

            kospi_close = float(kospi["종가"].iloc[-1])
            kosdaq_close = float(kosdaq["종가"].iloc[-1])

        except Exception:

            # 휴장일 또는 장 시작 전 등 조회 실패 시
            kospi_close = 0.0
            kosdaq_close = 0.0

        return MarketSnapshot(
            market="KRX",
            timestamp=datetime.now(),
            kospi=kospi_close,
            kosdaq=kosdaq_close,
        )