"""
Unit Tests for Desktop Context Filtering

Module : Desktop Application
"""

from src.desktop.stock_cio_app import StockCIOApp


def test_internal_context_is_removed():
    """내부 Context 키 목록은 사용자 화면에 표시하지 않는다."""

    output = (
        "Dashboard result\n"
        + "=" * 60
        + "\nSystem Context\n"
        + "=" * 60
        + "\n- market\n- score\n"
    )

    filtered = StockCIOApp._translate_output(output)

    assert "Dashboard result" in filtered
    assert "System Context" not in filtered
    assert "- market" not in filtered
