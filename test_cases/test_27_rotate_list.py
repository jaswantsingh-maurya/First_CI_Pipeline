import importlib

rotate_list = importlib.import_module("27_rotate_list").rotate_list


def test_right_rotation():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_empty_and_single_element():
    assert rotate_list([], 3) == []
    assert rotate_list([7], -8) == [7]


def test_negative_rotation():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_oversized_and_negative_oversized_rotation():
    assert rotate_list([1, 2, 3], 7) == [3, 1, 2]
    assert rotate_list([1, 2, 3], -7) == [2, 3, 1]


def test_input_unchanged_and_new_list_even_without_rotation():
    items = [1, 2, 3]
    assert rotate_list(items, 1) == [3, 1, 2]
    for k in (0, 3, -3):
        result = rotate_list(items, k)
        assert result == items
        assert result is not items
    assert items == [1, 2, 3]
