import importlib

import pytest

decimal_to_binary = importlib.import_module("30_decimal_to_binary").decimal_to_binary


def test_normal_conversion():
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(13) == "1101"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_one_and_powers_of_two():
    assert decimal_to_binary(1) == "1"
    assert decimal_to_binary(2) == "10"
    assert decimal_to_binary(16) == "10000"


def test_larger_numbers_and_string_result():
    result = decimal_to_binary(255)
    assert result == "11111111"
    assert isinstance(result, str)
    assert decimal_to_binary(1024) == "10000000000"


def test_negative_raises_value_error():
    with pytest.raises(ValueError):
        decimal_to_binary(-1)
    with pytest.raises(ValueError):
        decimal_to_binary(-10)
