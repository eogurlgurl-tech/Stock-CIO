"""
Test MarketAnalyzer

Stock-CIO
"""

from datetime import datetime

from src.analyzers.market_analyzer import MarketAnalyzer
from src.models.market_snapshot import MarketSnapshot


def create_market(
    kospi_change: float | None = None,
    kosdaq_change: float | None = None,
) -> MarketSnapshot:
    """Create test market snapshot."""

    return MarketSnapshot(
        market="TEST",
        timestamp=datetime.now(),

        kospi=3000,
        kosdaq=800,

        kospi_change=kospi_change,
        kosdaq_change=kosdaq_change,

        dow=0,
        sp500=0,
        nasdaq=0,
        sox=0,
        vix=20,
        usdkrw=1350,
    )


def test_market_score_positive():
    """Strong Korea market should produce high score."""

    analyzer = MarketAnalyzer()

    market = create_market(
        kospi_change=2.5,
        kosdaq_change=2.2,
    )

    score = analyzer.analyze(market)

    assert score == 100


def test_market_score_negative():
    """Weak Korea market should produce low score."""

    analyzer = MarketAnalyzer()

    market = create_market(
        kospi_change=-2.0,
        kosdaq_change=-2.0,
    )

    score = analyzer.analyze(market)

    assert score == 20


def test_market_score_none():
    """None values should return neutral score."""

    analyzer = MarketAnalyzer()

    market = create_market()

    score = analyzer.analyze(market)

    assert score == 50


def test_market_score_is_numeric():
    """Return type should be numeric."""

    analyzer = MarketAnalyzer()

    market = create_market()

    score = analyzer.analyze(market)

    assert isinstance(score, (int, float))