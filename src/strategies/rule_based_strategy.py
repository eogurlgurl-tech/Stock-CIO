"""
Rule Based Strategy

Stock-CIO
"""

from __future__ import annotations

from src.models.portfolio import Portfolio
from src.models.position import Position

from .allocation_strategy import AllocationStrategy


class RuleBasedStrategy(AllocationStrategy):
    """Create target weights with a maximum position limit."""

    MAX_WEIGHT = 30.0

    def allocate(
        self,
        portfolio: Portfolio,
    ) -> Portfolio:
        """Create a separate target allocation."""

        target = self._clone(portfolio)

        if target.is_empty:
            return target

        if len(target.positions) * self.MAX_WEIGHT < 100.0:
            self._apply_equal_weight(target)
            return target

        self._calculate_weights(target)
        self._apply_max_weight(target)
        self._finalize_weights(target)

        return target

    @staticmethod
    def _clone(
        portfolio: Portfolio,
    ) -> Portfolio:
        """Clone portfolio and positions."""

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
        """Calculate unrounded stock allocation weights."""

        total = portfolio.stock_asset

        if total <= 0:
            return

        for position in portfolio.positions:
            position.weight = (
                position.market_value / total * 100.0
            )

    def _apply_max_weight(
        self,
        portfolio: Portfolio,
    ) -> None:
        """Cap and redistribute weights until all satisfy the limit."""

        capped: set[int] = set()

        while True:
            exceeded = [
                index
                for index, position in enumerate(
                    portfolio.positions
                )
                if (
                    index not in capped
                    and position.weight > self.MAX_WEIGHT
                )
            ]

            if not exceeded:
                return

            excess = 0.0

            for index in exceeded:
                position = portfolio.positions[index]
                excess += position.weight - self.MAX_WEIGHT
                position.weight = self.MAX_WEIGHT
                capped.add(index)

            candidates = [
                position
                for index, position in enumerate(
                    portfolio.positions
                )
                if index not in capped
            ]

            if not candidates:
                return

            share = excess / len(candidates)

            for position in candidates:
                position.weight += share

    @staticmethod
    def _apply_equal_weight(
        portfolio: Portfolio,
    ) -> None:
        """Apply equal weights when the configured cap is infeasible."""

        count = len(portfolio.positions)

        if count == 0:
            return

        weight = 100.0 / count

        for position in portfolio.positions:
            position.weight = weight

        RuleBasedStrategy._finalize_weights(portfolio)

    @staticmethod
    def _finalize_weights(
        portfolio: Portfolio,
    ) -> None:
        """Round weights while keeping the total at 100%."""

        if portfolio.is_empty:
            return

        for position in portfolio.positions:
            position.weight = round(position.weight, 2)

        difference = round(
            100.0
            - sum(
                position.weight
                for position in portfolio.positions
            ),
            2,
        )

        if difference == 0:
            return

        candidate = min(
            portfolio.positions,
            key=lambda position: position.weight,
        )
        candidate.weight = round(
            candidate.weight + difference,
            2,
        )
