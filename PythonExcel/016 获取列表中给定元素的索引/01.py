#使用内置函数index()

#定义一个列表
my_list = ['apple','banana','cherry','date','fig']

#找到'banana'的索引
index_of_banana = my_list.index('banana')

print("The index of 'banana' is:",index_of_banana)

#从指定位置开始查找
index_of_cherry = my_list.index('cherry',2)
print("The index of 'cherry' starting from index 2 is:",index_of_cherry)

#处理找不到元素的情况
try:
    index_of_grape = my_list.index('grape')
except ValueError:
    print("'grape' is not in the list.")