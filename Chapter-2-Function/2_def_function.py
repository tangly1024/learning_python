# coding=utf-8
import math


def yoyoyo(name):
    """

    :param name:
    :return:
    """
    if not isinstance(name, (str, int, float)):
        raise TypeError('不行呀，参数只能是字符还有数字')
    return '哈哈哈哈你好吗～～～ %s' % name


def nop():
    pass  # 这里还没想好怎么写，用pass占位
    print("这里还没想好怎么写")


print(yoyoyo('周杰伦'))
try:
    print(yoyoyo(b'123'))
except TypeError:
    print('上面这个方法异常啦👆')
print(nop())

"""
允许回多个值
其本质是返回一个省略括号的tuple
math 库已经在top引入
"""


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)
x, y = move(100, 100, 60, math.pi / 6)
print(r)
print(x, y)
