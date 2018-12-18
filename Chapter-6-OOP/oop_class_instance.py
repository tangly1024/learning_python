# coding=utf-8

"""
demo
"""


class Student(object):
    """
    学生类
    """

    def __init__(self, name, score, sex):
        self.name = name
        self.score = score
        self.__sex = sex

    def print_score(self):
        """
        打印分数
        """
        print("%s: %s" % (self.name, self.score))

    def getSex(self):
        return self.__sex

    def setSex(self, sex):
        self.__sex = sex

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        if self.score >= 60:
            return 'B'
        else:
            return 'C'


zhoujielun = Student('周杰伦', 100, "男")

zhoujielun.print_score()
print(zhoujielun)

print(zhoujielun.getSex())
zhoujielun.setSex("女")
print(zhoujielun.getSex())
zhoujielun.score = 99
zhoujielun.print_score()
print(zhoujielun.get_grade())
print(zhoujielun)

"""
特殊方法 __init__ 第一个参数永远是self
"""

"""
访问限制
如果要让内部属性不被外部访问，属性前面加上两个下划线__ 然后提供set() get()方法一遍访问和检查
"""


