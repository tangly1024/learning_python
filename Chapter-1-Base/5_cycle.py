"""
循环
for x in ...
"""

boys = ['哈哈哈', '哟哟哟', '大傻叉']
for boy in boys:
    print(boy)

result = 0
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in num:
    result += n
print(result)
print(sum(num))  # 自带求和函数

"""
range范围类型
可以用list()转化
"""
print(range(1, 10))  # 自带生成数组函数
print(list(range(1, 11)))
print(sum(list(range(1, 11))))

"""
while
break
continue
"""
nums = list(range(1, 101))
results = 0
while len(nums) > 0:
    n = nums.pop(0)
    if n > 10:
        break
    results += n
print(results)
