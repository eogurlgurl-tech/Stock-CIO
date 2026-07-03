"""
Rebalancing Action Constants

Defines available portfolio rebalancing actions.
"""

from enum import Enum


class RebalancingAction(str, Enum):
    """
    Portfolio rebalancing action.
    """

    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

    def __str__(self) -> str:
        return self.value