"""
Decision Type

Represents the final investment decision.
"""

from enum import Enum, auto


class DecisionType(Enum):
    """Final investment decision."""

    BUY = auto()

    HOLD = auto()

    SELL = auto()