"""
Signal Model

Stock-CIO
"""

from enum import Enum


class Signal(str, Enum):
    """매매 신호"""

    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

    def __str__(self) -> str:
        return self.value