"""
Unit Tests for Position Model

Stock-CIO
"""

from src.models.position import Position


def test_position_creation():
    """Position 생성"""

    position = Position(
        ticker="005930",
        name="Samsung Electronics",
        quantity=10,
        average_price=70000,
        current_price=75000,
    )

    assert position.ticker == "005930"
    assert position.name == "Samsung Electronics"
    assert position.quantity == 10
    assert position.average_price == 70000
    assert position.current_price == 75000


def test_cost_basis():
    """매입원가"""

    position = Position(
        ticker="005930",
        quantity=10,
        average_price=70000,
    )

    assert position.cost_basis == 700000


def test_market_value():
    """평가금액"""

    position = Position(
        ticker="005930",
        quantity=10,
        average_price=70000,
        current_price=75000,
    )

    assert position.market_value == 750000


def test_unrealized_profit():
    """평가손익"""

    position = Position(
        ticker="005930",
        quantity=10,
        average_price=70000,
        current_price=75000,
    )

    assert position.unrealized_profit == 50000


def test_return_rate():
    """평가수익률"""

    position = Position(
        ticker="005930",
        quantity=10,
        average_price=70000,
        current_price=77000,
    )

    assert round(position.return_rate, 2) == 10.00


def test_return_rate_zero_cost():
    """원가 0"""

    position = Position(
        ticker="005930",
        quantity=0,
        average_price=0,
        current_price=1000,
    )

    assert position.return_rate == 0.0


def test_is_open_true():
    """보유중"""

    position = Position(
        ticker="005930",
        quantity=1,
    )

    assert position.is_open is True


def test_is_open_false():
    """미보유"""

    position = Position(
        ticker="005930",
        quantity=0,
    )

    assert position.is_open is False