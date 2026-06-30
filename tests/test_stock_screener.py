"""
Test StockScreener

Stock-CIO
"""

from src.analyzers.stock_screener import StockScreener
from src.models.score import Score


def create_score(total: float) -> Score:
    """Create test score."""

    score = Score()
    score.total = total

    return score


def test_strong_bull_market():
    """80+ should recommend AI/Semiconductor."""

    screener = StockScreener()

    result = screener.screen(create_score(90))

    assert "AI" in result.top_sectors
    assert "Semiconductor" in result.top_sectors
    assert "Samsung Electronics" in result.watch_list
    assert len(result.top_sectors) == 4
    assert len(result.watch_list) == 5


def test_neutral_market():
    """60~79 should recommend balanced sectors."""

    screener = StockScreener()

    result = screener.screen(create_score(70))

    assert "Healthcare" in result.top_sectors
    assert "Samsung Electronics" in result.watch_list
    assert len(result.top_sectors) == 4
    assert len(result.watch_list) == 5


def test_defensive_market():
    """Below 60 should recommend defensive assets."""

    screener = StockScreener()

    result = screener.screen(create_score(40))

    assert "Utilities" in result.top_sectors
    assert "KODEX 200" in result.watch_list
    assert len(result.top_sectors) == 4
    assert len(result.watch_list) == 3


def test_result_has_required_fields():
    """ScreenResult should expose required attributes."""

    screener = StockScreener()

    result = screener.screen(create_score(90))

    assert hasattr(result, "top_sectors")
    assert hasattr(result, "watch_list")


def test_return_type():
    """Returned collections should be list."""

    screener = StockScreener()

    result = screener.screen(create_score(90))

    assert isinstance(result.top_sectors, list)
    assert isinstance(result.watch_list, list)