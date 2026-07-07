"""
Unit Tests for KRX Loader

Module : KRX Loader
"""

from src.collectors.krx_loader import KRXLoader


def test_yahoo_result_is_used_first(monkeypatch):
    """Yahoo data is used without calling pykrx."""

    loader = KRXLoader()
    monkeypatch.setattr(
        loader,
        "_yahoo_market_data",
        lambda symbol: (3000.0, 1.5),
    )
    monkeypatch.setattr(
        loader,
        "_pykrx_market_data",
        lambda ticker: (_ for _ in ()).throw(
            AssertionError("pykrx must not be called")
        ),
    )

    result = loader._market_data("1001", "^KS11")

    assert result == (3000.0, 1.5)


def test_pykrx_is_used_as_fallback(monkeypatch):
    """pykrx data is used when Yahoo is unavailable."""

    loader = KRXLoader()
    monkeypatch.setattr(
        loader,
        "_yahoo_market_data",
        lambda symbol: None,
    )
    monkeypatch.setattr(
        loader,
        "_pykrx_market_data",
        lambda ticker: (3000.0, -0.5),
    )

    result = loader._market_data("1001", "^KS11")

    assert result == (3000.0, -0.5)


def test_missing_data_returns_neutral_change(monkeypatch):
    """Total source failure does not create a false decline."""

    loader = KRXLoader()
    monkeypatch.setattr(
        loader,
        "_yahoo_market_data",
        lambda symbol: None,
    )
    monkeypatch.setattr(
        loader,
        "_pykrx_market_data",
        lambda ticker: None,
    )

    result = loader._market_data("1001", "^KS11")

    assert result == (0.0, None)


def test_load_maps_kospi_and_kosdaq(monkeypatch):
    """Loaded values are mapped to MarketSnapshot."""

    loader = KRXLoader()
    results = iter(
        [
            (3000.0, 1.0),
            (900.0, -1.0),
        ]
    )
    monkeypatch.setattr(
        loader,
        "_market_data",
        lambda ticker, symbol: next(results),
    )

    market = loader.load()

    assert market.kospi == 3000.0
    assert market.kospi_change == 1.0
    assert market.kosdaq == 900.0
    assert market.kosdaq_change == -1.0
