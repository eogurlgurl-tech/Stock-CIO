"""
Integration Tests for Portfolio Output

Feature : FEATURE-026
Module  : CIO Engine Output
"""

from pathlib import Path

from src.core.cio_engine import CIOEngine
from src.models.portfolio import Portfolio


class EmptyPortfolioLoader:
    """Return an empty portfolio."""

    def load(self) -> Portfolio:
        """Return an empty portfolio."""

        return Portfolio()


class DashboardStub:
    """Return a predefined market dashboard."""

    def render(self, *args) -> str:
        """Return dashboard text."""

        return "MARKET DASHBOARD"


class MorningBriefStub:
    """Create a predefined Morning Brief."""

    def __init__(self, report_path: Path) -> None:
        self._report_path = report_path

    def generate(self, *args) -> Path:
        """Create and return the report path."""

        self._report_path.write_text(
            "# Market\n",
            encoding="utf-8",
        )
        return self._report_path


def test_dashboard_contains_portfolio_section():
    """Rendered dashboard includes portfolio results."""

    engine = CIOEngine()
    engine.portfolio_loader = EmptyPortfolioLoader()
    engine.dashboard = DashboardStub()
    engine.context.update(
        {
            "market": object(),
            "score": object(),
            "decision": object(),
            "news": [],
        }
    )
    engine.run_portfolio_pipeline()

    engine.render_dashboard()

    assert "MARKET DASHBOARD" in engine.context["dashboard"]
    assert "PORTFOLIO" in engine.context["dashboard"]


def test_morning_brief_contains_portfolio_section(tmp_path):
    """Generated Morning Brief includes portfolio results."""

    report_path = tmp_path / "brief.md"
    engine = CIOEngine()
    engine.portfolio_loader = EmptyPortfolioLoader()
    engine.brief = MorningBriefStub(report_path)
    engine.context.update(
        {
            "market": object(),
            "score": object(),
            "decision": object(),
            "news": [],
        }
    )
    engine.run_portfolio_pipeline()

    engine.generate_morning_brief()

    content = report_path.read_text(encoding="utf-8")
    assert "# Market" in content
    assert "# Portfolio" in content
