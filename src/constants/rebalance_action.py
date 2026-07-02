"""
Rebalance Action

Stock-CIO
"""

from enum import Enum


class RebalanceAction(str, Enum):
    """Rebalancing Action"""

    BUY = "BUY"

    SELL = "SELL"

    HOLD = "HOLD"