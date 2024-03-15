#!/usr/bin/env python3
from typing import List

"""a module that makes type-annotated function sum_list 
which takes a list input_list of floats as argument and returns their sum as a float."""

def sum_list(input_list : List[float]) -> float:
    """function that adds a list of float values"""
    sum : float = 0
    for i in input_list :
        sum += i
    return sum

