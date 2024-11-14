#获取元素的索引

#定义一个列表
lst = ['hello','world',999,'hello']
print(lst.index('hello')) #如查列表中含有多个相同元素，则只返回相同元素中的第一个元素的索引
print(lst.index('hello',1,4)) #从索引1到4查询'hello'的索引，[1,4)，不包含4，即从1到3