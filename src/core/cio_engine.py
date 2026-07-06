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
from src.core.decision_engine import DecisionEngine
from src.dashboard.dashboard_renderer import DashboardRenderer
from src.reports.morning_brief import MorningBrief
from src.utils.logger import Logger


class CIOEngine:
    """Application Orchestrator."""

    VERSION = "v0.4.0-alpha"

    def __init__(self) -> None:

        self.started_at = datetime.now()

        self.logger = Logger.get_logger()

        # Components
        self.market_loader = MarketDataLoader()
        self.portfolio_loader = PortfolioLoader()

        self.macro_analyzer = MacroAnalyzer()
        self.market_analyzer = MarketAnalyzer()
        self.news_collector = NewsCollector()
        self.news_analyzer = NewsAnalyzer()

        self.score_engine = ScoreEngine()
        self.decision_engine = DecisionEngine()

        self.dashboard = DashboardRenderer()
        self.brief = MorningBrief()

        # Shared Context
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
        """
        Execute portfolio pipeline.

        FEATURE-025
        Portfolio Context를 생성하고 PortfolioLoader를 통해
        현재 Portfolio를 공급한다.
        Target Portfolio 생성 및 Rebalancing은
        향후 Feature에서 연결한다.
        """

        print("[6/8] Portfolio Pipeline")

        portfolio = self.portfolio_loader.load()

        portfolio_context = {
            "portfolio": portfolio,
            "analysis": None,
            "recommendation": None,
            "rebalancing": None,
            "decision": None,
        }

        self.context["portfolio"] = portfolio_context

    def render_dashboard(self) -> None:
        """Render dashboard."""

        print("[7/8] Dashboard")

        dashboard = self.dashboard.render(
            self.context["market"],
            self.context["score"],
            self.context["decision"],
            self.context["news"],
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
            print(f"✔ {key}")

        print("=" * 60)

    def run(self) -> None:
        """Official application entry point."""

        print("=" * 60)
        print("📈 STOCK-CIO")
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