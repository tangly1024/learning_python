# coding=utf-8
"""
继承
"""


class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self, place):
        """
        跑去哪儿呢
        :param place:
        """
        print("Cat is running to %s" % place)

    def eat(self):
        """
        吃鱼
        """
        print("Cat eating fish")


# 只要传入的参数有run方法就可以，不用管他是什么类型的
# 动态语言的鸭子特性 如果走起路来像鸭子，叫起来也像鸭子，那么它就是鸭子
def run_twice(animal):
    if (not isinstance(animal, Animal)):
        raise TypeError('不行呀，参数只能是动物Animal')
    animal.run()
    animal.run()


dog1 = Dog()
dog1.run()

cat1 = Cat()
cat1.run('school')
cat1.eat()

a = list()
b = Animal()
c = Dog()
"""
继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行
以下为true
"""
isinstance(a, list)
isinstance(b, Animal)
isinstance(c, Dog)
isinstance(c, Animal)
"""
以下为false
"""
bb = Animal()
isinstance(b, Dog)

run_twice(c)
