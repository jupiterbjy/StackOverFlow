import asyncio


async def test_assert_ensure_future_called():
    async def increment():
        increment.call_count += 1

    increment.call_count = 0

    tasks = [asyncio.ensure_future(increment()) for _ in range(3)]
    await asyncio.gather(*tasks)

    assert increment.call_count == 3


asyncio.run(test_assert_ensure_future_called())
