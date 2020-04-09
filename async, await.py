import asyncio


async def hello_1():
    print('hello1')
    r = await asyncio.sleep(2)
    print('hello1 again')


async def hello_2():
    print('hello2')
    r = await asyncio.sleep(2)
    print('hello2 again')

task = [hello_1(), hello_2()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
loop.close()