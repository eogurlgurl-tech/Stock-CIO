"""
Trade Model

Stock-CIO
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Trade:
    """백테스트 거래 정보"""

    ticker: str
    trade_date: datetime
    side: str
    price: float
    quantity: int
    fee: float = 0.0
    realized_profit: float = 0.0

    @property
    def amount(self) -> float:
        """거래 금액"""
        return self.price * self.quantity

    @property
    def total_amount(self) -> float:
        """수수료 포함 거래 금액"""
        return self.amount + self.fee

    @property
    def return_rate(self) -> float:
        """수익률 (%)"""
        if self.amount == 0:
            return 0.0

        return (self.realized_profit / self.amount) * 100