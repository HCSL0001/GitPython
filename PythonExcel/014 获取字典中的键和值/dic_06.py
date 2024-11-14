#使用in关键字可以判断一个键是否在字典中，如果在则返回True，否则返回False

#定义一个字典
my_dict = {"name":"Tom","age":18,"gender":"male"}

#判断name是否在字典中
if "name" in my_dict:
    print("name is in my_dict")

#判断phone是否在字典中
if "phhone" in my_dict:
    print("phone is in my_dict")
else:
    print("phone is not in my_dict")