"""EX07 - Dictionary Tests."""

__author__: str = "730320104"

import pytest
from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_1_invert() -> None:
    """Created a edge case unit test for the function we created that inverts a given dictionary involving a blank dictionary."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_2_invert() -> None:
    """Created a use case unit test for the function we created that inverts a given dictionary."""
    a: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_3_invert() -> None:
    """Created a use case unit test for the function we created that inverts a given dictionary."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)

def test_1_favorite_color() -> None:
    """Created a use case unit test for the function we created that returns the value (color) that appears most frequently."""
    a: dict[str, str] = {}
    assert favorite_color(a) == ""


def test_2_favorite_color() -> None:
    """Created a edge case unit test for the function we created that returns the value (color) that appears most frequently."""    
    a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(a) == "blue"


def test_3_favorite_color() -> None:
    """Created a edge case unit test for the function we created that returns the value (color) that appears most frequently."""    
    a: dict[str, str] = {"Josh": "orange", "Aiden": "purple"}
    assert favorite_color(a) == "orange"


def test_1_count() -> None:
    """Created a edge case unit test for the function we created that counts the number of times a value appeared in a given list."""
    a: list[str] = []
    assert count(a) == {}


def test_2_count() -> None:
    """Created a use case unit test for the function we created that counts the number of times a value appeared in a given list."""
    a: list[str] = ["hello", "hi", "hello"]
    assert count(a) == {"hello": 2, "hi": 1}


def test_3_count() -> None:
    """Created a use case unit test for the function we created that counts the number of times a value appeared in a given list."""
    a: list[str] = ["goodbye", "bye", "hello"]
    assert count(a) == {"goodbye": 1, "bye": 1, "hello": 1}