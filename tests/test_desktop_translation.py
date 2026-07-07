"""
Unit Tests for Desktop Translation

Module : Desktop Application
"""

from src.desktop.stock_cio_app import StockCIOApp


def test_analysis_output_is_translated_to_korean():
    """주요 분석 결과가 한글로 변환된다."""

    output = StockCIOApp._translate_output(
        "Market Status : VERY BEARISH\n"
        "ACTION : REDUCE\n"
        "Portfolio Score : 81.00\n"
        "Decision : SELL\n"
    )

    assert "시장 상태 : 매우 약세" in output
    assert "대응 : 비중 축소" in output
    assert "포트폴리오 점수 : 81.00" in output
    assert "판단 : 매도" in output
