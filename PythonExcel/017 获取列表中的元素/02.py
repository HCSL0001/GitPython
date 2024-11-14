#定义一个列表
lst = ['hello','world',999,'hello','world',666]

#获取索引为2的元素(正向索引)
print(lst[2])

#获取索引为-3的元素(负向索引)
print(lst[-1])

#获取索引为10的元素
try:
    print(lst[10]) #报错
except:
    print("不存在list[10]")