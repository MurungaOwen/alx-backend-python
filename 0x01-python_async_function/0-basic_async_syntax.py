#!/usr/bin/env python3
import asyncio
import random
"""module containing coroutine"""


async def wait_random(max_delay: int = 10) -> float:
    """async function for random delay
    :params-delay which is integer
    :return
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
