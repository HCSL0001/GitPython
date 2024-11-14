#获取列表中的多个元素：（切片操作）

#定义一个列表
lst = [10,20,30,40,50,60,70,80]

#start:1 stop:6 step:1 左闭右开[1,6)
print(lst[1:6:1])
print('原列表id:',id(lst))

lst2 = lst[1:6:1]
print('切片列表的id:',id(lst2))

#start不写，默认从0开始；stop不写，默认在结尾结束。step为正数的情况
print(lst[1:6])
print(lst[1:6:])
print(lst[1:6:2])

print(lst[1:4]) #包含1 不包含4
print(lst[:3]) #包含0 不包含3
print(lst[-3:]) #从列表的末尾开始计数
print(lst[::2]) #从0到末尾，步长设置2，所以只提取偶数索引
print(lst[1::2]) #从1到末尾，步长设置2，所以只提取奇数所以
print(lst[::-1]) #反转列表
print(lst[:]) #返回整个列表
