"""
Rebalancing Engine

Stock-CIO
"""

from src.constants.rebalance_action import RebalanceAction
from src.models.portfolio import Portfolio
from src.models.rebalance_item import RebalanceItem
from src.models.rebalance_plan import RebalancePlan


class RebalancingEngine:
    """Compare current and target portfolio weights."""

    DEFAULT_TOLERANCE = 1.0

    def __init__(
        self,
        tolerance: float = DEFAULT_TOLERANCE,
    ) -> None:
        """Initialize with an absolute weight tolerance in %p."""

        if tolerance < 0:
            raise ValueError(
                "Rebalancing tolerance must be non-negative."
            )

        self._tolerance = tolerance

    @property
    def tolerance(self) -> float:
        """Return the current rebalance tolerance."""

        return self._tolerance

    def create_plan(
        self,
        current: Portfolio,
        target: Portfolio,
    ) -> RebalancePlan:
        """Compare current and target and create a plan."""

        plan = RebalancePlan()
        current_map = {
            position.ticker: position
            for position in current.positions
        }
        target_map = {
            position.ticker: position
            for position in target.positions
        }

        for current_position in current.positions:
            target_position = target_map.get(
                current_position.ticker
            )

            if target_position is None:
                plan.add_item(
                    RebalanceItem(
                        ticker=current_position.ticker,
                        name=current_position.name,
                        current_weight=current_position.weight,
                        target_weight=0.0,
                        action=RebalanceAction.SELL,
                    )
                )
                continue

            difference = (
                target_position.weight
                - current_position.weight
            )

            if abs(difference) < self._tolerance:
                action = RebalanceAction.HOLD
            elif difference > 0:
                action = RebalanceAction.BUY
            else:
                action = RebalanceAction.SELL

            plan.add_item(
                RebalanceItem(
                    ticker=current_position.ticker,
                    name=current_position.name,
                    current_weight=current_position.weight,
                    target_weight=target_position.weight,
                    action=action,
                )
            )

        for target_position in target.positions:
            if target_position.ticker in current_map:
                continue

            action = (
                RebalanceAction.BUY
                if target_position.weight >= self._tolerance
                else RebalanceAction.HOLD
            )

            plan.add_item(
                RebalanceItem(
                    ticker=target_position.ticker,
                    name=target_position.name,
                    current_weight=0.0,
                    target_weight=target_position.weight,
                    action=action,
                )
            )

        return plan
