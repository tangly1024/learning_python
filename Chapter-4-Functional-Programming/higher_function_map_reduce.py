# coding=utf-8
# 高阶函数
from functools import reduce

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
list(map(print, ['123', '321', 'abc']))


def f(x):
    """
    返回参数平方
    :param x: 底数
    :return: 平方数
    """
    return x * x


m = map(f, [1, 2, 3, 4, 5])

print(m)

"""
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数f必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# reduce 函数在python3里已经不是 built-in function 需要from functools import reduce.
"""


def f_sn(x, y):
    """
    求和
    :param x:
    :param y:
    :return:
    """
    return x * 10 + y


r = reduce(f_sn, [1, 2, 3, 4, 5])
print(r)


# 使用 map和reduce组合使用
# 完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！
# 这里用到了lambda表示式，匿名函数
def str2int(ss):
    """
    字符串转成完整数字
    :param ss:
    :return:
    """

    def char2num(s):
        """
        字符串转数字
        :param s:
        :return:
        """
        if isinstance(s, int):
            return s
        else:
            DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
            return DIGITS[s]

    # 字符串也可以视为数组
    return reduce(lambda x, y: x * 10 + y, map(char2num, ss))


print(str2int("123131321"))


# 练习
# 转化为首字母大写的标准单词
def normalize(name):
    def toLower(s):
        """
        大写转小写
        :param s:
        :return:
        """
        if 65 <= ord(s) <= 90:  # 大写字母 65-90
            return chr(ord(s) + 32)
        else:
            return s

    def toCapital(s):
        """
        小写转大写
        :param s:
        :return:
        """
        if 97 <= ord(s) <= 122:  # 小写字母97-122
            return chr(ord(s) - 32)
        else:
            return s

    def concat(s1, s2):
        return s1 + s2

    return toCapital(name[0]) + reduce(concat, list(map(toLower, name[1:])))


print(list(map(normalize, ['aisa', 'ameRican'])))
# 用自带的拼接
print(list(map(lambda name: str.capitalize(name[0]) + ''.join(list(map(str.lower, name[1:]))), ['aisa', 'ameRican'])))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
