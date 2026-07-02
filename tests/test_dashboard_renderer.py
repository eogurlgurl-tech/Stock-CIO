"""
Dashboard Renderer Tests

Stock-CIO
"""

from datetime import datetime

from src.dashboard.dashboard_renderer import DashboardRenderer
from src.models.cio_decision import CIODecision
from src.models.market_snapshot import MarketSnapshot
from src.models.news import News
from src.models.score import Score


def test_dashboard_renderer():
    """Dashboard Renderer Test"""

    renderer = DashboardRenderer()

    market = MarketSnapshot(
        market="GLOBAL",
        timestamp=datetime.now(),
        kospi=3200.25,
        kosdaq=810.15,
        nasdaq=20123.45,
        sp500=6123.55,
        sox=5400.10,
        vix=18.20,
    )

    score = Score(
        macro=80,
        market=75,
        sector=70,
        money_flow=65,
        news=60,
        portfolio=80,
        risk=20,
        total=75,
        grade="A",
        stars="★★★★☆",
    )

    decision = CIODecision(
        market_status="BULLISH",
        action="BUY",
        cash_ratio=30,
        stock_ratio=70,
        watch_list=[
            "AI",
            "Semiconductor",
            "Battery",
        ],
    )

    news_list = [
        News(
            title="NVIDIA hits new high",
            source="Reuters",
            published_at="2026-07-02",
        ),
        News(
            title="Fed keeps rates unchanged",
            source="Bloomberg",
            published_at="2026-07-02",
        ),
        News(
            title="TSMC expands AI production",
            source="CNBC",
            published_at="2026-07-02",
        ),
    ]

    dashboard = renderer.render(
        market,
        score,
        decision,
        news_list,
    )

    assert "STOCK-CIO DASHBOARD" in dashboard
    assert "MARKET" in dashboard
    assert "CIO SCORE" in dashboard
    assert "DECISION" in dashboard
    assert "WATCH LIST" in dashboard
    assert "TOP NEWS" in dashboard

    assert "BUY" in dashboard
    assert "75.00" in dashboard
    assert "★★★★☆" in dashboard
    assert "NVIDIA hits new high" in dashboard