# 查找全体素数
'''
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

首先，列出从2开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：

3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：

5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取新序列的第一个数5，然后用5把序列的5的倍数筛掉：

7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

不断筛下去，就可以得到所有的素数。
'''
def init_add():  # 构造一个从3开始的奇数序列
    n = 3
    yield n
    while True:
        n += 2
        yield n


def not_divisible(n):  # 筛选函数
    return lambda x: x % n > 0


def primes():  # 定义生成器，不断返回下一个素数
    yield 2  # 2是第一个素数
    nums = init_add()
    while True:
        num = next(nums)
        yield num  # 返回序列的第一个数
        nums = filter(not_divisible(num), nums)


sushu = primes()
for i in range(10):
    print(next(sushu))
