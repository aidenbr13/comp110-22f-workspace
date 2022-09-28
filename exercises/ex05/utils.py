"""EX05 - Utils."""

__author__: str = "730320104"


def only_evens(x: list[int]) -> list[int]:
    """Defined a function that returns even numbers in a given list."""
    i: int = 0
    for x[i] in x:
        if x[i] % 2 == 0:
            print(x[i])



def concat(x: list[int], y: list[int]) -> list[int]:
    """Defined a function that combines the elements of two lists into one longer list."""
    z: list[int] = x + y
    print(z)



def sub(a_list: list[int], y: int, z: int) -> list[int]:
    """Defined a function that shortens a given list to be between given indeces."""
    while y < z:
        print(a_list[y])
        y += 1