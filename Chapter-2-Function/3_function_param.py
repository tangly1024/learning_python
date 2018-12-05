"""
普通参数都是位置参数，按照位置顺序传入
参数组合顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""


def power(x):
    return x * x


"""
函数参数的扩充，
默认参数必须指向不变对象！
默认参数
------------------------------------------
"""


def my_power(x, n=2):
    """
    计算平方
    :param x: 底数
    :param n: 默认计算 平方
    :return:
    """
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s


print(my_power(2))


# 错误
def add_end(L=[]):
    L.append('END')
    return L


# 正确
def add_end_right(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


"""
可变参数
------------------------------------------
java 的...  例如String...
"""


# 普通
def calc_sum(numbers):
    """
    计算数组和
    :param numbers: list或tuple
    :return:
    """
    result = 0
    for n in numbers:
        result += n
    return result


print("计算结果", calc_sum((1, 2, 3, 4)))


# 利用可变参数 * 替换tuple的作用，可以传入任意个参数
def calc_sum_2(*number):
    """

    :type number: 传入多个数字
    """
    result = 0
    for n in number:
        result += n

    return result


print("计算结果，可变参数: ", calc_sum_2(1, 2, 3, 4, 5, 6, 7, 8))

"""
关键字参数
------------------------------------------
**kw  自动组装为dict
类似lambda
"""


def person(name, age, **kw):
    """
    构造一个人
    :param name: 姓名
    :param age: 年龄
    :param kw: 关键字参数
    """
    print('name:', name, 'age:', age, 'other:', kw)


person('哈哈哈哈', 100, test=123, hahah=123)
yo = {'city': 'Beijing', 'job': 'Engineer'}
person('哈哈哈哈', 100, city=yo['city'], job=yo['job'])
# 直接把整个对象当作关键字参数
person('哟哟', 100, **yo)

"""
命名关键字参数
------------------------------------------
特殊分隔符*，*后面的参数被视为命名关键字参数。
若已有一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
"""


def person2(name, *args, age, job):
    print('name', name, 'age:', age, 'job:', job, 'args', args)


person2('周杰伦', 132, 213, 1231, age=123, job=321)

"""
练习
------------------------------------------
"""


def product(*number):
    """
    计算乘积
    :param number:
    :return:
    """
    if not number:
        raise TypeError
    result = 1
    for n in number:
        result *= n
    return result


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

"""
递归
所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
"""


# 阶乘
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)


print(fact(100))  # 会溢出

"""
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：
"""
# 尾递归优化
def fact_new(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact_new(100))
