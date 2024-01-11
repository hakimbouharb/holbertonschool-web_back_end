#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""
import asyncio
from time import time

async_generator = __import__('0-async_generator').async_generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run time for four parallel comprehensions
    """
    start_time = time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time()
    return end_time - start_time
