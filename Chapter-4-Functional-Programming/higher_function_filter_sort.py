# coding=utf-8


"""
Filter 过滤序列
map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
"""


def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))


def not_empty(s):
    """
    是否非空
    :param s:
    :return:
    """
    return s and s.strip()


print(list(filter(not_empty, ['123', 'asdf', '', None])))

"""
内置的sorted()函数就可以对list进行排序：
sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
"""

print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

"""
利用高阶函数特性排序tuple
"""
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    x, y = t
    return x


def by_score(t):
    x, y = t
    return y


print(sorted(L, key=by_name))
print(sorted(L, key=by_score))
