def customer():
    r = ''
    print(1111111111)
    while True:
        n = yield r  # yield不仅可以赋值，还可以接受传入的参数。customer.send(6), 则n被赋值为6
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 ok'


def product(c):
    print(2222222222222)
    c.send(None)  # 启动生成器c
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = customer()  # 如果一个函数写成了生成器，则该过程不会执行customer[不会打印11111],而普通函数则会打印。
product(c)

'''
2222222222222
1111111111
[PRODUCER] Producing 1...
[CONSUMER] Consuming 1...
[PRODUCER] Consumer return: 200 ok
[PRODUCER] Producing 2...
[CONSUMER] Consuming 2...
[PRODUCER] Consumer return: 200 ok
[PRODUCER] Producing 3...
[CONSUMER] Consuming 3...
[PRODUCER] Consumer return: 200 ok
[PRODUCER] Producing 4...
[CONSUMER] Consuming 4...
[PRODUCER] Consumer return: 200 ok
[PRODUCER] Producing 5...
[CONSUMER] Consuming 5...
[PRODUCER] Consumer return: 200 ok
'''
