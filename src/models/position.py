"""
Position Model

Stock-CIO
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    """현재 보유 포지션"""

    ticker: str

    name: str = ""

    quantity: int = 0

    average_price: float = 0.0

    current_price: float = 0.0

    weight: float = 0.0

    @property
    def cost_basis(self) -> float:
        """매입원가"""
        return self.average_price * self.quantity

    @property
    def market_value(self) -> float:
        """현재 평가금액"""
        return self.current_price * self.quantity

    @property
    def unrealized_profit(self) -> float:
        """평가손익"""
        return self.market_value - self.cost_basis

    @property
    def return_rate(self) -> float:
        """평가수익률 (%)"""

        if self.cost_basis == 0:
            return 0.0

        return (
            self.unrealized_profit
            / self.cost_basis
        ) * 100

    @property
    def is_open(self) -> bool:
        """보유 여부"""

        return self.quantity > 0