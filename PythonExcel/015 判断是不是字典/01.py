#使用python内置函数type来判断一个对象的类型是否为字典。如果对象是字典，则typy(obj)的返回值应该是dict

#判断一个对象是否字典
def is_dict(obj):
    return type(obj) is dict

#测试用例
obj1 = {"key":"value"}
obj2 = [1,2,3]
print(is_dict(obj1))
print(is_dict(obj2))