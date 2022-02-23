"""Writing utility functions to practice unit tests."""

__author__ = "730388033"


def only_evens(numbers: list[int]) -> list[int]:
    """When given a list of ints, only even numbers will be returned in the list."""
    xs: list[int] = list()
    # i: int = 0
    # while numbers[i] < len(numbers):
    #     if numbers[i] % 2 == 0:
    #         xs.append(numbers[i])
    #     i += 1
    for number in numbers:
        if number % 2 == 0:
            xs.append(number)
    return xs


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """In a given list, the first int is the start index.

    The second int is the end index, and it returns the values in-between.
    Non-inclusive of the end index.
    """
    return_list: list[int] = list()
    if a < 0:
        a = 0
    if b > len(a_list):
        b = len(a_list) - 1
    if a > len(a_list) or len(a_list) == 0 or b <= 0:
        return return_list
    while a < b:
        return_list.append(a_list[a])
        a += 1
    return return_list


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """Makes a list containing all of the first list, followed by the second."""
    # i: int = 0
    for i in list_b:
        list_a.append(i)
    return list_a
