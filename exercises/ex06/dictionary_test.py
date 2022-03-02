"""Testing the dictionary functions."""

__author__ = "730388033"


from exercises.ex06.dictionary import invert, favourite_colour, count
import pytest


def test_keyerror() -> None:
    """Tests to see if KeyError is raised w/duplicate keys or not."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_three_keys() -> None:
    """Tests three key-value pairs to see if inverted or not."""
    a_dict = {'mercedes': 'chai', 'jewell': 'taro', 'angela': 'matcha'}
    assert invert(a_dict) == {'chai': 'mercedes', 'taro': 'jewell', 'matcha': 'angela'}


def test_two_keys() -> None:
    """Tests two key-value pairs to see if inverted or not."""
    a_dict = {'rue': 'jules', 'maddy': 'cassie'}
    assert invert(a_dict) == {'jules': 'rue', 'cassie': 'maddy'}


def test_single_colour() -> None:
    """Tests to see if a single colour is reported back."""
    initial_dict = {'mercedes': 'sage green'}
    assert favourite_colour(initial_dict) == "sage green"


def test_same_favourite_colour() -> None:
    """Everyone has the same favourite colour."""
    initial_dict = {'mercedes': 'sage green', 'angela': 'sage green', 'jewell': 'sage green'}
    assert favourite_colour(initial_dict) == "sage green"


def test_tie_colour() -> None:
    """Tie for two fave colours, returns the first one reported."""
    initial_dict = {'esther': 'yellow', 'mercedes': 'blue', 'michelle': 'blue', 'james': 'yellow'}
    assert favourite_colour(initial_dict) == "yellow"


def test_one_char() -> None:
    """Tests a single char and how many times it appears."""
    a_list: list[str] = ['a']
    assert count(a_list) == {'a': 1}


def test_5_words() -> None:
    """Tests to see how many times a word occurs in a list of 5."""
    a_list = ['cat', 'dog', 'pony', 'mouse', 'cat']
    assert count(a_list) == {'cat': 2, 'dog': 1, 'pony': 1, 'mouse': 1}


def test_same_words() -> None:
    """Tests to see if the same word will be reported n times."""
    a_list = ['cat', 'cat', 'cat', 'cat', 'cat', 'cat']
    assert count(a_list) == {'cat': 6}