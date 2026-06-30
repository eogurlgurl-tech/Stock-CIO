"""
Portfolio Model

Stock-CIO
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class Position:
    """보유 종목"""

    ticker: str
    name: str

    quantity: int

    average_price: float
    current_price: float

    weight: float = 0.0

    @property
    def amount(self) -> float:
        """평가금액"""
        return self.quantity * self.current_price

    @property
    def profit(self) -> float:
        """평가손익"""
        return (
            self.current_price - self.average_price
        ) * self.quantity

    @property
    def profit_rate(self) -> float:
        """수익률 (%)"""

        if self.average_price == 0:
            return 0.0

        return (
            (self.current_price - self.average_price)
            / self.average_price
        ) * 100


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
            position.amount
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

        return self.cash / self.total_asset * 100

    @property
    def stock_ratio(self) -> float:
        """주식 비중 (%)"""

        if self.total_asset == 0:
            return 0.0

        return self.stock_asset / self.total_asset * 100

    @property
    def total_profit(self) -> float:
        """총 평가손익"""

        return sum(
            position.profit
            for position in self.positions
        )

    @property
    def total_profit_rate(self) -> float:
        """총 수익률 (%)"""

        invested = sum(
            position.average_price * position.quantity
            for position in self.positions
        )

        if invested == 0:
            return 0.0

        return (
            self.total_profit / invested
        ) * 100