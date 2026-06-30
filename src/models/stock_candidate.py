"""
Stock Candidate Model

Stock-CIO
"""

from dataclasses import dataclass


@dataclass(slots=True)
class StockCandidate:
    """추천 종목"""

    symbol: str

    sector: str

    score: int

    reason: str