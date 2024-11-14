#使用字典的get(方法)

#举例01
dictionary = {"key1":"valuel","key2":"value2"}
value01 = dictionary.get("key1")
print(value01)

#举例02
#定义一个字典
my_dict = {"name":"Tom","age":18,"gender":"male"}

#获取字典中"name"键对应的值
value02 = my_dict.get("name")
print(value02)

#获取字典中"phone"键对应的值，由于"phone"不存在，返回None
value02 = my_dict.get("phone")
print(value02)