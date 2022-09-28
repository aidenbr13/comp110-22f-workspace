"""EX05 - Utils Test."""

__author__: str = "730320104"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

def test_only_evens() -> None:
    """Created a unit test for the function we created that returns even numbers."""
    a: list[int] = [1, 3, 2]
    assert only_evens(a) == [2]

def test_concat() -> None:
    """Created a unit test for the function we created that combines two lists into one."""
    a: list[int] = [1, 1, 1]
    b: list[int] = [2, 2, 2]
    assert concat(a, b) == [1, 1, 1, 2, 2, 2]

def test_sub() -> None:
    """Created a unit test for the function we created that returns a new list between the given indeces."""
    a: list[int] = [1, 3, 5, 7]
    b: int = 1
    c: int = 3
    assert sub(a, b, c) == [3, 5]