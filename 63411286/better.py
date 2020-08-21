import asyncio
import time


async def say_after(wait=True):
    result = []

    if wait:
        print("I'm sleeping!")
        await asyncio.sleep(2)  # 'await' a coroutine version of it instead.
        print("'morning!")

    # wrap iterator in generator - or coroutine
    async def asynchronous_range(end):
        for _i in range(end):
            yield _i

    # use it with async for
    async for i in asynchronous_range(5):
        result.append(i)
        print(i, end='')
    print()

    return result


async def main():
    start = time.time()

    tasks = say_after(), say_after(False)
    a, b = await asyncio.gather(*tasks)

    print(f"Took {time.time() - start:5f}")


asyncio.run(main())
