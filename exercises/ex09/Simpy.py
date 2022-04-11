"""Utility class for numerical operations."""

from __future__ import annotations
# from optparse import Values

from typing import Union

__author__ = "730388033"


class Simpy:
    values: list[float]

    def __init__(self, numbers: list[float]):
        """Initialises values attribute of the Simpy object."""
        self.values = numbers

    def __str__(self) -> str:
        """Returns the list of floats as a str."""
        return f"Simpy({self.values})"

    def fill(self, float_value: float, iterations: int) -> None:
        """Mutates the object and returns the list of values equal to the second argument given."""
        i: int = 0
        while i < iterations:
            self.values.append(float_value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values from the start float to end float number excluding end."""
        assert step != 0.0
        result: list[float] = []
        if stop < 0.0:
            while start > stop:
                result.append(start)
                start += step 
        else:
            while start < stop:
                result.append(start)
                start += step
        self.values = result

    def sum(self) -> float:
        """Takes all items in the values attribute and returns the sum of the items."""
        total: float = 0.0
        for value in self.values:
            total += value
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds the rhs to the Simpy object."""
        result: list[float] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Raises the Simpy object to the rhs power."""
        result: list[float] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Assesses whether self and the rhs are equal to each other and returns a bool."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            for value in self.values: 
                if self.values[i] == rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Assesses whether self is greater than the rhs or not and returns a bool."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            for value in self.values: 
                if self.values[i] > rhs:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        else:
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Using subscription notation on the Simpy object."""
        if isinstance(rhs, int):
            result: float = 0.0
            result = self.values[rhs]
            return result
        else:
            Simpy_result: list[float] = []
            i: int = 0
            while i < len(rhs):
                if rhs[i] is True:
                    Simpy_result.append(self.values[i])
                i += 1
        
        return Simpy(Simpy_result)