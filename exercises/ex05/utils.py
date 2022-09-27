"""EX05 - Utils."""

__author__: str = "730320104"


def only_evens(x: list[int]) -> list[int]:
    i: int = 0
    for x[i] in x:
        if x[i] % 2 == 0:
            print(x[i])


def concat(x: list[int], y: list[int]) -> list[int]:
    z: list[int] = x + y
    print(z)


def sub(a_list: list[int], y: int, z: int) -> list[int]:
    while y < z:
        print(a_list[y])
        y += 1
