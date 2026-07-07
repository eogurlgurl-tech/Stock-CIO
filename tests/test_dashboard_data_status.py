"""
Unit Tests for Dashboard Data Status

Module : Dashboard Renderer
"""

from datetime import datetime

from src.dashboard.dashboard_renderer import DashboardRenderer
from src.models.cio_decision import CIODecision
from src.models.market_snapshot import MarketSnapshot
from src.models.news import News
from src.models.score import Score


def test_dashboard_displays_data_collection_status():
    """Market and news data status are visible."""

    output = DashboardRenderer().render(
        MarketSnapshot(
            market="GLOBAL",
            timestamp=datetime(2026, 7, 7, 8, 0, 0),
            kospi=3000.0,
            kosdaq=900.0,
            nasdaq=20000.0,
            sp500=6000.0,
            vix=15.0,
        ),
        Score(),
        CIODecision(),
        [
            News(
                title="Headline",
                source="Source",
                published_at="2026-07-07",
            )
        ],
    )

    assert "Analysis Time  : 2026-07-07 08:00:00" in output
    assert "Korea Market   : AVAILABLE" in output
    assert "US Market      : AVAILABLE" in output
    assert "News           : AVAILABLE" in output
