# coding=utf-8
"""
函数作为返回值
“闭包（Closure）” 相关参数和变量都保存在返回的函数
"""

"""
举例，可变参求和函数
"""


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3)
f()

"""
闭包引用循环变量
返回函数不要引用任何循环变量，或者后续会发生变化的变量。
如果一定要引用循环变量？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
"""


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


# 闭包练习
# 创建一个独立组建
def createCounter():
    def counter(x):
        while True:
            yield x
            x += 1

    x = 1
    g = counter(x)

    def get():
        return next(g)

    return get


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


"""
lambda
"""

"""
以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
"""
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

f = lambda x: x * x
print(f(2))


# 也可以返回函数
def build(x, y):
    return lambda: x * x + y * y


ff = build(1, 2)
print(ff())
