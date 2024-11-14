#字典对象有一个特有的方法item，该方法返回字典的键值对。我们可以利用这一特性来判断一个对象是否是字典

#判断一个对象是否字典
def is_dict(obj):
    try:
        obj.items()
        return True
    except AttributeError:
        return False

#测试用例
obj1 = {"key":"value"}
obj2 = [1,2,3]
print(is_dict(obj1))
print(is_dict(obj2))