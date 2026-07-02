"""
Unit tests for RiskAnalyzer.
"""

from src.constants.risk_level import RiskLevel
from src.models.portfolio import Portfolio
from src.models.position import Position
from src.services.risk_analyzer import RiskAnalyzer


class TestRiskAnalyzer:

    def setup_method(self):
        self.analyzer = RiskAnalyzer()

    def test_empty_portfolio(self):
        portfolio = Portfolio()

        report = self.analyzer.analyze(portfolio)

        assert report.position_count == 0
        assert report.largest_weight == 0.0
        assert report.cash_ratio == 0.0
        assert report.portfolio_score >= 0

    def test_single_position(self):
        portfolio = Portfolio(
            positions=[
                Position(
                    ticker="005930",
                    quantity=10,
                    average_price=70000,
                    current_price=70000,
                )
            ]
        )

        report = self.analyzer.analyze(portfolio)

        assert report.position_count == 1
        assert report.largest_weight == 100.0
        assert report.concentration_score == 30.0

    def test_diversified_portfolio(self):
        portfolio = Portfolio(
            positions=[
                Position("A", quantity=10, current_price=100),
                Position("B", quantity=10, current_price=100),
                Position("C", quantity=10, current_price=100),
                Position("D", quantity=10, current_price=100),
                Position("E", quantity=10, current_price=100),
            ]
        )

        report = self.analyzer.analyze(portfolio)

        assert report.position_count == 5
        assert report.largest_weight == 20.0
        assert report.concentration_score == 100.0
        assert report.diversification_score == 100.0

    def test_high_concentration(self):
        portfolio = Portfolio(
            positions=[
                Position("A", quantity=90, current_price=100),
                Position("B", quantity=10, current_price=100),
            ]
        )

        report = self.analyzer.analyze(portfolio)

        assert report.largest_weight == 90.0
        assert report.concentration_score == 30.0

    def test_high_cash_ratio(self):
        portfolio = Portfolio(
            cash=9000,
            positions=[
                Position(
                    "A",
                    quantity=10,
                    current_price=100,
                )
            ],
        )

        report = self.analyzer.analyze(portfolio)

        assert report.cash_ratio > 60
        assert report.cash_score == 60.0

    def test_low_cash_ratio(self):
        portfolio = Portfolio(
            cash=100,
            positions=[
                Position(
                    "A",
                    quantity=100,
                    current_price=100,
                )
            ],
        )

        report = self.analyzer.analyze(portfolio)

        assert report.cash_ratio < 5
        assert report.cash_score == 40.0

    def test_risk_level_classification(self):
        portfolio = Portfolio(
            positions=[
                Position("A", quantity=10, current_price=100),
                Position("B", quantity=10, current_price=100),
                Position("C", quantity=10, current_price=100),
                Position("D", quantity=10, current_price=100),
                Position("E", quantity=10, current_price=100),
            ],
            cash=2500,
        )

        report = self.analyzer.analyze(portfolio)

        assert report.risk_level == RiskLevel.LOW