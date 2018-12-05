"""
dict
相当于键值对map，dict的key必须是不可变对象不能是list。。
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

in 判断是否存在
get() 获取
pop() 删除
"""
yo = {'周杰伦': '猛男', '周星驰': '猛虎', '刘德华': None}
print(yo['周杰伦'])

print('周杰伦' in yo)
print(yo['刘德华'])

print(yo.pop('周杰伦'))
print(yo)

"""
当key不存在的情况
get() 默认返回None
"""
print(yo.get('呀哈', '不存在呀'))

"""
set
不存储value,需要提供一个list作为输入集合;同样不可以放入可变对象
s = set([1, 2, 3])语法里没有value的dict自动转为set

add()添加,重复不会生效
remove()
pop()
"""
s = {1, 1, 1, 1, 1, 2, 2, 2, 2}
s.add(3)
s.remove(1)
s.pop()
print(s)

"""
不可变对象作为key很重要，最常用的key是字符串
tuple也不能作为key
"""
