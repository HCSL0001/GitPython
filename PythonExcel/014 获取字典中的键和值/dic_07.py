#使用pop()方法可以删除字典中指定键的键值对，并返回对应的值

#定义一个字典
my_dict = {"name":"Tom","age":18,"gender":"male"}

#删除字典中age中对应的值，并返回对应的值
valua = my_dict.pop("age")
print(valua)
print(my_dict)