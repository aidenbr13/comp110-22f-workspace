"""EX05 - Utils."""

__author__: str = "730320104"


def only_evens(x: list[int]) -> list[int]:
    """Defined a function that returns even numbers in a given list."""
    i: int = 0
    z: list[int] = []
    while i < len(x):
        if x[i] % 2 == 0:
            z.append(x[i])
        i += 1
    return z


def concat(x: list[int], y: list[int]) -> list[int]:
    """Defined a function that combines the elements of two lists into one longer list."""
    z: list[int] = []
    i: int = 0
    while i < len(x):
        z.append(x[i])
        i += 1
    while i < len(y):
        z.append(y[i])
        i += 1
    return z


def sub(a_list: list[int], y: int, z: int) -> list[int]:
    """Defined a function that shortens a given list to be between given indeces."""
    q: list[int] = []
    if len(a_list) == 0:
        return q
    else:
        while y < z:
            q.append(a_list[y])
            y += 1
        return q