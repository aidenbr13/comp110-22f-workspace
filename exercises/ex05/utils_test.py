"""EX05 - Utils Test."""

__author__: str = "730320104"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat

def test_only_evens() -> None:
    a: list[int] = [2, 1, 3]
    assert only_evens(a) == [2]

def test_concat() -> None:
    a: list[int] = [1, 1, 1]
    b: list[int] = [2, 2, 2]
    assert concat(a,b) == [1, 1, 1, 2, 2, 2]

def test_sub() -> None:
    a: list[int] = [1, 3, 5, 7]
    b: int = 1
    c: int = 3