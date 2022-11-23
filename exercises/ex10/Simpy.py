"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730320104"


class Simpy:
    """A class calling for a list of floats."""
    values: list[float]

    def __init__(self, list: list[float]) -> None:
        """The constructor function for the Simpy class."""
        self.values = []
        for i in list:
            self.values.append(i)

    def __repr__(self) -> str:
        """A function that uses the overflow method to print the Simpy list."""
        return f"Simpy({self.values})"

    def fill(self, float: float, integer: int) -> None:
        """A function that fills the Simpy list with the integer list of the same float."""
        self.values: list[float] = []
        for i in range(integer):
            self.values.append(float)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """A function that steps from start to finish filling the Simpy list with each new float."""
        assert step != 0
        i: float = start
        if start < stop:
            while i < stop:
                self.values.append(i)
                i += step
        if start > stop:
            while i > stop:
                self.values.append(i)
                i += step

    def sum(self) -> float:
        """A function that sums floats in a Simpy list."""
        sums: float = 0.0
        for i in self.values:
            sums += i
        return sums

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """A function that adds two floats at the same time in different Simpy lists and more."""
        floats: list[float] = []
        new_float: float
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                new_float = self.values[i] + rhs
                floats.append(new_float)
                i += 1
        else:
            assert len(rhs.values) == len(self.values)
            while i < len(rhs.values) and i < len(self.values):
                new_float = self.values[i] + rhs.values[i]
                floats.append(new_float)
                i += 1
        z: Simpy = Simpy(floats)
        return z

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """A function that raises one Simpy list to the power of one or the other."""
        floats: list[float] = []
        new_float: float
        i: int = 0
        if isinstance(rhs, float):
            while i < len(self.values):
                new_float = self.values[i] ** rhs
                floats.append(new_float)
                i += 1
        else:
            assert len(rhs.values) == len(self.values)
            while i < len(rhs.values) and i < len(self.values):
                new_float = self.values[i] ** rhs.values[i]
                floats.append(new_float)
                i += 1
        z: Simpy = Simpy(floats)
        return z

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Function that tests if the floats of a simpy list are equal and more."""
        t_f: list[bool] = []
        t: bool = True
        f: bool = False
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs:
                    t_f.append(t)
                else:
                    t_f.append(f)
                i += 1
        else:
            assert len(rhs.values) == len(self.values)
            i: int = 0
            while i < len(self.values) and i < len(rhs.values):
                if self.values[i] == rhs.values[i]:
                    t_f.append(t)
                else:
                    t_f.append(f)
                i += 1
        return t_f
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """A function that tests if one float is greater than one in a simpy list."""
        greater: list[bool] = []
        t: bool = True
        f: bool = False
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    greater.append(t)
                else:
                    greater.append(f)
                i += 1
        else:
            assert len(rhs.values) == len(self.values)
            i: int = 0
            while i < len(self.values) and i < len(rhs.values):
                if self.values[i] > rhs.values[i]:
                    greater.append(t)
                else:
                    greater.append(f)
                i += 1
        return greater

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """A function that obtains a float at a given index integer."""
        if isinstance(rhs, int):
            f: float = self.values[rhs]
            return f
        else:
            assert len(self.values) == len(rhs)
            l: list[float] = []
            i: int = 0
            while i < len(self.values) and i < len(rhs):
                if rhs[i]:
                    l.append(self.values[i])
                i += 1
            s: Simpy = Simpy(l)
            return s