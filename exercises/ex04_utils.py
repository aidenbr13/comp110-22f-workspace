"""EX04 - Utils!"""

__author__: str = "730320104"


def all(x: list[int], y: int) -> bool:
    """Created a function in which a list is tested to see whether all the integers in the list are the same as a given integer."""
    i: int = 0
    if len(x) == 0:
        return False
    while i < len(x):
        if x[i] == y:
            i = i + 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Created a function that returns the largest value in a given list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    z: int = input[0]
    while i < len(input):
        if z < input[i]:
            z = input[i]
            i = i + 1
        else:
            i = i + 1
    return z


def is_equal(a: list[int], b: list[int]) -> bool:
    """Created a function to see if each integer in a list is equal to a given list of integers at each specific index."""
    if a == b:
        return True
    else:
        return False