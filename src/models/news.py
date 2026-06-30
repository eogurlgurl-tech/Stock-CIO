"""
News Model

Stock-CIO
"""

from dataclasses import dataclass


@dataclass(slots=True)
class News:
    """뉴스 데이터 모델"""

    title: str

    source: str

    published_at: str

    sentiment: float = 0.0

    importance: int = 0

    url: str = ""