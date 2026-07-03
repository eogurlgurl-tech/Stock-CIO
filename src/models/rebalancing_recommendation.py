"""
Rebalancing Recommendation Model

Represents a single portfolio rebalancing recommendation.
"""

from dataclasses import dataclass

from src.constants.rebalancing_action import (
    RebalancingAction,
)


@dataclass(slots=True)
class RebalancingRecommendation:
    """
    Represents a portfolio rebalancing recommendation.

    Attributes
    ----------
    ticker : str
        Stock ticker.

    action : RebalancingAction
        BUY / SELL / HOLD recommendation.

    current_weight : float
        Current portfolio weight (%).

    target_weight : float
        Target portfolio weight (%).

    weight_difference : float
        Difference between current and target weight (%).

    reason : str
        Reason for the recommendation.
    """

    ticker: str

    action: RebalancingAction

    current_weight: float

    target_weight: float

    weight_difference: float

    reason: str