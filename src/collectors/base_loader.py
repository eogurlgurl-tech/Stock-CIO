"""
Base Loader

Stock-CIO
"""

from __future__ import annotations


class BaseLoader:
    """Collector 공통 기능"""

    @staticmethod
    def calculate_change(today: float, yesterday: float) -> float:
        """
        전일 대비 등락률(%)

        Returns
        -------
        float
        """

        if yesterday == 0:
            return 0.0

        return round(
            ((today - yesterday) / yesterday) * 100,
            2,
        )

    @staticmethod
    def safe_round(
        value: float,
        digits: int = 2,
    ) -> float:
        """안전한 반올림"""

        try:
            return round(float(value), digits)
        except Exception:
            return 0.0

    @staticmethod
    def has_enough_data(df, minimum_rows: int = 2) -> bool:
        """데이터 유효성 검사"""

        return (
            df is not None
            and not df.empty
            and len(df) >= minimum_rows
        )