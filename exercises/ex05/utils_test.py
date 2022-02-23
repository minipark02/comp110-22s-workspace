"""Tests for the utility functions."""

__author__ = "730388033"


from utils import only_evens, sub, concat


def test_only_evens_no_numbers() -> None:
    """Tests for empty list."""
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_single_odd_number() -> None:
    """Tests for a single odd number."""
    numbers: list[int] = [3]
    assert only_evens(numbers) == []


def test_only_evens_two_even_numbers() -> None:
    """Tests for two even numbers."""
    numbers: list[int] = [1, 3, 2, 6, 7]
    assert only_evens(numbers) == [2, 6]


def test_only_evens_all_even_numbers() -> None:
    """Tests for all even numbers in list."""
    numbers: list[int] = [2, 6, 30, 40, 24]
    assert only_evens(numbers) == [2, 6, 30, 40, 24]


def test_sub_len_0_list() -> None:
    """Tests for an empty list."""
    a_list: list[int] = []
    assert sub(a_list, 3, 6) == []


def test_sub_negative_a_int() -> None:
    """Tests for a negative first index."""
    a_list: list[int] = [10, 20, 30, 40, 50]
    assert sub(a_list, -2, 3) == [10, 20, 30]


def test_sub_b_int_longer_than_len() -> None:
    """Tests for an end index longer than the len of the list."""
    a_list: list[int] = [10, 20, 30, 40, 50]
    assert sub(a_list, 1, 6) == [20, 30, 40]


def test_sub_len_5_list() -> None:
    """Tests for a list with a len of 5."""
    a_list: list[int] = [10, 20, 30, 40, 50]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_len_4_list() -> None:
    """Tests for a list with a len of 4."""
    a_list: list[int] = [1, 2, 3, 4]
    assert sub(a_list, 1, 3) == [2, 3]


def test_concat_only_one_number_with_single_list() -> None:
    """Adds numbers to the end of the first list with only one value."""
    list_a: list[int] = [0]
    list_b: list[int] = [1, 2, 3]
    assert concat(list_a, list_b) == [0, 1, 2, 3]


def test_concat_even_list_odd_list() -> None:
    """Adds odd numbers after even numbers in a list."""
    list_a: list[int] = [2, 4, 6]
    list_b: list[int] = [1, 3, 5]
    assert concat(list_a, list_b) == [2, 4, 6, 1, 3, 5]


def test_concat_different_len_lists() -> None:
    """Both lists are different lens and list b is added to the end of a."""
    list_a: list[int] = [1, 2, 3, 4, 5]
    list_b: list[int] = [0, 4, 3]
    assert concat(list_a, list_b) == [1, 2, 3, 4, 5, 0, 4, 3]
