# coding=utf-8
import functools

"""
functools模块提供了很多有用的功能，其中一个偏函数（Partial function）
"""

# 2进制转整数
print(int('1000000', base=2))


def int_2(x, base=2):
    return int(x, base)


print(int_2('1000001'))

"""
functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
"""
int2 = functools.partial(int, base=2)

int2('10010')
# 相当于
kw = {'base': 2}
int('10010', **kw)

max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：

max2(5, 6, 7)
# 相当于：

args = (10, 5, 6, 7)
max(*args)
