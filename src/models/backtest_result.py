"""
Backtest Result Model

Stock-CIO
"""

from dataclasses import dataclass, field
from datetime import datetime

from src.models.position import Position
from src.models.trade import Trade


@dataclass(slots=True)
class BacktestResult:
    """백테스트 결과"""

    initial_cash: float
    final_cash: float
    final_value: float

    start_date: datetime | None = None
    end_date: datetime | None = None

    trades: list[Trade] = field(default_factory=list)
    positions: list[Position] = field(default_factory=list)

    equity_curve: list[float] = field(default_factory=list)
    daily_returns: list[float] = field(default_factory=list)