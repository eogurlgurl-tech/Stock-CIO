"""
Core Engine

Stock-CIO
"""

from datetime import datetime

from src.analyzers.macro_analyzer import MacroAnalyzer
from src.analyzers.market_analyzer import MarketAnalyzer
from src.analyzers.news_analyzer import NewsAnalyzer
from src.analyzers.score_engine import ScoreEngine
from src.collectors.market_data_loader import MarketDataLoader
from src.collectors.news_collector import NewsCollector
from src.collectors.portfolio_loader import PortfolioLoader
from src.core.decision_engine import DecisionEngine as MarketDecisionEngine
from src.core.portfolio_optimizer import PortfolioOptimizer
from src.dashboard.dashboard_renderer import DashboardRenderer
from src.dashboard.portfolio_dashboard_renderer import (
    PortfolioDashboardRenderer,
)
from src.models.cio_decision import CIODecision
from src.reports.morning_brief import MorningBrief
from src.reports.portfolio_morning_brief_appender import (
    PortfolioMorningBriefAppender,
)
from src.services.decision_engine import (
    DecisionEngine as PortfolioDecisionEngine,
)
from src.services.rebalancing_engine import RebalancingEngine
from src.services.rebalancing_recommendation_engine import (
    RebalancingRecommendationEngine,
)
from src.services.recommendation_engine import RecommendationEngine
from src.services.risk_analyzer import RiskAnalyzer
from src.services.target_portfolio_builder import (
    TargetPortfolioBuilder,
)
from src.services.unified_decision_engine import (
    UnifiedDecisionEngine,
)
from src.utils.logger import Logger
from src.services.price_updater import update_portfolio_prices


