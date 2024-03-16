#!/usr/bin/env python3
from typing import List, Union
"""a module that makes a type-annotated function sum_mixed_list
    which takes a list mxd_lst of integers and
floats and returns their sum as a float."""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """a function that add ups a list of
    either float or integers"""
    sum = 0.0
    for i in mxd_lst:
        sum += i
    return sum
