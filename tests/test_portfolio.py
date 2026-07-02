"""
Unit Tests for Portfolio Model

Feature : FEATURE-018
Module  : Portfolio
"""

from src.models.portfolio import Portfolio
from src.models.position import Position


def create_position():
    """테스트용 Position"""

    return Position(
        ticker="005930",
        name="Samsung Electronics",
        quantity=10,
        average_price=70000,
        current_price=75000,
    )


def test_empty_portfolio():
    """빈 포트폴리오"""

    portfolio = Portfolio()

    assert portfolio.cash == 0.0
    assert portfolio.stock_asset == 0.0
    assert portfolio.total_asset == 0.0
    assert portfolio.total_profit == 0.0
    assert portfolio.cash_ratio == 0.0
    assert portfolio.stock_ratio == 0.0
    assert portfolio.total_profit_rate == 0.0
    assert portfolio.is_empty is True


def test_stock_asset():
    """주식 평가금액"""

    portfolio = Portfolio(
        positions=[create_position()]
    )

    assert portfolio.stock_asset == 750000


def test_total_asset():
    """총 자산"""

    portfolio = Portfolio(
        cash=250000,
        positions=[create_position()],
    )

    assert portfolio.total_asset == 1000000


def test_total_profit():
    """총 평가손익"""

    portfolio = Portfolio(
        positions=[create_position()]
    )

    assert portfolio.total_profit == 50000


def test_total_profit_rate():
    """총 평가수익률"""

    portfolio = Portfolio(
        positions=[create_position()]
    )

    assert round(
        portfolio.total_profit_rate,
        2,
    ) == 7.14


def test_cash_ratio():
    """현금 비중"""

    portfolio = Portfolio(
        cash=250000,
        positions=[create_position()],
    )

    assert round(
        portfolio.cash_ratio,
        2,
    ) == 25.00


def test_stock_ratio():
    """주식 비중"""

    portfolio = Portfolio(
        cash=250000,
        positions=[create_position()],
    )

    assert round(
        portfolio.stock_ratio,
        2,
    ) == 75.00


def test_is_empty_false():
    """보유 종목 존재"""

    portfolio = Portfolio(
        positions=[create_position()]
    )

    assert portfolio.is_empty is False