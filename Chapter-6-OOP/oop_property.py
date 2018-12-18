# coding=utf-8
"""
如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数
"""


class Student(object):

    def get_score(self):
        """

        :return:
        """
        return self._score

    def set_score(self, value):
        """

        :param value:
        """
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(999)
print(s.get_score())

"""
装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的
"""


class MyStudent(object):
    """
    我的学生
    """
    def __init__(self,value):
        self._score = value

    @property
    def score(self):
        """

        :return:
        """
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
