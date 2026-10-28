import importlib

import pytest

find_max_min = importlib.import_module("25_max_min_list").find_max_min


def test_normal_list():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)


def test_single_element():
    assert find_max_min([5]) == (5, 5)


def test_all_negative():
    assert find_max_min([-4, -9, -1]) == (-1, -9)


def test_duplicates_and_floats():
    assert find_max_min([2, 2, 2]) == (2, 2)
    assert find_max_min([1.5, -0.5, 3.25]) == (3.25, -0.5)


def test_empty_raises_value_error():
    with pytest.raises(ValueError):
        find_max_min([])
