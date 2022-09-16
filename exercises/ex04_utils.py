"""EX04 - Utils!"""

__author__: str = "730320104"

from random import randint

def all(x: list[int], y: int) -> bool:
    i: int = 0
    while i < len(x):
        if x[i] == x[i+1] == x[len(x)-1] == y:
            i= i + 1
            return True
        else:
            return False

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    z: int = input[i]
    while z < len(input):
        if z < input[i+1]:
            z= input[i+1]
            i= i + 1
        else:
            i= i + 1
    print(z)

def is_equal(a: list[int], b: list[int]) -> bool:
    if a == b:
        return True
    else:
        return False