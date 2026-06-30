"""
Test MacroAnalyzer

Stock-CIO
"""

from datetime import datetime

from src.analyzers.macro_analyzer import MacroAnalyzer
from src.models.market_snapshot import MarketSnapshot


def create_market(
    nasdaq_change: float | None = None,
    sp500_change: float | None = None,
    sox_change: float | None = None,
    vix_change: float | None = None,
) -> MarketSnapshot:
    """Create test market snapshot."""

    return MarketSnapshot(
        market="TEST",
        timestamp=datetime.now(),

        kospi=0,
        kosdaq=0,

        dow=0,
        sp500=5500,
        nasdaq=18000,

        sox=5000,
        vix=15,
        usdkrw=1350,

        nasdaq_change=nasdaq_change,
        sp500_change=sp500_change,
        sox_change=sox_change,
        vix_change=vix_change,
    )


def test_macro_score_positive_market():
    """Strong market should produce high score."""

    analyzer = MacroAnalyzer()

    market = create_market(
        nasdaq_change=2.5,
        sp500_change=1.5,
        sox_change=3.0,
        vix_change=-3.0,
    )

    score = analyzer.analyze(market)

    assert score >= 80


def test_macro_score_high_vix():
    """High VIX should reduce score."""

    analyzer = MacroAnalyzer()

    market = create_market(
        nasdaq_change=2.5,
        sp500_change=1.5,
        sox_change=3.0,
        vix_change=6.0,
    )

    score = analyzer.analyze(market)

    assert score < 80


def test_macro_score_is_numeric():
    """Return type should be numeric."""

    analyzer = MacroAnalyzer()

    market = create_market()

    score = analyzer.analyze(market)

    assert isinstance(score, (int, float))