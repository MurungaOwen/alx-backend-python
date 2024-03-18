#!/usr/bin/env python3
"""module containing async generator"""
import asyncio
from typing import List, Any
import random


async def async_generator():
    """a function to generate random floats
        params:
            None
        return:
            list of random floats
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
