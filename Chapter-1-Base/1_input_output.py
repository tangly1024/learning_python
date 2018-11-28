"""
建议一边开启解释器模式；一边开着编译执行模式调试
"""
"""
 输出
"""
print('hello,world')  # 注释测试

"""
输入
"""
name = input('请输入你的名字: ')
print('你好啊,', name)  # 注释测试

"""
字符转义
"""
print('I\'m ok.')
# r'' 表示不转义
print(r'\\\\\\\\\\')

"""
多行输出
"""
print('''周杰伦 
123
345
567''')

"""
类型转换
int(x [,base ])         将x转换为一个整数  
long(x [,base ])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数  
complex(real [,imag ])  创建一个复数  
str(x )                 将对象 x 转换为字符串  
repr(x )                将对象 x 转换为表达式字符串  
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               将序列 s 转换为一个元组  
list(s )                将序列 s 转换为一个列表  
chr(x )                 将一个整数转换为一个字符  
unichr(x )              将一个整数转换为Unicode字符  
ord(x )                 将一个字符转换为它的整数值  
hex(x )                 将一个整数转换为一个十六进制字符串  
oct(x )                 将一个整数转换为一个八进制字符串
"""
