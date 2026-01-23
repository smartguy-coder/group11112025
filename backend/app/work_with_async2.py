import time
import asyncio


async def hello():
    print('Hello world')
    time.sleep(2)
    print('Hello again')


# asyncio.run(hello())

# hello()
# print(1111111)
# hello()
# hello()
# hello()

async def hello2():
    print('Hello world')
    await asyncio.sleep(2)
    print('Hello again')


async def foo(n):
    print(f'from foo before {n}')
    await asyncio.sleep(10)
    print('from foo after')


# asyncio.run(hello2())

async def main():
    await asyncio.gather(
        foo(6),
        foo(8),
        hello2(),
        hello2(),
        hello2(),
        hello2(),
        hello2(),
        hello2(),
        hello2(),
    )

asyncio.run(main())