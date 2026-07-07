"""
News Collector

Stock-CIO
"""

from datetime import UTC, datetime
from typing import Any

import yfinance as yf

from src.collectors.base_collector import BaseCollector
from src.models.news import News


class NewsCollector(BaseCollector):
    """Collect current market headlines from Yahoo Finance."""

    QUERIES = (
        "KOSPI",
        "US stock market",
    )

    MAX_NEWS = 5

    def collect(self) -> list[News]:
        """Collect and normalize current market headlines."""

        collected: list[News] = []
        titles: set[str] = set()

        for query in self.QUERIES:
            try:
                search = yf.Search(
                    query,
                    news_count=self.MAX_NEWS,
                    raise_errors=True,
                )

                for item in search.news:
                    news = self._build_news(item)

                    if news is None or news.title in titles:
                        continue

                    collected.append(news)
                    titles.add(news.title)

                    if len(collected) >= self.MAX_NEWS:
                        return collected

            except Exception as error:
                print(
                    f"News Collector Error ({query}) : {error}"
                )

        return collected

    @classmethod
    def _build_news(
        cls,
        item: Any,
    ) -> News | None:
        """Convert Yahoo's flat or nested news payload."""

        if not isinstance(item, dict):
            return None

        content = item.get("content")

        if not isinstance(content, dict):
            content = {}

        title = item.get("title") or content.get("title")

        if not isinstance(title, str) or not title.strip():
            return None

        source = cls._source(item, content)
        published_at = cls._published_at(item, content)
        url = cls._url(item, content)

        return News(
            title=title.strip(),
            source=source,
            published_at=published_at,
            sentiment=0.0,
            importance=1,
            url=url,
        )

    @staticmethod
    def _source(
        item: dict,
        content: dict,
    ) -> str:
        """Extract the publisher name."""

        source = item.get("publisher")

        if isinstance(source, str):
            return source

        provider = content.get("provider")

        if isinstance(provider, dict):
            display_name = provider.get("displayName")

            if isinstance(display_name, str):
                return display_name

        return "Yahoo Finance"

    @staticmethod
    def _published_at(
        item: dict,
        content: dict,
    ) -> str:
        """Extract the publication date."""

        timestamp = item.get("providerPublishTime")

        if isinstance(timestamp, (int, float)):
            return datetime.fromtimestamp(
                timestamp,
                tz=UTC,
            ).strftime("%Y-%m-%d")

        publication = content.get("pubDate")

        if isinstance(publication, str):
            return publication[:10]

        return ""

    @staticmethod
    def _url(
        item: dict,
        content: dict,
    ) -> str:
        """Extract the article URL."""

        link = item.get("link")

        if isinstance(link, str):
            return link

        canonical_url = content.get("canonicalUrl")

        if isinstance(canonical_url, dict):
            url = canonical_url.get("url")

            if isinstance(url, str):
                return url

        return ""
