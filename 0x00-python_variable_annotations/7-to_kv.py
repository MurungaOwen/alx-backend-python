#!/usr/bin/env python3
"""module containig to_kv"""
import math
from typing import Union

def to_kv(k : str,v : Union[int, float]) -> tuple:
    """get power of number and string"""  
    output = k
    output2 = float(math.pow(v,2))
    total = (output,output2)
    return total
