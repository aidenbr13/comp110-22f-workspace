"""EX05 - Utils."""

__author__: str = "730320104"


def only_evens(x: list[int]) -> list[int]:
    """Defined a function that returns even numbers in a given list."""
    i: int = 0
    z: list[int] = []
    for x[i] in x:
        if x[i] % 2 == 0:
            z.append(x[i])
    return z



def concat(x: list[int], y: list[int]) -> list[int]:
    """Defined a function that combines the elements of two lists into one longer list."""
    i: int = 0
    z: list[int] = []
    for x[i] in x:
        z.append(x[i])
    for y[i] in y:
        z.append(y[i])
    return z



def sub(a_list: list[int], y: int, z: int) -> list[int]:
    """Defined a function that shortens a given list to be between given indeces."""
    q: list[int] = []
    while y < z:
        q.append(a_list[y])
        y += 1
    return q