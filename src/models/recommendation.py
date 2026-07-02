"""
Recommendation Model

Represents the result of a portfolio recommendation.
"""

from dataclasses import dataclass, field

from src.constants.risk_level import RiskLevel


@dataclass(slots=True)
class Recommendation:
    """
    Portfolio recommendation result.

    Attributes
    ----------
    overall_grade : str
        Overall recommendation grade.

    portfolio_score : float
        Overall portfolio score.

    risk_level : RiskLevel
        Portfolio risk level.

    summary : str
        Recommendation summary.

    recommendation_items : list[str]
        Recommendation list.
    """

    overall_grade: str

    portfolio_score: float

    risk_level: RiskLevel

    summary: str

    recommendation_items: list[str] = field(
        default_factory=list
    )