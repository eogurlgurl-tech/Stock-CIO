"""
News Analyzer Tests

Stock-CIO
"""

from src.analyzers.news_analyzer import NewsAnalyzer
from src.models.news import News


class TestNewsAnalyzer:

    def setup_method(self):

        self.analyzer = NewsAnalyzer()

    def test_empty_news_returns_default_score(self):

        score = self.analyzer.analyze([])

        assert score == 50.0

    def test_positive_news(self):

        news = [
            News(
                title="NVIDIA AI Growth",
                source="Reuters",
                published_at="2026-06-30",
                sentiment=0.8,
                importance=5,
            )
        ]

        score = self.analyzer.analyze(news)

        assert score > 80

    def test_negative_news(self):

        news = [
            News(
                title="Market Crash",
                source="Reuters",
                published_at="2026-06-30",
                sentiment=-0.8,
                importance=5,
            )
        ]

        score = self.analyzer.analyze(news)

        assert score < 20

    def test_score_never_exceeds_100(self):

        news = [
            News(
                title="Extreme Positive",
                source="Reuters",
                published_at="2026-06-30",
                sentiment=5.0,
                importance=10,
            )
        ]

        score = self.analyzer.analyze(news)

        assert score == 100.0

    def test_score_never_below_zero(self):

        news = [
            News(
                title="Extreme Negative",
                source="Reuters",
                published_at="2026-06-30",
                sentiment=-5.0,
                importance=10,
            )
        ]

        score = self.analyzer.analyze(news)

        assert score == 0.0