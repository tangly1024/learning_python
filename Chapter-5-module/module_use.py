# coding=utf-8
""" a test module"""

__author__ = 'TangHH'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello,world!")
    elif len(args) == 2:
        print('Hello, %s !' % args[1])
    else:
        print("too many arguments")


"""
当我们在命令行运行hello模块文件时，Python解释器把特殊变量__name__置为__main__，
而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
"""
if __name__ == '__main__':
    test()

"""
运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael]
"""


"""
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

"""
