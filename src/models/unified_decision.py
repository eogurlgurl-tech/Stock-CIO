"""
Unified Decision Model

Stock-CIO
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class UnifiedDecision:
    """Final action combining market and portfolio decisions."""

    market_action: str

    portfolio_action: str

    final_action: str

    reason: str
