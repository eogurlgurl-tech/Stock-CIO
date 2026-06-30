"""
News Collector

Stock-CIO
"""

from src.collectors.base_collector import BaseCollector
from src.models.news import News


class NewsCollector(BaseCollector):
    """뉴스 수집기"""

    def collect(self) -> list[News]:

        # FEATURE-013 초기 버전
        # 실제 API 연동 예정

        return []