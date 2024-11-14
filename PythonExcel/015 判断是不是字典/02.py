#使用内置函数isinstance来判断一个对象是否是字典格式

#判断一个对象是否字典
def is_dict(obj):
    return isinstance(obj,dict) #isinstance(obj,list)判断是否为列表

#测试用例
obj1 = {"key":"value"}
obj2 = [1,2,3]
print(is_dict(obj1))
print(is_dict(obj2))