#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple
"""module to define element_length"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function to return length of first"""
    return [(i, len(i)) for i in lst]
