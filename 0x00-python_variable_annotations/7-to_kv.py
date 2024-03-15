#!/usr/bin/env python3
"""a type-annotated function to_kv that takes a string k and an int OR 
float v as arguments and returns a tuple"""
from typing import Union
import math

def to_kv(k : str,v : Union[int, float]) -> tuple:
    """a function takes a string k and an int OR float
     v as arguments and returns a tuple. of string and square of number"""
    
    output = k
    output2 = float(math.pow(v,2))
    total = (output,output2)
    return total
