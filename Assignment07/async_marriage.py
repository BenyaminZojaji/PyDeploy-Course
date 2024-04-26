import time
import asyncio
import random


async def marriage(name):
    r = random.randint(0, 10)
    await asyncio.sleep(r)
    print(f"{name} married after {r} years.")


async def main():
    await asyncio.gather(marriage("Benyamin"), marriage("Jack"), marriage("David"), marriage("alex"))


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"Executed in {elapsed:0.3f} seconds.")