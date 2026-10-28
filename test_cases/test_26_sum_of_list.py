import importlib

sum_of_list = importlib.import_module("26_sum_of_list").sum_of_list


def test_positive_numbers():
    assert sum_of_list([1, 2, 3, 4]) == 10


def test_empty_list():
    assert sum_of_list([]) == 0


def test_single_element():
    assert sum_of_list([7]) == 7


def test_negative_and_mixed_numbers():
    assert sum_of_list([-1, -2, -3]) == -6
    assert sum_of_list([-5, 0, 5]) == 0


def test_floats_and_unchanged_input():
    numbers = [1.5, 2.25, -0.75]
    assert sum_of_list(numbers) == 3.0
    assert numbers == [1.5, 2.25, -0.75]
