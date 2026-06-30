"""
Core Engine

Stock-CIO
"""

from datetime import datetime

from src.analyzers.macro_analyzer import MacroAnalyzer
from src.analyzers.market_analyzer import MarketAnalyzer
from src.analyzers.score_engine import ScoreEngine
from src.collectors.market_data_loader import MarketDataLoader
from src.core.decision_engine import DecisionEngine
from src.reports.morning_brief import MorningBrief
from src.utils.logger import Logger


class CIOEngine:
    """Main application engine."""

    VERSION = "0.3.0-alpha"

    def __init__(self) -> None:

        self.started_at = datetime.now()

        self.logger = Logger.get_logger()

        # Components
        self.market_loader = MarketDataLoader()

        self.macro_analyzer = MacroAnalyzer()
        self.market_analyzer = MarketAnalyzer()

        self.score_engine = ScoreEngine()
        self.decision_engine = DecisionEngine()

        self.brief = MorningBrief()

        # Shared Context
        self.context: dict = {}

    def initialize(self) -> None:

        self.logger.info("Initialize System")

    def load_data(self) -> None:
        """Load Market Data"""

        print("[2/5] Load Market Data")

        market = self.market_loader.load()

        self.context["market"] = market

        print(f"Market : {market.market}")
        print(f"KOSPI  : {market.kospi}")
        print(f"KOSDAQ : {market.kosdaq}")
        print(f"NASDAQ : {market.nasdaq}")
        print(f"S&P500 : {market.sp500}")
        print(f"SOX    : {market.sox}")
        print(f"VIX    : {market.vix}")

    def analyze(self) -> None:
        """Analyze Market"""

        print("[3/5] Analyze")

        market = self.context["market"]

        # -------------------------
        # Analyzer
        # -------------------------

        macro_score = self.macro_analyzer.analyze(market)
        market_score = self.market_analyzer.analyze(market)

        # -------------------------
        # Score
        # -------------------------

        score = self.score_engine.calculate(
            macro=macro_score,
            market=market_score,
        )

        self.context["score"] = score

        # -------------------------
        # Decision
        # -------------------------

        decision = self.decision_engine.make_decision(score)

        self.context["decision"] = decision

        print()
        print("=" * 50)
        print("Today's CIO Score")
        print("=" * 50)

        print(f"Macro      : {score.macro:.2f}")
        print(f"Market     : {score.market:.2f}")
        print(f"Sector     : {score.sector:.2f}")
        print(f"MoneyFlow  : {score.money_flow:.2f}")
        print(f"News       : {score.news:.2f}")
        print(f"Portfolio  : {score.portfolio:.2f}")
        print(f"Risk       : {score.risk:.2f}")

        print("-" * 50)

        print(f"TOTAL SCORE : {score.total:.2f}")
        print(f"GRADE       : {score.grade}")
        print(f"RATING      : {score.stars}")

        print("=" * 50)

        print()
        print("Today's Decision")
        print("=" * 50)

        print(f"Market Status : {decision.market_status}")
        print(f"Action        : {decision.action}")
        print(f"Cash Ratio    : {decision.cash_ratio}%")
        print(f"Stock Ratio   : {decision.stock_ratio}%")

        print("=" * 50)

    def generate_reports(self) -> None:
        """Generate Morning Brief"""

        print("[4/5] Generate Reports")

        report = self.brief.generate(
            self.context["market"],
            self.context["score"],
            self.context["decision"],
        )

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
        """Start Application"""

        print("=" * 60)
        print("📈 STOCK-CIO")
        print("AI Chief Investment Officer")
        print(f"Version : {self.VERSION}")
        print(f"Started : {self.started_at:%Y-%m-%d %H:%M:%S}")
        print("=" * 60)

        self.initialize()
        self.load_data()
        self.analyze()
        self.generate_reports()
        self.ready()