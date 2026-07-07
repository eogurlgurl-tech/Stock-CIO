"""
Price Updater Service

Update `Position.current_price` values from market data sources.
"""

from datetime import datetime, timedelta
from typing import Optional

import yfinance as yf


def _try_yfinance_price(ticker: str) -> tuple[Optional[float], str | None]:
    """Try to fetch price from Yahoo Finance. Accepts raw ticker and attempts
    common KRX suffixes if needed."""

    candidates = [ticker]

    # If ticker is 6 digits, try KRX suffix
    if ticker.isdigit() and len(ticker) == 6:
        candidates = [f"{ticker}.KS", f"{ticker}.KQ", ticker]

    for sym in candidates:
        try:
            frame = yf.Ticker(sym).history(period="5d")

            if frame is None or frame.empty:
                continue

            price = float(frame["Close"].iloc[-1])
            # timestamp from index if available
            try:
                ts = frame.index[-1]
                ts_str = getattr(ts, 'strftime', lambda fmt: str(ts))("%Y-%m-%d %H:%M:%S")
            except Exception:
                ts_str = None

            return price, ts_str
        except Exception:
            continue

    return None
    return None, None


def _try_pykrx_price(ticker: str) -> tuple[Optional[float], str | None]:
    """Try to fetch price from pykrx for 6-digit KRX tickers."""
    if not (ticker.isdigit() and len(ticker) == 6):
        return None, None

    try:
        from pykrx import stock

        today = datetime.now()
        from_date = (today - timedelta(days=7)).strftime("%Y%m%d")
        to_date = today.strftime("%Y%m%d")

        frame = stock.get_market_ohlcv_by_date(from_date, to_date, ticker)

        if frame is None or frame.empty:
            return None, None

        price = float(frame["종가"].iloc[-1])
        # pykrx returns dates as index; try to extract last date
        try:
            last_date = frame.index[-1]
            ts_str = getattr(last_date, 'strftime', lambda fmt: str(last_date))("%Y-%m-%d %H:%M:%S")
        except Exception:
            ts_str = None

        return price, ts_str
    except Exception:
        return None, None


def update_portfolio_prices(portfolio) -> None:
    """Update `current_price` for each position in the given portfolio.

    This function mutates the `portfolio.positions` list in-place. It tries
    Yahoo Finance first, then falls back to pykrx for KRX tickers.
    """

    for position in getattr(portfolio, "positions", []):
        ticker = getattr(position, "ticker", "")

        if not isinstance(ticker, str) or not ticker:
            continue
        # Prefer pykrx for Korean 6-digit tickers
        price = None
        source = None
        ts = None

        if ticker.isdigit() and len(ticker) == 6:
            p, p_ts = _try_pykrx_price(ticker)
            if p is not None:
                price = p
                source = "pykrx"
                ts = p_ts

        if price is None:
            p, p_ts = _try_yfinance_price(ticker)
            if p is not None:
                price = p
                source = "yfinance"
                ts = p_ts

        if price is not None:
            try:
                position.current_price = float(price)
                position.price_source = source or ""
                position.price_timestamp = ts or ""
            except Exception:
                continue
