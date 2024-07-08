#!/usr/bin/env python3
"""module documentation"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns list of delays"""
    lDelays = []
    for _ in range(n):
        lDelays.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*lDelays))
