"""
News Analyzer

Stock-CIO
"""

from src.models.news import News


class NewsAnalyzer:
    """뉴스 데이터를 분석하여 News Score 생성"""

    def analyze(self, news: list[News]) -> float:
        """
        News Score 계산

        Returns
        -------
        float
            0 ~ 100
        """

        if not news:
            return 50.0

        score = 50.0

        # ==========================================================
        # Importance Score
        # ==========================================================

        importance = sum(item.importance for item in news)

        score += importance * 2

        # ==========================================================
        # Sentiment Score
        # ==========================================================

        sentiment = sum(item.sentiment for item in news)

        score += sentiment * 10

        # ==========================================================
        # Normalize
        # ==========================================================

        score = max(0.0, min(100.0, score))

        return round(score, 2)