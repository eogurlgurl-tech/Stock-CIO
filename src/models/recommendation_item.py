"""
Recommendation Item Model

Represents a single portfolio recommendation.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class RecommendationItem:
    """
    Recommendation item.

    Attributes
    ----------
    category : str
        Recommendation category.

    message : str
        Recommendation message.
    """

    category: str

    message: str