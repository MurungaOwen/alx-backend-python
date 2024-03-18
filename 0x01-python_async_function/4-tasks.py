#!/usr/bin/env python3
"""
Module containing function similar to
wait_n
"""
import typing
wait_r = __import__('0-basic_async_syntax').wait_random
task_wait_r = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """function that ges randm numbers
        in loop
        params:
            n which is loop times
        return:
            a list of values
    """
    myList = []
    for i in range(n):
        task = task_wait_r(await wait_r(max_delay))
        result = await task
        myList.append(result)

    return myList
