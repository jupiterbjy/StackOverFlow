import asyncio
from aiocfscrape import CloudflareScraper


async def nested(url):
    async with CloudflareScraper() as session:
        async with session.get(url) as resp:
            return await resp.text()


async def main():
    await nested("https://www.binance.com/api/v3/exchangeInfo")


try:
    assert isinstance(loop := asyncio.new_event_loop(), asyncio.ProactorEventLoop)

    async def proactor_wrap(loop_: asyncio.ProactorEventLoop, fut: asyncio.coroutines):
        await fut
        loop_.stop()

    loop.create_task(proactor_wrap(loop, main()))
    loop.run_forever()

except (AssertionError, AttributeError):
    asyncio.run(main())
