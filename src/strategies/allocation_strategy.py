"""
Allocation Strategy

Stock-CIO

Abstract base class for portfolio allocation strategies.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from src.models.portfolio import Portfolio


class AllocationStrategy(ABC):
    """Allocation Strategy Interface"""

    @abstractmethod
    def allocate(
        self,
        portfolio: Portfolio,
    ) -> Portfolio:
        """
        Allocate portfolio weights.

        Parameters
        ----------
        portfolio : Portfolio

        Returns
        -------
        Portfolio
            Portfolio with updated target weights.
        """
        raise NotImplementedError