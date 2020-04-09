import asyncio

@asyncio.coroutine  # coroutine会把一个生成器标记为coroutine类型，然后通过loop执行
def hello_1():
    print('hello1')
    r = yield from asyncio.sleep(2)
    print('hello1 again')


@asyncio.coroutine
def hello_2():
    print('hello2')
    r = yield from asyncio.sleep(2)
    print('hello2 again')

task = [hello_1(), hello_2()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
loop.close()