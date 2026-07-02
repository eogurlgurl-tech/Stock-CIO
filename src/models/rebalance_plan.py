"""
Rebalance Plan Model

Stock-CIO
"""

from dataclasses import dataclass, field

from src.constants.rebalance_action import RebalanceAction
from src.models.rebalance_item import RebalanceItem


@dataclass(slots=True)
class RebalancePlan:
    """Portfolio Rebalancing Plan"""

    items: list[RebalanceItem] = field(
        default_factory=list
    )

    @property
    def buy_items(self) -> list[RebalanceItem]:
        """BUY 대상"""

        return [
            item
            for item in self.items
            if item.action == RebalanceAction.BUY
        ]

    @property
    def sell_items(self) -> list[RebalanceItem]:
        """SELL 대상"""

        return [
            item
            for item in self.items
            if item.action == RebalanceAction.SELL
        ]

    @property
    def hold_items(self) -> list[RebalanceItem]:
        """HOLD 대상"""

        return [
            item
            for item in self.items
            if item.action == RebalanceAction.HOLD
        ]

    @property
    def buy_count(self) -> int:
        """BUY 종목 수"""

        return len(self.buy_items)

    @property
    def sell_count(self) -> int:
        """SELL 종목 수"""

        return len(self.sell_items)

    @property
    def hold_count(self) -> int:
        """HOLD 종목 수"""

        return len(self.hold_items)

    @property
    def rebalance_count(self) -> int:
        """리밸런싱 대상 종목 수"""

        return (
            self.buy_count
            + self.sell_count
        )

    @property
    def needs_rebalance(self) -> bool:
        """리밸런싱 필요 여부"""

        return self.rebalance_count > 0

    def add_item(
        self,
        item: RebalanceItem,
    ) -> None:
        """Rebalance Item 추가"""

        self.items.append(item)