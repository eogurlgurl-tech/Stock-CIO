"""
Unit tests for RecommendationEngine.
"""

from src.constants.risk_level import RiskLevel
from src.models.portfolio import Portfolio
from src.models.risk_report import RiskReport
from src.services.recommendation_engine import RecommendationEngine


class TestRecommendationEngine:

    def setup_method(self):
        self.engine = RecommendationEngine()

    def test_low_risk_recommendation(self):
        portfolio = Portfolio()

        report = RiskReport(
            portfolio_score=92.0,
            concentration_score=100.0,
            diversification_score=100.0,
            cash_score=100.0,
            largest_weight=20.0,
            position_count=5,
            cash_ratio=30.0,
            risk_level=RiskLevel.LOW,
        )

        recommendation = self.engine.generate(
            portfolio,
            report,
        )

        assert recommendation.overall_grade == "A"
        assert recommendation.risk_level == RiskLevel.LOW
        assert (
            recommendation.portfolio_score == 92.0
        )
        assert len(
            recommendation.recommendation_items
        ) == 1

    def test_high_concentration(self):
        portfolio = Portfolio()

        report = RiskReport(
            portfolio_score=55.0,
            concentration_score=30.0,
            diversification_score=75.0,
            cash_score=80.0,
            largest_weight=90.0,
            position_count=3,
            cash_ratio=20.0,
            risk_level=RiskLevel.HIGH,
        )

        recommendation = self.engine.generate(
            portfolio,
            report,
        )

        assert any(
            "Reduce concentration"
            in item
            for item in recommendation.recommendation_items
        )

    def test_diversification(self):
        portfolio = Portfolio()

        report = RiskReport(
            portfolio_score=60.0,
            concentration_score=80.0,
            diversification_score=30.0,
            cash_score=80.0,
            largest_weight=35.0,
            position_count=1,
            cash_ratio=20.0,
            risk_level=RiskLevel.MEDIUM,
        )

        recommendation = self.engine.generate(
            portfolio,
            report,
        )

        assert any(
            "Increase portfolio diversification"
            in item
            for item in recommendation.recommendation_items
        )

    def test_high_cash(self):
        portfolio = Portfolio()

        report = RiskReport(
            portfolio_score=70.0,
            concentration_score=80.0,
            diversification_score=80.0,
            cash_score=60.0,
            largest_weight=30.0,
            position_count=4,
            cash_ratio=80.0,
            risk_level=RiskLevel.MEDIUM,
        )

        recommendation = self.engine.generate(
            portfolio,
            report,
        )

        assert any(
            "Consider investing excess cash"
            in item
            for item in recommendation.recommendation_items
        )

    def test_low_cash(self):
        portfolio = Portfolio()

        report = RiskReport(
            portfolio_score=65.0,
            concentration_score=80.0,
            diversification_score=80.0,
            cash_score=40.0,
            largest_weight=30.0,
            position_count=4,
            cash_ratio=2.0,
            risk_level=RiskLevel.MEDIUM,
        )

        recommendation = self.engine.generate(
            portfolio,
            report,
        )

        assert any(
            "Increase cash reserve"
            in item
            for item in recommendation.recommendation_items
        )

    def test_grade(self):
        assert self.engine._grade(95) == "A"
        assert self.engine._grade(85) == "B"
        assert self.engine._grade(75) == "C"
        assert self.engine._grade(65) == "D"
        assert self.engine._grade(45) == "F"

    def test_summary(self):
        summary = self.engine._summary(
            [
                "First recommendation.",
                "Second recommendation.",
            ]
        )

        assert (
            summary
            == "First recommendation. Second recommendation."
        )