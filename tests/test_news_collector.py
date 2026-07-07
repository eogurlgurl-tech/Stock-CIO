"""
Unit Tests for News Collector

Module : News Collector
"""

from src.collectors.news_collector import NewsCollector


def test_build_news_from_flat_payload():
    """Yahoo flat payload is converted to News."""

    news = NewsCollector._build_news(
        {
            "title": "Market headline",
            "publisher": "Publisher",
            "providerPublishTime": 0,
            "link": "https://example.com/news",
        }
    )

    assert news is not None
    assert news.title == "Market headline"
    assert news.source == "Publisher"
    assert news.published_at == "1970-01-01"
    assert news.url == "https://example.com/news"


def test_build_news_from_nested_payload():
    """Yahoo nested payload is converted to News."""

    news = NewsCollector._build_news(
        {
            "content": {
                "title": "Nested headline",
                "provider": {
                    "displayName": "News Source",
                },
                "pubDate": "2026-07-06T08:00:00Z",
                "canonicalUrl": {
                    "url": "https://example.com/nested",
                },
            }
        }
    )

    assert news is not None
    assert news.title == "Nested headline"
    assert news.source == "News Source"
    assert news.published_at == "2026-07-06"
    assert news.url == "https://example.com/nested"


def test_invalid_news_payload_is_ignored():
    """Payload without a title is ignored."""

    assert NewsCollector._build_news({}) is None
