#使用enumerate()函数和列表推导式来找到元素的索引

#定义一个列表
my_list = ['apple','banana','cherry','date','fig']

#使用enumerate()遍历列表和索引
for index,fruit in enumerate(my_list):
    if fruit == 'date':
        print("The index of 'date' is:",index)
        break

#使用列表推导式找到所有匹配元素的索引
indexes_of_fig = [index for index,fruit in enumerate(my_list) if fruit == 'fig']
print("Indexes of 'fig':",indexes_of_fig)