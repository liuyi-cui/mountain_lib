# 统计函数运行时间的装饰器
import time


def cal_time(func):

    def wrap(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        print('运行%s 耗时%.2f' % (func.__name__, time.time()-st))
        return res
    return wrap

