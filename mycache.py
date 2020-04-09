# 一个非线程安全的cachedict
import time
from collections import OrderedDict

class LRUCacheDict:  # 近期最少使用算法
    def __init__(self, max_size=1024, expiration=60):
        '''最大容量为1024，缓存有效时间为60s'''
        self.max_size = max_size
        self.expiration = expiration

        self._cache = {}
        self._access_records = OrderedDict()  # 记录访问时间
        self._expire_records = OrderedDict()  # 记录失效时间

    def __setitem__(self, key, value):
        now = int(time.time())
        self.__delete__(key)

        self._cache[key] = value
        self._access_records[key] = now
        self._expire_records[key] = now + self.expiration

        self.cleanup()

    def __getitem__(self, key):
        now = int(time.time())
        del self._access_records[key]

        self._access_records[key] = now
        self.cleanup()

        return self._cache[key]

    def __contains__(self, key):
        self.cleanup()
        return key in self._cache

    def __delete__(self, key):
        if key in self._cache:
            del self._cache[key]
            del self._access_records[key]
            del self._expire_records[key]

    def cleanup(self):
        '''去掉过期或超过存储大小的缓存'''
        if self.expiration is None:
            return None

        pending_delete_key = []
        now = int(time.time())
        for k, v in self._expire_records.items():
            if v < now:
                pending_delete_key.append(k)

        for key in pending_delete_key:
            self.__delete__(key)


        # 如果数据量超出存储大小
        while (len(self._cache) >  self.max_size):
            for k in self._cache:
                self.__delete__(k)
                break


if __name__ == '__main__':
    lrucache = LRUCacheDict(max_size=2, expiration=5)
    lrucache['name'] = 'one'
    lrucache['age'] = 12
    lrucache['sex'] = 'male'

    print('name' in lrucache)
    print('age' in lrucache)

    time.sleep(8)
    print('age' in lrucache)




