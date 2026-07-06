"""
CIO Decision Model

Stock-CIO
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class CIODecision:
    """Final CIO investment decision model."""

    market_status: str = "NEUTRAL"

    action: str = "HOLD"

    cash_ratio: int = 50

    stock_ratio: int = 50

    top_sectors: list[str] = field(default_factory=list)

    watch_list: list[str] = field(default_factory=list)

    risks: list[str] = field(default_factory=list)

    summary: str = ""