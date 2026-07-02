"""
Risk Level Constants

Defines portfolio risk classifications used throughout
the STOCK-CIO risk analysis modules.
"""

from enum import Enum


class RiskLevel(str, Enum):
    """Portfolio risk classification."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    VERY_HIGH = "VERY_HIGH"