class CIOEngine:
    """Application Orchestrator."""

    VERSION = "v1.0.0-rc"

    def __init__(self) -> None:
        self.started_at = datetime.now()
        self.logger = Logger.get_logger()

        self.market_loader = MarketDataLoader()
        self.portfolio_loader = PortfolioLoader()

        self.macro_analyzer = MacroAnalyzer()
        self.market_analyzer = MarketAnalyzer()
        self.news_collector = NewsCollector()
        self.news_analyzer = NewsAnalyzer()

        self.score_engine = ScoreEngine()
        self.decision_engine = MarketDecisionEngine()

        self.portfolio_optimizer = PortfolioOptimizer()
        self.target_portfolio_builder = TargetPortfolioBuilder()
        self.risk_analyzer = RiskAnalyzer()
        self.recommendation_engine = RecommendationEngine()
        self.rebalancing_engine = RebalancingEngine()
        self.rebalancing_recommendation_engine = (
            RebalancingRecommendationEngine()
        )
        self.portfolio_decision_engine = PortfolioDecisionEngine()
        self.unified_decision_engine = UnifiedDecisionEngine()

        self.dashboard = DashboardRenderer()
        self.portfolio_dashboard = PortfolioDashboardRenderer()
        self.brief = MorningBrief()
        self.portfolio_brief = PortfolioMorningBriefAppender()

        self.context: dict = {}

    def initialize(self) -> None:
        """Initialize application."""

        self.logger.info("Initialize System")

    def load_market_data(self) -> None:
        """Load market data."""

        print("[2/8] Load Market Data")

        market = self.market_loader.load()
        self.context["market"] = market

        print(f"Market : {market.market}")
        print(f"KOSPI  : {market.kospi}")
        print(f"KOSDAQ : {market.kosdaq}")
        print(f"NASDAQ : {market.nasdaq}")
        print(f"S&P500 : {market.sp500}")
        print(f"SOX    : {market.sox}")
        print(f"VIX    : {market.vix}")

    def analyze_market(self) -> None:
        """Run market analyzers."""

        print("[3/8] Market Analyze")

        market = self.context["market"]

        macro_score = self.macro_analyzer.analyze(market)
        market_score = self.market_analyzer.analyze(market)

        news_list = self.news_collector.collect()
        news_score = self.news_analyzer.analyze(news_list)

        self.context["news"] = news_list
        self.context["macro_score"] = macro_score
        self.context["market_score"] = market_score
        self.context["news_score"] = news_score

    def calculate_score(self) -> None:
        """Calculate integrated market score."""

        print("[4/8] Score Calculate")

        score = self.score_engine.calculate(
            macro=self.context["macro_score"],
            market=self.context["market_score"],
            news=self.context["news_score"],
        )

        self.context["score"] = score

    def make_market_decision(self) -> None:
        """Generate market decision."""

        print("[5/8] Market Decision")

        decision = self.decision_engine.make_decision(
            self.context["score"],
        )

        self.context["decision"] = decision

    def run_portfolio_pipeline(self) -> None:
        """Execute the complete portfolio workflow."""

        print("[6/8] Portfolio Pipeline")

        portfolio = self.portfolio_loader.load()
        self.portfolio_optimizer.update_weights(portfolio)

        target = self.target_portfolio_builder.build(portfolio)
        risk_report = self.risk_analyzer.analyze(portfolio)

        recommendation = self.recommendation_engine.generate(
            portfolio,
            risk_report,
        )

        rebalancing_plan = self.rebalancing_engine.create_plan(
            current=portfolio,
            target=target,
        )

        rebalancing_recommendations = (
            self.rebalancing_recommendation_engine
            .generate_from_plan(rebalancing_plan)
        )

        portfolio_decision = (
            self.portfolio_decision_engine.generate(
                recommendation,
                rebalancing_recommendations,
            )
        )

        market_decision = self.context.get("decision")

        if not isinstance(market_decision, CIODecision):
            market_decision = CIODecision()

        unified_decision = self.unified_decision_engine.generate(
            market_decision,
            portfolio_decision,
        )

        self.context["portfolio"] = {
            "portfolio": portfolio,
            "target": target,
            "analysis": risk_report,
            "recommendation": recommendation,
            "rebalancing": rebalancing_plan,
            "rebalancing_recommendations": (
                rebalancing_recommendations
            ),
            "decision": portfolio_decision,
            "unified_decision": unified_decision,
        }

    def render_dashboard(self) -> None:
        """Render dashboard."""

        print("[7/8] Dashboard")

        # Refresh live prices for portfolio positions before rendering
        portfolio_context = self.context.get("portfolio")
        if portfolio_context:
            update_portfolio_prices(
                portfolio_context["portfolio"]
            )

        dashboard = self.dashboard.render(
            self.context["market"],
            self.context["score"],
            self.context["decision"],
            self.context["news"],
        )

        portfolio_context = self.context["portfolio"]
        portfolio_dashboard = self.portfolio_dashboard.render(
            portfolio_context["portfolio"],
            portfolio_context["analysis"],
            portfolio_context["decision"],
            portfolio_context["rebalancing"],
            portfolio_context["unified_decision"],
        )

        dashboard = (
            f"{dashboard}\n\n"
            f"{portfolio_dashboard}"
        )

        self.context["dashboard"] = dashboard

        print()
        print(dashboard)

    def generate_morning_brief(self) -> None:
        """Generate morning brief."""

        print("[8/8] Morning Brief")

        report = self.brief.generate(
            self.context["market"],
            self.context["score"],
            self.context["decision"],
            self.context["news"],
        )

        portfolio_context = self.context["portfolio"]
        self.portfolio_brief.append(
            report,
            portfolio_context["portfolio"],
            portfolio_context["analysis"],
            portfolio_context["decision"],
            portfolio_context["rebalancing"],
            portfolio_context["unified_decision"],
        )

        self.context["report"] = report

        print(f"Report Saved : {report}")

    def ready(self) -> None:
        """Application ready."""

        self.logger.info("System Ready")

        print()
        print("=" * 60)
        print("System Context")
        print("=" * 60)

        for key in self.context:
            print(f"- {key}")

        print("=" * 60)

    def run(self) -> None:
        """Official application entry point."""

        print("=" * 60)
        print("STOCK-CIO")
        print("AI Chief Investment Officer")
        print(f"Version : {self.VERSION}")
        print(f"Started : {self.started_at:%Y-%m-%d %H:%M:%S}")
        print("=" * 60)

        self.initialize()
        self.load_market_data()
        self.analyze_market()
        self.calculate_score()
        self.make_market_decision()
        self.run_portfolio_pipeline()
        self.render_dashboard()
        self.generate_morning_brief()
        self.ready()

    def start(self) -> None:
        """Backward compatible entry point."""

        self.run()
