# coding=utf-8
from types import MethodType

"""
给一个实例绑定的方法，对另一个实例是不起作用的：
"""

"""
但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
"""


class Student(object):
    pass


def set_age(self, age):
    self.age = age


def get_age(self):
    return self.age


s = Student()
# 将方法绑定到对象上
s.set_age = MethodType(set_age, s)
s.get_age = MethodType(get_age, s)
s.set_age(25)
print(s.age)
print(s.get_age())

"""
为了给所有实例都绑定方法，可以给class绑定方法：

"""


def set_score(self, score):
    self.score = score


Student.set_score = set_score

s.set_score(100)
print(s.score)


"""
Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
"""
class MyStudent(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

    pass


ms = MyStudent()
# ms.test = set_age  # 这个不能设置
