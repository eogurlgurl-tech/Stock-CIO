"""
Historical Repository Test

Stock-CIO
"""

from unittest.mock import Mock

from src.models.historical_price import HistoricalPrice
from src.repositories.historical_repository import HistoricalRepository


def create_history() -> list[HistoricalPrice]:
    """테스트용 Historical Data"""

    from datetime import datetime

    return [
        HistoricalPrice(
            symbol="TEST",
            date=datetime(2026, 1, 1),
            open=100,
            high=110,
            low=90,
            close=105,
            volume=1000,
        )
    ]


def test_repository_load_from_csv():
    """CSV가 존재하면 Loader를 호출하지 않는다."""

    loader = Mock()
    storage = Mock()

    history = create_history()

    storage.exists.return_value = True
    storage.load.return_value = history

    repository = HistoricalRepository(
        loader=loader,
        storage=storage,
    )

    result = repository.load("TEST")

    assert result == history

    storage.load.assert_called_once_with("TEST")

    loader.load.assert_not_called()


def test_repository_download_and_save():
    """CSV가 없으면 다운로드 후 저장한다."""

    loader = Mock()
    storage = Mock()

    history = create_history()

    storage.exists.return_value = False

    loader.load.return_value = history

    repository = HistoricalRepository(
        loader=loader,
        storage=storage,
    )

    result = repository.load("TEST")

    assert result == history

    loader.load.assert_called_once()

    storage.save.assert_called_once_with(history)


def test_repository_empty_history():
    """다운로드 실패 시 빈 리스트 반환"""

    loader = Mock()
    storage = Mock()

    storage.exists.return_value = False

    loader.load.return_value = []

    repository = HistoricalRepository(
        loader=loader,
        storage=storage,
    )

    result = repository.load("TEST")

    assert result == []

    storage.save.assert_not_called()