# coding=utf-8
"""
切片
取list或tuple的部分
倒数第一个元素的索引是-1。
"""

L = ['yooo', 'hhah', 'mamamam', 'oooo']
print(L[0:2])  # 从第0个到2
print(L[:1])  # 取第一个
print(L[-3:-1])  # 取倒3到倒1

L = list(range(1, 101))
print(L[-10:])

"""
甚至什么都不写，只写[:]就可以原样复制一个list：
"""
P = L[:]
print(P)

"""
tuple也可以用切片操作，只是操作的结果仍是tuple：
'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
"""

print((0, 1, 2, 3)[-2:])
print('ABCDEFGHIJKLMN'[-3:-1])
