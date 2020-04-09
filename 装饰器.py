import functools


def derector(func):
    @functools.wraps(func)  # 不加该修饰的话，now.__name__将会是wrapper
    def wrapper(*args, **kwargs):
        print('执行:',  func.__name__)
        return func(*args, **kwargs)
    return wrapper


@derector
def now():
    print('now:11:39')


now()
print(now.__name__)


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')





class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, value):
        return Chain('%s/%s' % (self._path, value))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain())
print(Chain().users)
print(Chain()('michael'))
print(Chain().users('michael').repos) # /users/michael/repos


