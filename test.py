from fail import sum, multiplication

def test_sum():
    assert sum(3,5) == 8
    assert sum(6, 10) == 16
    assert multiplication(4, 3) == 12

if __name__ == "__main__":
    test_sum()