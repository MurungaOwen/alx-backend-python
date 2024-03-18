#!/usr/bin/env python3
import asyncio
import random
"""module containing coroutine"""


async def wait_random(max_delay: int = 10) -> float:
    """function uses random module to wait for a random delay
    and returns it
    params:
        max_delay wich is time to sleep
    return:
        return a random float
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
