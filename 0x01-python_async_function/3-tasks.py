#!/usr/bin/env python3
"""module containing function with tasks"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """function to return an asyncio task
    params:
        max_delay which is sleep time
    return:
        instance of asyncio task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
