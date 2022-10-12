"""EX07 - Dictionary."""

__author__: str = "730320104"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Created a function that inverts a given dictionary."""
    z: dict[str, str] = {}
    key: str = ""
    for key in x:
        if x[key] in z:
            raise KeyError("Encountered a repeating key")
        else:
            z[x[key]] = key
    return (z)


def favorite_color(x: dict[str, str]) -> str:
    """Created a function that returns the value (color) that appears most frequently."""
    m: int = 0
    p: str = ""
    z: dict[str, int] = {}
    for key in x:
        if x[key] in z:
            z[x[key]] += 1
        else:
            z[x[key]] = 1
    for key in z:
        if z[key] > m:
            m = z[key]
            p = key
        else:
            p = p
    return p


def count(x: list[str]) -> dict[str, int]:
    """Created a function that counts the number of times a value appeared in a given list."""
    z: dict[str, int] = {}
    for item in x:
        if item in z:
            z[item] += 1
        else:
            z[item] = 1
    return z