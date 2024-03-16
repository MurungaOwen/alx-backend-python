#!/usr/bin/env python3
from typing import Any, TypeVar, Union, Mapping
"""module that has safely get value function"""


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> Union[Any, T]:
    """using default values"""
    if key in dct:
        return dct[key]
    else:
        return default
  