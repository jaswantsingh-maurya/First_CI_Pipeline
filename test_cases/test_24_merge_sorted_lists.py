import importlib

merge_sorted_lists = importlib.import_module("24_merge_sorted_lists").merge_sorted_lists


def test_interleaved_lists():
    assert merge_sorted_lists([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]


def test_empty_lists():
    assert merge_sorted_lists([], []) == []
    assert merge_sorted_lists([], [1, 2]) == [1, 2]
    assert merge_sorted_lists([1, 2], []) == [1, 2]


def test_negatives_and_duplicates():
    assert merge_sorted_lists([-3, 0, 2], [-3, -1, 2]) == [-3, -3, -1, 0, 2, 2]


def test_single_elements_and_unequal_lengths():
    assert merge_sorted_lists([2], [1]) == [1, 2]
    assert merge_sorted_lists([1], [2, 3, 4]) == [1, 2, 3, 4]


def test_inputs_unchanged_and_result_is_new():
    first, second = [1, 3], [2, 4]
    result = merge_sorted_lists(first, second)
    assert first == [1, 3] and second == [2, 4]
    assert result == [1, 2, 3, 4]
    assert result is not first and result is not second
