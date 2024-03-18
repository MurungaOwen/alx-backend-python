#!/usr/bin/env python3
"""a module on async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """function to return list generated random
    nums
    params:
        None
    return:
        List of float
    """
    random_numbers = [number async for number in async_generator()]
    return random_numbers
