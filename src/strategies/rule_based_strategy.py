"""
Rule Based Strategy

Stock-CIO

Generates a target portfolio using predefined allocation rules.
"""

from __future__ import annotations

from src.models.portfolio import Portfolio
from src.models.position import Position

from .allocation_strategy import AllocationStrategy


class RuleBasedStrategy(AllocationStrategy):
    """Rule-based portfolio allocation strategy."""

    MAX_WEIGHT = 30.0

    def allocate(
        self,
        portfolio: Portfolio,
    ) -> Portfolio:
        """
        Create target allocation.

        Rules
        -----
        1. Limit maximum position weight.
        2. Redistribute excess weight.
        """

        target = self._clone(portfolio)

        self._calculate_weights(target)
        self._apply_max_weight(target)
        self._normalize(target)

        return target

    @staticmethod
    def _clone(
        portfolio: Portfolio,
    ) -> Portfolio:
        """Clone portfolio."""

        return Portfolio(
            cash=portfolio.cash,
            positions=[
                Position(
                    ticker=position.ticker,
                    name=position.name,
                    quantity=position.quantity,
                    average_price=position.average_price,
                    current_price=position.current_price,
                    weight=position.weight,
                )
                for position in portfolio.positions
            ],
        )

    @staticmethod
    def _calculate_weights(
        portfolio: Portfolio,
    ) -> None:
        """Calculate current weights."""

        total = portfolio.stock_asset

        if total <= 0:
            return

        for position in portfolio.positions:
            position.weight = round(
                position.market_value / total * 100,
                2,
            )

    def _apply_max_weight(
        self,
        portfolio: Portfolio,
    ) -> None:
        """Apply maximum weight rule."""

        excess = 0.0
        candidates: list[Position] = []

        for position in portfolio.positions:

            if position.weight > self.MAX_WEIGHT:

                excess += (
                    position.weight
                    - self.MAX_WEIGHT
                )

                position.weight = self.MAX_WEIGHT

            else:
                candidates.append(position)

        if excess <= 0:
            return

        if not candidates:
            return

        share = excess / len(candidates)

        for position in candidates:
            position.weight += share

    @staticmethod
    def _normalize(
        portfolio: Portfolio,
    ) -> None:
        """Normalize total weight to 100%."""

        total = sum(
            position.weight
            for position in portfolio.positions
        )

        if total <= 0:
            return

        ratio = 100.0 / total

        for position in portfolio.positions:
            position.weight = round(
                position.weight * ratio,
                2,
            )