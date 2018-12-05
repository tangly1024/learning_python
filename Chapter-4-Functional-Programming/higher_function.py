# coding=utf-8
# 高阶函数

"""
变量可指向函数
函数名其实就是指向函数的变量
"""
abs(1)
f = abs
print(f(-1))

"""
传入函数
既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
"""


def my_add(x, y, f):
    """
    自定义加法
    :param x: 参数一
    :param y: 参数二
    :param f: 对参数处理的函数
    :return:
    """
    return f(x) + f(y)


print(my_add(-1, -2, abs))

"""
Map/Reduce
"""

"""
map()函数接收两个参数，一个是函数，一个是Iterable
map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
Iterator 有点类似generator 可以使用next() list() 进行取出
"""


def f(x):
    """
    返回参数平方
    :param x: 底数
    :return: 平方数
    """
    return x * x


m = map(f, [1, 2, 3, 4, 5])

print(m)
