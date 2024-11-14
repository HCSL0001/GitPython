import json


def count_json_nodes(json_data):
    def count_nodes_helper(data):
        if isinstance(data, dict):
            count = 1  # 加上当前节点
            for value in data.values():
                count += count_nodes_helper(value)  # 递归计算每个值的节点数
            return count
        elif isinstance(data, list):
            count = 0
            for item in data:
                count += count_nodes_helper(item)  # 递归计算列表中每个项的节点数
            return count
        else:
            return 1  # 基本类型如字符串、数字、布尔值等，节点数为1

    return count_nodes_helper(json_data)


# 示例JSON数据
json_data = """
{
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
"""

# 计算节点数
node_count = count_json_nodes(json.loads(json_data))
print(f"节点数量: {node_count}")
# dic_str = json.loads(str(json_data).replace("'","\""))
dic_str = json.loads(json_data)
print(dic_str["friends"])