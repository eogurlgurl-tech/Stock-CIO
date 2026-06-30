"""
News Analyzer

Stock-CIO
"""

from src.models.news import News


class NewsAnalyzer:
    """뉴스 데이터를 분석하여 News Score를 계산"""

    DEFAULT_SCORE = 50.0

    MIN_SCORE = 0.0

    MAX_SCORE = 100.0

    def analyze(self, news_list: list[News]) -> float:
        """
        뉴스 리스트를 분석하여 0~100 점수 반환

        Parameters
        ----------
        news_list : list[News]

        Returns
        -------
        float
        """

        if not news_list:
            return self.DEFAULT_SCORE

        total_weight = 0.0
        weighted_score = 0.0

        for news in news_list:

            weight = max(news.importance, 1)

            # sentiment
            # -1.0 ~ +1.0
            sentiment = max(min(news.sentiment, 1.0), -1.0)

            score = 50.0 + (sentiment * 50.0)

            weighted_score += score * weight
            total_weight += weight

        result = weighted_score / total_weight

        return round(self._clamp(result), 2)

    def _clamp(self, value: float) -> float:

        if value < self.MIN_SCORE:
            return self.MIN_SCORE

        if value > self.MAX_SCORE:
            return self.MAX_SCORE

        return value