"""
CIO Decision Model

Stock-CIO
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class CIODecision:
    """최종 투자 의사결정 모델"""

    market_status: str = "NEUTRAL"

    action: str = "HOLD"

    cash_ratio: int = 50

    stock_ratio: int = 50

    top_sectors: list[str] = field(default_factory=list)

    watch_list: list[str] = field(default_factory=list)

    risks: list[str] = field(default_factory=list)

    summary: str = ""