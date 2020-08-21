import asyncio
import time

# @asyncio.coroutine IS DEPRECATED since python 3.8
@asyncio.coroutine
def say_after(wait=True):
    result = []

    if wait:
        print("I'm sleeping!")
        time.sleep(5)
        print("'morning!")
        # This BLOCKs thread, but release GIL so other thread can run.
        # But asyncio runs in ONE thread, so this still harms simultaneity.

    # normal for is BLOCKING operation.
    for i in range(5):
        result.append(i)
        print(i, end='')
    print()

    return result


def main():
    start = time.time()

    # Loop argument will be DEPRECATED from python 3.10
    # Make main() as coroutine, then use asyncio.run(main()).
    # It will be in asyncio Event loop, without explicitly passing Loop.
    loop = asyncio.get_event_loop()
    tasks = say_after(), say_after(False)

    # As we will use asyncio.run(main()) from now on, this should be await-ed.
    a, b = loop.run_until_complete(asyncio.gather(*tasks))

    print(f"Took {time.time() - start:5f}")

    loop.close()


main()
