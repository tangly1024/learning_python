# coding=utf-8
"""
函数对象有一个__name__属性，可以拿到函数的名字
在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
"""
import functools
import time

"""
本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
"""


def log_simple(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        # wrapper.__name__ = func.__name__
        return wrapper

    return decorator


@log_simple('execute')
def now():
    return '2018-10'


f = now
print(f())
print(now.__name__)
print(f.__name__)

"""
把@log放到now()函数的定义处，相当于执行了语句：

now = log(now)

首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：

可以使用@functools.wraps(func) 确保函数名
"""

"""
装饰器练习 注解
可作用于任何函数上，并打印该函数的执行时间：
"""


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        res = func(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, end - start))
        return res

    # wrapper.__name__ = func.__name__
    return wrapper


def log(*args):
    def decorator(func):
        def wrapper(*args, **kw):
            print('begin call')
            print('%s %s():' % (text, func.__name__))
            f = func(*args, **kw)
            print('end call')
            return f

        return wrapper

    if len(args) == 1 and callable(args[0]):
        text = 'call'
        return decorator(args[0])
    else:
        text = args[0]
        return decorator


"""
写出一个@log的decorator，使它既支持：

@log
def f():
    pass
又支持：

@log('execute')
def f():
    pass
    """


# 测试
@metric
@log
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)

print(f)
print(s)
