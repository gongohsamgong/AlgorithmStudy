import asyncio

"""
async def delay(name, seconds):
    await asyncio.sleep(seconds)
    print(name)

async def main():
    tasks = [
        asyncio.create_task(delay('A', 1)),
        asyncio.create_task(delay('B', 2)),
        asyncio.create_task(delay('D', 1)),
        asyncio.create_task(delay('E', 2))
    ]
    print('C')
    await asyncio.gather(*tasks)
    print('F')

asyncio.run(main())
"""


async def delay(name, ms):
    await asyncio.sleep(ms)
    print(name)


if __name__ == "__main__":
    asyncio.gather(
        delay('A', 1),
        delay('B', 1)
    )
    # asyncio.run(delay('A', 1))
    # asyncio.run(delay('B', 1))
    print('C')
