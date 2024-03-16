#!/usr/bin/env python3
"""module containig to_kv"""


import math
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """get power of number and string"""
    return k, math.pow(v, 2)
