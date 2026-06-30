"""
Score Model

Stock-CIO
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Score:
    """CIO Score Model"""

    # ==========================
    # Analyzer Scores
    # ==========================

    macro: float = 0.0
    market: float = 0.0
    sector: float = 0.0
    money_flow: float = 0.0
    news: float = 0.0
    portfolio: float = 0.0
    risk: float = 0.0

    # ==========================
    # Final Result
    # ==========================

    total: float = 0.0
    grade: str = ""
    stars: str = ""