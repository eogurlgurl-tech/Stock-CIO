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

    @property
    def grade(self) -> str:
        """투자 등급"""

        if self.total >= 90:
            return "S"
        elif self.total >= 80:
            return "A"
        elif self.total >= 70:
            return "B"
        elif self.total >= 60:
            return "C"
        else:
            return "D"

    @property
    def stars(self) -> str:
        """별점"""

        if self.total >= 90:
            return "★★★★★"
        elif self.total >= 80:
            return "★★★★☆"
        elif self.total >= 70:
            return "★★★☆☆"
        elif self.total >= 60:
            return "★★☆☆☆"
        else:
            return "★☆☆☆☆"