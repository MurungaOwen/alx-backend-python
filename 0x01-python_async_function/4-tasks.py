#!/usr/bin/env python3
"""
Module containing function similar to
wait_n
"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> list:
    """function that ges randm numbers
        in loop
        params:
            n which is loop times
        return:
            a list of values
    """
    result = await wait_n(n, max_delay)
    return result
