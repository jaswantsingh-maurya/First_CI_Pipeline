import importlib

is_armstrong = importlib.import_module("29_armstrong_number").is_armstrong


def test_three_digit_armstrong_numbers():
    for number in (153, 370, 371, 407):
        assert is_armstrong(number) is True


def test_non_armstrong_numbers():
    for number in (10, 123, 154):
        assert is_armstrong(number) is False


def test_zero_and_single_digits():
    for number in range(10):
        assert is_armstrong(number) is True


def test_negative_numbers():
    assert is_armstrong(-153) is False
    assert is_armstrong(-1) is False


def test_larger_digit_counts():
    assert is_armstrong(1634) is True
    assert is_armstrong(9474) is True
    assert is_armstrong(54748) is True
    assert is_armstrong(9475) is False
