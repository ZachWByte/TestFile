import pytest

from fail import (
    calculate_total,
    calculate_average,
    apply_multiplier,
    find_max,
    count_positive,
)


def test_calculate_total():
    result = calculate_total([60, 60], 0.10, 0.20)
    assert result == pytest.approx(105.6)


def test_calculate_total_no_discount():
    result = calculate_total([50], 0.10, 0.20)
    assert result == pytest.approx(55)


def test_calculate_average():
    assert calculate_average([10, 20, 30]) == 20


def test_calculate_average_empty():
    assert calculate_average([]) == 0


def test_apply_multiplier():
    assert apply_multiplier(5, 3) == 15


def test_apply_multiplier_decimal():
    assert apply_multiplier(2.5, 4) == 10


def test_find_max():
    assert find_max([3, 8, 2, 5]) == 8


def test_find_max_negative_numbers():
    assert find_max([-10, -3, -7]) == -3


def test_find_max_empty():
    assert find_max([]) is None


def test_count_positive():
    assert count_positive([1, 2, 3, -1, -5]) == 3


def test_count_positive_with_zero():
    assert count_positive([1, 0, -1, 5, 0]) == 2