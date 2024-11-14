import json
# 代码有问题
# 原始JSON数据
json_data = {
    "name":"John",
    "age":30,
    "address":{
        "city":"New York",
        "state":"NY",
        "country":"USA"
    }
}

# 将JSON转换为Python对象
data = json.loads(json_data)

# 定义递归函数删除节点
def delete_node(ndoe,key):
    if key in node:
        del node[key]
    elif isinstance(node,dict):
        for k,v in node.items():
            if isinstance(v,(dict,list)):
                delete_node(v.key)
    elif isinstance(node,list):
        for item in node:
            if isinstance(item,(dict,list)):
                delete_node(item,key)

# 删除address节点
delete_node(data,'address')

# 将Python对象转换为JSON
json_result = json.dump(data)

print(json_result)