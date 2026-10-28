import importlib

bubble_sort = importlib.import_module("23_sort_without_sort").bubble_sort


def test_unsorted_list():
    assert bubble_sort([5, 2, 9, 1]) == [1, 2, 5, 9]


def test_empty_and_single_element():
    assert bubble_sort([]) == []
    assert bubble_sort([7]) == [7]


def test_negative_numbers_and_duplicates():
    assert bubble_sort([0, -2, 3, -2]) == [-2, -2, 0, 3]


def test_sorted_and_reverse_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_returns_new_list_without_mutating_input():
    original = [3, 1, 2]
    result = bubble_sort(original)
    assert original == [3, 1, 2]
    assert result == [1, 2, 3]
    assert result is not original
