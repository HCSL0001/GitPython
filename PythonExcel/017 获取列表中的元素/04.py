#定义一个列表
my_list = [1,2,3,4,5,6,7,8,9,10]

#使用slice()函数对列表经行切片
s = slice(2,8,2)
new_list = my_list[s]

#打印切边结果
print(new_list) #等同print(my_list[2:8:2])

s1 = slice(None,5) #相当于[:5]
s2 = slice(2,None) #相当于[2:]
s3 = slice(None,None,2) #相当于[::2]

print(my_list[s1])
print(my_list[s2])
print(my_list[s3])

#负数索引
s4 = slice(-5,-1) #相当于[-5:-1]
print(my_list[s4])