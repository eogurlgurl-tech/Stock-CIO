"""
Unit tests for RebalancingRecommendationEngine.
"""

from src.constants.rebalancing_action import (
    RebalancingAction,
)
from src.constants.risk_level import RiskLevel
from src.models.portfolio import Portfolio
from src.models.position import Position
from src.models.risk_report import RiskReport
from src.services.rebalancing_recommendation_engine import (
    RebalancingRecommendationEngine,
)


class TestRebalancingRecommendationEngine:

    def setup_method(self):
        self.engine = (
            RebalancingRecommendationEngine()
        )

    def test_empty_portfolio(self):
        portfolio = Portfolio()

        report = RiskReport(
            portfolio_score=100.0,
            concentration_score=100.0,
            diversification_score=100.0,
            cash_score=100.0,
            largest_weight=0.0,
            position_count=0,
            cash_ratio=100.0,
            risk_level=RiskLevel.LOW,
        )

        recommendations = self.engine.generate(
            portfolio,
            report,
        )

        assert recommendations == []

    def test_sell_recommendation(self):
        portfolio = Portfolio(
            positions=[
                Position(
                    ticker="AAPL",
                    weight=70.0,
                ),
                Position(
                    ticker="MSFT",
                    weight=30.0,
                ),
            ]
        )

        report = RiskReport(
            portfolio_score=55.0,
            concentration_score=30.0,
            diversification_score=75.0,
            cash_score=80.0,
            largest_weight=70.0,
            position_count=2,
            cash_ratio=20.0,
            risk_level=RiskLevel.HIGH,
        )

        recommendations = self.engine.generate(
            portfolio,
            report,
        )

        sell = next(
            item
            for item in recommendations
            if item.ticker == "AAPL"
        )

        assert (
            sell.action
            == RebalancingAction.SELL
        )

        assert (
            "Reduce concentration"
            in sell.reason
        )

    def test_buy_recommendation(self):
        portfolio = Portfolio(
            positions=[
                Position(
                    ticker="AAPL",
                    weight=15.0,
                ),
                Position(
                    ticker="MSFT",
                    weight=85.0,
                ),
            ]
        )

        report = RiskReport(
            portfolio_score=70.0,
            concentration_score=80.0,
            diversification_score=80.0,
            cash_score=60.0,
            largest_weight=85.0,
            position_count=2,
            cash_ratio=80.0,
            risk_level=RiskLevel.MEDIUM,
        )

        recommendations = self.engine.generate(
            portfolio,
            report,
        )

        buy = next(
            item
            for item in recommendations
            if item.ticker == "AAPL"
        )

        assert (
            buy.action
            == RebalancingAction.BUY
        )

        assert (
            "Utilize excess cash"
            in buy.reason
        )

    def test_hold_recommendation(self):
        portfolio = Portfolio(
            positions=[
                Position(
                    ticker="AAPL",
                    weight=40.0,
                ),
                Position(
                    ticker="MSFT",
                    weight=35.0,
                ),
                Position(
                    ticker="GOOGL",
                    weight=25.0,
                ),
            ]
        )

        report = RiskReport(
            portfolio_score=90.0,
            concentration_score=100.0,
            diversification_score=100.0,
            cash_score=100.0,
            largest_weight=40.0,
            position_count=3,
            cash_ratio=30.0,
            risk_level=RiskLevel.LOW,
        )

        recommendations = self.engine.generate(
            portfolio,
            report,
        )

        assert all(
            item.action
            == RebalancingAction.HOLD
            for item in recommendations
        )

    def test_reason_for_hold(self):
        portfolio = Portfolio(
            positions=[
                Position(
                    ticker="AAPL",
                    weight=50.0,
                ),
            ]
        )

        report = RiskReport(
            portfolio_score=90.0,
            concentration_score=100.0,
            diversification_score=100.0,
            cash_score=100.0,
            largest_weight=50.0,
            position_count=1,
            cash_ratio=30.0,
            risk_level=RiskLevel.LOW,
        )

        recommendations = self.engine.generate(
            portfolio,
            report,
        )

        assert (
            recommendations[0].reason
            == "Current allocation is appropriate."
        )

    def test_recommendation_count(self):
        portfolio = Portfolio(
            positions=[
                Position(
                    ticker="AAA",
                    weight=50.0,
                ),
                Position(
                    ticker="BBB",
                    weight=30.0,
                ),
                Position(
                    ticker="CCC",
                    weight=20.0,
                ),
            ]
        )

        report = RiskReport(
            portfolio_score=80.0,
            concentration_score=80.0,
            diversification_score=90.0,
            cash_score=100.0,
            largest_weight=50.0,
            position_count=3,
            cash_ratio=20.0,
            risk_level=RiskLevel.MEDIUM,
        )

        recommendations = self.engine.generate(
            portfolio,
            report,
        )

        assert len(recommendations) == 3