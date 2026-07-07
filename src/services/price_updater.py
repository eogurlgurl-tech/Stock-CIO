"""
Price Updater Service

Update `Position.current_price` values from market data sources.
"""

from datetime import datetime, timedelta
from typing import Optional

import yfinance as yf


def _try_yfinance_price(ticker: str) -> Optional[float]:
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
            return price
        except Exception:
            continue

    return None


def _try_pykrx_price(ticker: str) -> Optional[float]:
    """Try to fetch price from pykrx for 6-digit KRX tickers."""

    if not (ticker.isdigit() and len(ticker) == 6):
        return None

    try:
        from pykrx import stock

        today = datetime.now()
        from_date = (today - timedelta(days=7)).strftime("%Y%m%d")
        to_date = today.strftime("%Y%m%d")

        frame = stock.get_market_ohlcv_by_date(from_date, to_date, ticker)

        if frame is None or frame.empty:
            return None

        price = float(frame["종가"].iloc[-1])
        return price
    except Exception:
        return None


def update_portfolio_prices(portfolio) -> None:
    """Update `current_price` for each position in the given portfolio.

    This function mutates the `portfolio.positions` list in-place. It tries
    Yahoo Finance first, then falls back to pykrx for KRX tickers.
    """

    for position in getattr(portfolio, "positions", []):
        ticker = getattr(position, "ticker", "")

        if not isinstance(ticker, str) or not ticker:
            continue

        price = _try_yfinance_price(ticker)

        if price is None:
            price = _try_pykrx_price(ticker)

        if price is not None:
            try:
                position.current_price = float(price)
            except Exception:
                # ignore assignment errors
                continue
