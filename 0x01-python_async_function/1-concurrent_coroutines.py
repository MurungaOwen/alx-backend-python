#!/usr/bin/env python3
"""executing multiple coroutines"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """async function to loop through and
        produce random input
        params:
            n which is number of times
        return:
            list of random values
    """
    myList = [await wait_random(max_delay) for i in range(n)]
    return myList
