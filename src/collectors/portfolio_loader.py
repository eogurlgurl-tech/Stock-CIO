"""
Portfolio Loader

Stock-CIO
"""

from src.models.portfolio import Portfolio


class PortfolioLoader:
    """Portfolio Loader."""

    def load(self) -> Portfolio:
        """
        Load portfolio.

        Returns
        -------
        Portfolio
            Current portfolio.
        """

        return Portfolio()