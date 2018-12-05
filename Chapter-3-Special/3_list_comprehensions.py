# coding=utf-8
import os  # 引入系统库

"""
代替循环遍历生成列表
直接在 [] 中写表达式
"""
ll = [x * x for x in range(1, 11)]
print(ll)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 11) if x % 2 == 0])

# 两层循环
print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('../')])

"""
for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
"""
d = {'x': 'A', 'y': 'B', 'z': "C"}
td = [k + '=' + v for k, v in d.items()]
print(td)

"""
练习
转为小写
"""
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [text.lower() for text in L1 if isinstance(text, str)]
print(L2)
