def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())  # 9 9 9
# 闭包的内部函数尽量不要使用循环变量。如果一定要使用的话，需要将该变量复制给一个函数作为参数传入
def count():
    fs = []
    def f(j):
        def g():
            return j*j
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print(f1(), f2(), f3())