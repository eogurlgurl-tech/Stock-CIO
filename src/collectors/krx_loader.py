"""
KRX Loader

현재는 테스트용 데이터를 반환한다.
"""

from datetime import datetime

from models.market_snapshot import MarketSnapshot


class KRXLoader:
    """한국 시장 데이터 로더"""

    def load(self) -> MarketSnapshot:
        """시장 데이터를 반환한다."""

        return MarketSnapshot(
            market="KRX",
            timestamp=datetime.now(),
            kospi=0.0,
            kosdaq=0.0,
        )