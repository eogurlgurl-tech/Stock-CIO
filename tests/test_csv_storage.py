"""
CSV Storage Test

Stock-CIO
"""

from datetime import datetime
from pathlib import Path
import shutil

from src.models.historical_price import HistoricalPrice
from src.storage.csv_storage import CSVStorage


TEMP_DIR = Path("tests") / "temp_storage"


def create_history() -> list[HistoricalPrice]:

    return [
        HistoricalPrice(
            symbol="TEST",
            date=datetime(2026, 1, 1),
            open=100,
            high=110,
            low=90,
            close=105,
            volume=1000,
        ),
        HistoricalPrice(
            symbol="TEST",
            date=datetime(2026, 1, 2),
            open=105,
            high=120,
            low=100,
            close=115,
            volume=1500,
        ),
    ]


def setup_function():

    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)


def teardown_function():

    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)


def test_save_and_load():

    storage = CSVStorage(TEMP_DIR)

    history = create_history()

    storage.save(history)

    assert storage.exists("TEST")

    loaded = storage.load("TEST")

    assert len(loaded) == 2

    assert loaded[0].symbol == "TEST"

    assert loaded[0].close == 105

    assert loaded[1].close == 115


def test_load_not_exists():

    storage = CSVStorage(TEMP_DIR)

    history = storage.load("NOT_EXIST")

    assert history == []