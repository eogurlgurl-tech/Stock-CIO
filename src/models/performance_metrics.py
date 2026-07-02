"""
Performance Metrics Model

Stock-CIO
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PerformanceMetrics:
    """백테스트 성과 지표"""

    total_return: float = 0.0
    cagr: float = 0.0
    mdd: float = 0.0
    win_rate: float = 0.0
    profit_factor: float = 0.0
    sharpe_ratio: float = 0.0
    trade_count: int = 0