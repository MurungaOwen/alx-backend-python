#!/usr/bin/env python3
"""module containig to_kv"""
import math
import typing

def to_kv(k : str,v : typing.Union[int, float]) -> tuple[str,float]:
    """get power of number and string"""  
    return (k,float(math.pow(v,2)))
