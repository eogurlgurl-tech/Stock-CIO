"""
Core Engine

Stock-CIO
"""
from analyzers.score_engine import ScoreEngine

from reports.morning_brief import MorningBrief

from utils.logger import Logger

from datetime import datetime

from collectors.market_data_loader import MarketDataLoader


class CIOEngine:
    """Main application engine."""

    VERSION = "0.1.0-alpha"

    def __init__(self) -> None:
        self.started_at = datetime.now()

        self.logger = Logger.get_logger()
          
        # MarketDataLoader는 프로그램 시작 시 한 번만 생성
        self.market_loader = MarketDataLoader()

        self.brief = MorningBrief()

        self.score_engine = ScoreEngine()

    def initialize(self) -> None:
        self.logger.info("Initialize System")

    def load_data(self):
        """Load market data."""

        print("[2/5] Load Market Data")

        market = self.market_loader.load()

        print(f"Market : {market.market}")
        print(f"KOSPI  : {market.kospi}")
        print(f"NASDAQ : {market.nasdaq}")
        print(f"S&P500 : {market.sp500}")
        print(f"VIX    : {market.vix}")

        return market

    def analyze(self) -> None:
        """Analyze Market"""

        print("[3/5] Analyze")

        market = self.market_loader.load()

        score = self.score_engine.calculate(market)

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
        """Generate reports."""

        print("[4/5] Generate Reports")

        market = self.market_loader.load()

        report = self.brief.generate(market)

        print(f"Report Saved : {report}")

    def ready(self) -> None:
        self.logger.info("System Ready")

    def start(self) -> None:
        """Start application."""

        print("=" * 60)
        print("📈 Stock-CIO")
        print("AI Chief Investment Officer System")
        print(f"Version : {self.VERSION}")
        print(f"Started : {self.started_at:%Y-%m-%d %H:%M:%S}")
        print("=" * 60)

        # 시장 데이터 읽기
        market = self.load_data()

        # 이후 단계
        self.initialize()
        self.analyze()
        self.generate_reports()
        self.ready()