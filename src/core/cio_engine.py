"""
Core Engine

Stock-CIO
"""

from datetime import datetime

from analyzers.score_engine import ScoreEngine
from collectors.market_data_loader import MarketDataLoader
from reports.morning_brief import MorningBrief
from utils.logger import Logger


class CIOEngine:
    """Main application engine."""

    VERSION = "0.2.0-alpha"

    def __init__(self) -> None:
        self.started_at = datetime.now()

        self.logger = Logger.get_logger()

        # Components
        self.market_loader = MarketDataLoader()
        self.score_engine = ScoreEngine()
        self.brief = MorningBrief()

        # Shared Context
        self.context = {}

    def initialize(self) -> None:
        self.logger.info("Initialize System")

    def load_data(self):
        """Load market data only once."""

        print("[2/5] Load Market Data")

        market = self.market_loader.load()

        self.context["market"] = market

        print(f"Market : {market.market}")
        print(f"KOSPI  : {market.kospi}")
        print(f"NASDAQ : {market.nasdaq}")
        print(f"S&P500 : {market.sp500}")
        print(f"VIX    : {market.vix}")

    def analyze(self) -> None:
        """Analyze Market"""

        print("[3/5] Analyze")

        market = self.context["market"]

        score = self.score_engine.calculate(market)

        self.context["score"] = score

        print()
        print("=" * 45)
        print("Today's CIO Score")
        print("=" * 45)

        print(f"Macro      : {score.macro}")
        print(f"Sector     : {score.sector}")
        print(f"MoneyFlow  : {score.money_flow}")
        print(f"News       : {score.news}")
        print(f"Portfolio  : {score.portfolio}")
        print(f"Risk       : {score.risk}")

        print("-" * 45)

        print(f"TOTAL SCORE : {score.total}")

        print("=" * 45)

    def generate_reports(self) -> None:
        """Generate Morning Brief"""

        print("[4/5] Generate Reports")

        market = self.context["market"]

        report = self.brief.generate(market)

        self.context["report"] = report

        print(f"Report Saved : {report}")

    def ready(self) -> None:
        self.logger.info("System Ready")

        print()
        print("=" * 60)
        print("System Context")
        print("=" * 60)

        for key in self.context:
            print(f"✔ {key}")

        print("=" * 60)

    def start(self) -> None:
        """Start application."""

        print("=" * 60)
        print("📈 Stock-CIO")
        print("AI Chief Investment Officer System")
        print(f"Version : {self.VERSION}")
        print(f"Started : {self.started_at:%Y-%m-%d %H:%M:%S}")
        print("=" * 60)

        self.initialize()
        self.load_data()
        self.analyze()
        self.generate_reports()
        self.ready()