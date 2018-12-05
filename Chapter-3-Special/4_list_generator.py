# coding=utf-8
"""
列表生成器
一次性生成整个列表浪费内存空间，可以用生成器推算出下一个列表元素
生成列表的[] 替换成 () 就是一个生成器
"""
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(next(g))

for n in g:
    print(n)

"""
generator 底层是一个 yield返回
在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
注意区分普通函数和generator函数，普通函数调用直接返回结果：
generator函数的“调用”实际返回一个generator对象：
"""


# 杨辉三角生成器
def triangles():
    pre_list = [1]
    yield pre_list
    pre_list = [1, 1]
    yield pre_list
    while True:
        cur_list = [1]
        index = 1
        while index < len(pre_list):
            cur_list.append(pre_list[index - 1] + pre_list[index])
            index += 1
        cur_list.append(1)
        pre_list = cur_list
        yield cur_list


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n += 1
    if n == 10:
        break
