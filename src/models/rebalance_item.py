"""
Rebalance Item Model

Stock-CIO
"""

from dataclasses import dataclass

from src.constants.rebalance_action import RebalanceAction


@dataclass(slots=True)
class RebalanceItem:
    """Single rebalancing item"""

    ticker: str

    name: str = ""

    current_weight: float = 0.0

    target_weight: float = 0.0

    action: RebalanceAction = RebalanceAction.HOLD

    @property
    def difference(self) -> float:
        """
        Target - Current (%)
        """

        return (
            self.target_weight
            - self.current_weight
        )

    @property
    def abs_difference(self) -> float:
        """
        Absolute difference (%)
        """

        return abs(self.difference)

    @property
    def needs_rebalance(self) -> bool:
        """
        Whether rebalancing is required.
        """

        return self.action != RebalanceAction.HOLD