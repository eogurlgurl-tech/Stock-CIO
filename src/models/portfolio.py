"""
Portfolio Model

Stock-CIO
"""

from dataclasses import dataclass, field

from .position import Position


@dataclass(slots=True)
class Portfolio:
    """포트폴리오"""

    cash: float = 0.0

    positions: list[Position] = field(
        default_factory=list
    )

    @property
    def stock_asset(self) -> float:
        """주식 평가금액"""

        return sum(
            position.market_value
            for position in self.positions
        )

    @property
    def total_asset(self) -> float:
        """총 자산"""

        return self.cash + self.stock_asset

    @property
    def cash_ratio(self) -> float:
        """현금 비중 (%)"""

        if self.total_asset == 0:
            return 0.0

        return (
            self.cash
            / self.total_asset
        ) * 100

    @property
    def stock_ratio(self) -> float:
        """주식 비중 (%)"""

        if self.total_asset == 0:
            return 0.0

        return (
            self.stock_asset
            / self.total_asset
        ) * 100

    @property
    def total_profit(self) -> float:
        """총 평가손익"""

        return sum(
            position.unrealized_profit
            for position in self.positions
        )

    @property
    def total_profit_rate(self) -> float:
        """총 평가수익률 (%)"""

        invested = sum(
            position.cost_basis
            for position in self.positions
        )

        if invested == 0:
            return 0.0

        return (
            self.total_profit
            / invested
        ) * 100

    @property
    def is_empty(self) -> bool:
        """보유 종목 여부"""

        return len(self.positions) == 0