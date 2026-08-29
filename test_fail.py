from fail import calculate_total, calculate_average, apply_multiplier


def test_calculate_total():
    assert calculate_total([50, 30, 40], 0.1, 0.2) == 100
    assert calculate_total([20, 30, 50], 0.08, 0.1) == 90


def test_calculate_average():
    assert calculate_average([10, 20, 30, 40]) == 30
    assert calculate_average([5, 15, 25]) == 20


def test_apply_multiplier():
    assert apply_multiplier(10, 5) == 40
    assert apply_multiplier(7, 3) == 25


if __name__ == "__main__":
    test_calculate_total()
    test_calculate_average()
    test_apply_multiplier()