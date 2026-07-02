"""
Risk Report Model

Represents the result of a portfolio risk analysis.
"""

from dataclasses import dataclass

from src.constants.risk_level import RiskLevel


@dataclass(slots=True)
class RiskReport:
    """
    Portfolio risk analysis result.

    Attributes
    ----------
    portfolio_score : float
        Overall portfolio risk score (0~100).

    concentration_score : float
        Score representing portfolio concentration.

    diversification_score : float
        Score representing portfolio diversification.

    cash_score : float
        Score representing cash allocation.

    largest_weight : float
        Weight of the largest position (0.0~1.0).

    position_count : int
        Number of portfolio positions.

    cash_ratio : float
        Cash ratio within the portfolio (0.0~1.0).

    risk_level : RiskLevel
        Final portfolio risk classification.
    """

    portfolio_score: float
    concentration_score: float
    diversification_score: float
    cash_score: float

    largest_weight: float
    position_count: int
    cash_ratio: float

    risk_level: RiskLevel