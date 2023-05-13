import asyncio

async def async_generator():
    for i in range(5):
        yield i
        await asyncio.sleep(1)

async def main():
    async for num in async_generator():
        print(num)
    raise StopAsyncIteration

try:
    asyncio.run(main())
except StopAsyncIteration:
    print("Async iterator telah selesai.")