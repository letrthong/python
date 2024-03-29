# python3  set_interval.py

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(0.001, 'hello')
    await say_after(1, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())