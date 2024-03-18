#!/usr/bin/env python3
"""module containing function to measure
    execution time
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """mesures total time for execution"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    duration = end - start
    return duration / n
