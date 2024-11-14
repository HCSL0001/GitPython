import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "friends": [
        {
            "name": "Alice",
            "age": 28,
            "city": "London"
        },
        {
            "name":"Bob",
            "age":32,
            "city":"Paris"
        }
    ]
}

# 递归函数
def get_node_value(node, key):
    if isinstance(node, dict):
        if key in node:
            return node[key]
        for k, v in node.items():
            result = get_node_value(v, key)
            if result is not None:
                return result
    elif isinstance(node, list):
        for item in node:
            result = get_node_value(item, key)
            if result is not None:
                return result
    return None


# 解析JSON数据
"""
if "city" in data:
    data.pop("city")
"""
json_data = json.loads(str(data).replace("'","\""))

# 获取节点的值

name = get_node_value(json_data, "name")
age = get_node_value(json_data, "age")
city = get_node_value(json_data, "city")

print(name)
print(age)
print(city)

# print(json_data)
