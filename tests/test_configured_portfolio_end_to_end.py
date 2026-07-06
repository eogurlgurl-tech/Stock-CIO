"""
Configured Portfolio End-to-End Test

Feature : FEATURE-027
Module  : Portfolio Data Integration
"""

from pathlib import Path

from src.collectors.portfolio_loader import PortfolioLoader
from src.constants.decision_type import DecisionType
from src.core.cio_engine import CIOEngine
from src.strategies.equal_weight_strategy import EqualWeightStrategy


class EndToEndPortfolioConfig:
    """Return a configured portfolio mapping."""

    def load(self, name: str) -> dict:
        """Return portfolio configuration."""

        assert name == "portfolio"

        return {
            "cash": 100.0,
            "positions": [
                {
                    "ticker": "AAA",
                    "name": "Alpha",
                    "quantity": 3,
                    "average_price": 90.0,
                    "current_price": 100.0,
                },
                {
                    "ticker": "BBB",
                    "name": "Beta",
                    "quantity": 1,
                    "average_price": 110.0,
                    "current_price": 100.0,
                },
            ],
        }


class EndToEndDashboard:
    """Return the market dashboard section."""

    def render(self, *args) -> str:
        """Return predefined market output."""

        return "MARKET DASHBOARD"


class EndToEndMorningBrief:
    """Create a temporary Morning Brief."""

    def __init__(self, report_path: Path) -> None:
        self._report_path = report_path

    def generate(self, *args) -> Path:
        """Create the base report."""

        self._report_path.write_text(
            "# Market\n",
            encoding="utf-8",
        )
        return self._report_path


def test_configured_portfolio_reaches_all_outputs(tmp_path):
    """Configured positions reach decision and output layers."""

    report_path = tmp_path / "brief.md"
    engine = CIOEngine()
    engine.portfolio_loader = PortfolioLoader(
        EndToEndPortfolioConfig()
    )
    engine.target_portfolio_builder.set_strategy(
        EqualWeightStrategy()
    )
    engine.dashboard = EndToEndDashboard()
    engine.brief = EndToEndMorningBrief(report_path)
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
    engine.generate_morning_brief()

    context = engine.context["portfolio"]
    portfolio = context["portfolio"]
    report = report_path.read_text(encoding="utf-8")

    assert portfolio.cash == 100.0
    assert len(portfolio.positions) == 2
    assert portfolio.positions[0].weight == 75.0
    assert portfolio.positions[1].weight == 25.0
    assert context["decision"].decision == DecisionType.SELL
    assert "Positions       : 2" in engine.context["dashboard"]
    assert "Decision        : SELL" in engine.context["dashboard"]
    assert "| Positions | 2 |" in report
    assert "| Decision | SELL |" in report
