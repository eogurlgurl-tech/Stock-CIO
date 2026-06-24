"""
Score Model

Stock-CIO
"""

from dataclasses import dataclass


@dataclass
class Score:

    macro: int = 0
    sector: int = 0
    money_flow: int = 0
    news: int = 0
    portfolio: int = 0
    risk: int = 0

    @property
    def total(self) -> int:
        """최종 CIO Score"""

        return (
            self.macro
            + self.sector
            + self.money_flow
            + self.news
            + self.portfolio
            - self.risk
        )