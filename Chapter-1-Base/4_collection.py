# coding=utf-8
"""
集合列表
list tuple
对比dict set查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
"""

"""
list
len()
insert()
append()
pop() # 推出指定位置，默认最后;删除取出
sort() 只能排序同一种类型
"""
birds = ['A', True, 666]
print(len(birds))
print(birds[0])
print(birds[len(birds) - 1])  # 取最后一个元素
print(birds[-1])  # 加负号表示倒数
birds.append('yo')
birds.insert(1, '哈哈哈哈')  # 指定位置插入
birds.insert(0, 'go')  # 指定位置插入
AA = birds.pop(1)  # 推出1
print(AA)
birds[0] = 666  # 替换某一个值
print(birds)

"""
tuple 
tuple的每个元素，指向永远不变。
无法单独修改，没有insert()append()；对比list有一定安全性
若要定义只有一个对象的tuple需要尾部加逗号,
"""
box = ('yoyo', 'yaya', '666')
print(box)
t = (1,)
print(t)

"""
可变的tuple
"""
t = ('a', 'b', ['A', 'B'])
