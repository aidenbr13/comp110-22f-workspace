"""EX05 - Utils Test."""

__author__: str = "730320104"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_blank_only_evens() -> None:
    """Created a edge case unit test for the function we created that returns even numbers involving a blank list."""
    a: list[int] = []
    assert only_evens(a) == []


def test_1_only_evens() -> None:
    """Created a use case unit test for the function we created that returns even numbers."""
    a: list[int] = [1, 2, 3]
    assert only_evens(a) == [2]


def test_none_only_evens() -> None:
    """Created a use case unit test for the function we created that returns nothing from a list with no even numbers."""
    a: list[int] = [5, 7, 9]
    assert only_evens(a) == []


def test_1_concat() -> None:
    """Created a use case unit test for the function we created that combines two lists into one."""
    a: list[int] = [1, 1, 1]
    b: list[int] = [2, 2, 2]
    assert concat(a, b) == [1, 1, 1, 2, 2, 2]


def test_same_concat() -> None:
    """Created a use case unit test for the function we created that combines two lists into one when elements of a list are the same."""
    a: list[int] = [0, 0, 1]
    b: list[int] = [0, 0, 2]
    assert concat(a, b) == [0, 0, 1, 0, 0, 2]


def test_empty_concat() -> None:
    """Created a edge case unit test for the function we created that combines two lists into one when one of the given lists is empty."""
    a: list[int] = []
    b: list[int] = [2, 2, 2]
    assert concat(a, b) == [2, 2, 2]


def test_1_sub() -> None:
    """Created a use case unit test for the function we created that returns a new list between the given indeces."""
    a: list[int] = [1, 3, 5, 7]
    b: int = 1
    c: int = 3
    assert sub(a, b, c) == [3, 5]


def test_single_sub() -> None:
    """Created a use case unit test for the function we created that returns a new list between the given indeces when the indeces have a difference of only 1."""
    a: list[int] = [0, 1, 2]
    b: int = 0
    c: int = 1
    assert sub(a, b, c) == [0]


def test_blank_sub() -> None:
    """Created a edge case unit test for the function we created that returns a new list between the given indece when the given list is empty."""
    a: list[int] = []
    b: int = 1
    c: int = 3
    assert sub(a, b, c) == []