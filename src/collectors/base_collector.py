"""
Base Collector

Stock-CIO
"""

from abc import ABC, abstractmethod


class BaseCollector(ABC):
    """모든 Collector의 기본 인터페이스"""

    @abstractmethod
    def collect(self):
        """데이터 수집"""
        raise NotImplementedError