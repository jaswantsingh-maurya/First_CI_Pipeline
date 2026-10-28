import importlib

set_intersection = importlib.import_module("28_set_intersection").set_intersection


def test_common_elements():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_empty_sets():
    assert set_intersection(set(), {1}) == set()
    assert set_intersection({1}, set()) == set()
    assert set_intersection(set(), set()) == set()


def test_disjoint_sets():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_negative_numbers_and_strings():
    assert set_intersection({-2, -1, 0}, {-1, 0, 1}) == {-1, 0}
    assert set_intersection({"cat", "dog"}, {"dog", "bird"}) == {"dog"}


def test_identical_sets_return_new_set_without_mutation():
    first, second = {1, 2}, {1, 2}
    result = set_intersection(first, second)
    assert isinstance(result, set)
    assert result == {1, 2}
    assert result is not first and result is not second
    assert first == {1, 2} and second == {1, 2}
