#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 开头加上两行表示当前代码的编码方式

"""
字符串编码
Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
知道整数编码，还可以用十六进制写str
len()计算字符数
"""
print(ord('中'))
print(chr(20013))
print('\u4e2d\u6587')
print(len('中文'))

"""
字节 bytes
encode()
decode()
len() 计算字节数
replace()
"""
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
bABC = b'ABC'
print(bABC)
print(len(bABC))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('中文'.encode('utf-8')))

"""
格式化 占位符% 连接符号%
%d	整数
%f	浮点数
%s	字符串 %s永远起作用，它会把任何数据类型转换为字符串
%x	十六进制整数
%%  转义
"""
print('Hello, %s' % 'world')
print('%s是%s , 今年%d岁' % ('周杰伦', '天才', 30))

"""
除法 
/ 浮点除
// 地板除
%  求余
"""
s1 = 72
s2 = 85
print('小明成绩 去年%s 今年%s  提升了%2.1f%%' % (s1, s2, (s2 - s1) / s2 * 100))

"""
字符串对象不可变
"""
a = 'abc'
b = a.replace('a', 'A')
print(a)  # a还是原来的
print(b)  # b生成新的对象引用
