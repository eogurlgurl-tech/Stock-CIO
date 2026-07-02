"""
Unit Tests for Allocation Strategy

Feature : FEATURE-018
Module  : Allocation Strategy
"""

import pytest

from src.models.portfolio import Portfolio
from src.strategies.allocation_strategy import AllocationStrategy


class DummyAllocationStrategy(AllocationStrategy):
    """테스트용 Allocation Strategy"""

    def allocate(
        self,
        portfolio: Portfolio,
    ) -> Portfolio:
        return portfolio


def test_allocation_strategy_can_be_inherited():
    """상속 가능 여부"""

    strategy = DummyAllocationStrategy()

    assert isinstance(
        strategy,
        AllocationStrategy,
    )


def test_allocate_returns_portfolio():
    """Portfolio 반환"""

    portfolio = Portfolio()

    strategy = DummyAllocationStrategy()

    result = strategy.allocate(portfolio)

    assert result is portfolio


def test_abstract_class_cannot_be_instantiated():
    """추상 클래스 직접 생성 불가"""

    with pytest.raises(TypeError):
        AllocationStrategy()