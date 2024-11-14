#使用popitem()方法可以删除字典中的任意一个键值对，并返回对应的键值对，返回的是一个元组，元组的第一个元素是键，第二个元素是值

#定义一个字典
my_dict = {"name":"Tom","age":18,"gender":"male"}

#删除字典中的任意一个键值对，并返回对应的键值对
key,valua = my_dict.popitem()
print(key,valua)
print(my_dict)