import asyncio
from random import uniform


async def some_work():
    await asyncio.sleep(t := uniform(1.5, 1.9))
    return f"slept {t:.2f}"


async def timeout_wrapper(idx, coroutine, timeout):
    try:
        msg = await asyncio.wait_for(coroutine, timeout)
    except asyncio.TimeoutError:
        msg = "Timeout!"

    return f"Worker {idx:2}: {msg}"


async def create_tasks(worker_timeout=1.7, gather_timeout=1):
    tasks = [
        timeout_wrapper(i, some_work(), worker_timeout)
        for i in range(10)
    ]

    try:
        result = await asyncio.wait_for(asyncio.gather(*tasks), gather_timeout)
    except asyncio.TimeoutError:
        result = 'Timeout on gather'
    except asyncio.CancelledError:
        result = 'gather canceled.'
    else:
        return result


async def main():
    print(await create_tasks())

asyncio.run(main())
