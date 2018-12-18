# coding=utf-8

from oop_class_extend_polymorphism import Animal
from oop_class_extend_polymorphism import Cat

"""

判断对象类型，使用type()函数
"""

print(type(123) == int)

"""
能用type()判断的基本类型也可以用isinstance()判断：
class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
"""

print(isinstance([1, 2, 3], (list, tuple)))
a = Animal()
b = Cat()

print(isinstance(a, (Animal, Cat)))

"""
仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
"""


class MyObject(object):
    def __init__(self, x=8):
        self.x = x

    def power(self):
        """

        :return:
        """
        return self.x * self.x


obj = MyObject()
"""
使用dir()
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()
"""
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
print(getattr(obj, 'x'))
print(setattr(obj, 'x', 99))
print(getattr(obj, 'x'))
print(getattr(obj, 'y', 404))
print(setattr(obj, 'y', 99))
print(getattr(obj, 'y', 88))
print(dir(obj))

"""
正确的用法

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
"""
