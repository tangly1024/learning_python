"""
条件判断
"""
"""
布尔
"""
print(not True)
print(True or False)

PI = 3.141592653  # 常量大写 约定俗成
Answer = True
print('Answer: ', Answer, PI)

"""
if代码块
if x:
    print('True')
只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
"""
age = input('请输入你的年龄: ')
print(type(age))  # 默认输入都是str
if int(age) >= 18:  # 冒号结尾表示缩进语句为
    print('你的年龄是 %s , 是个成年人啊' % age)
elif int(age) >= 12:
    print('你的年龄是 %s , 是个青年' % age)
else:
    print('你的年龄是 %s , 还是个小朋友' % age)
