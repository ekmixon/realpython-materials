#!/usr/bin/env python3
# rand.py

import asyncio
import random

# colors
c = (
    "\033[0m",  # end of color
    "\033[36m",  # cyan
    "\033[91m",  # red
    "\033[35m",  # magenta
)


async def randint(a: int, b: int) -> int:
    return random.randint(a, b)


async def makerandom(idx: int, threshold: int = 6) -> int:
    print(f"{c[idx + 1]}Initiated makerandom({idx}).")
    i = await randint(0, 10)
    while i <= threshold:
        print(f"{c[idx + 1]}makerandom({idx}) == {i} too low; retrying.")
        await asyncio.sleep(idx + 1)
        i = await randint(0, 10)
    print(f"{c[idx + 1]}---> Finished: makerandom({idx}) == {i}{c[0]}")
    return i


async def main():
    res = await asyncio.gather(*(makerandom(i, 10 - i - 1) for i in range(3)))
    return res


if __name__ == "__main__":
    random.seed(444)
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
