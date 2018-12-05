from collections import Iterable

"""
循环
for x in ...
"""

boys = ['哈哈哈', '哟哟哟', '大傻叉']
for boy in boys:
    print(boy)

result = 0
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in num:
    result += n
print(result)
print(sum(num))  # 自带求和函数

"""
range范围类型
可以用list()转化
"""
print(range(1, 10))  # 自带生成数组函数
print(list(range(1, 11)))
print(sum(list(range(1, 11))))

"""
while
break
continue
"""
nums = list(range(1, 101))
results = 0
while len(nums) > 0:
    n = nums.pop(0)
    if n > 10:
        break
    results += n
print(results)

"""
dict 的迭代
"""
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
    print(d[key])

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

for item in d.items():
    print(item)

"""
通过以下方式判断是否可以用for迭代
"""
isinstance('abc', Iterable)  # str是否可迭代

isinstance([1, 2, 3], Iterable)  # list是否可迭代

isinstance(123, Iterable)  # 整数是否可迭代

"""
enumerate 加索引角标
list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对
"""
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

"""
迭代器

可以直接作用于for循环的数据类型有以下几种：
一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为【可迭代对象】：Iterable。


可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

可以使用isinstance()判断一个对象是否是Iterable/Iterator对象：

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

"""

"""
通过iter()函数获得一个Iterator对象。
"""
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
