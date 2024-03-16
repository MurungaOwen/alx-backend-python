#!/usr/bin/env python3
from typing import Callable
""" a module that has type-annotated function
make_multiplier that takes a float multiplier"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier."""
    def multiply_function(value: float) -> float:
        return value * multiplier
    return multiply_function
