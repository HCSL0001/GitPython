from pathlib import Path
import json

# 读取json文件
def load_json(F):
    path = Path(F)
    # 判断json文件在不在
    # 若文件存在
    if path.exists():
        # 读取json文件
        with open(F, 'r', encoding='utf-8') as file:
            json_data = file.read()
        json_str = json.loads(str(json_data).replace("'", "\""))
        # 判断json文件长度
        length = len(json_str)
        # 文件长度为0，就是没有任何数据的空文件
        if length == 0:
            print("文件" + F + "数据长度为0，没有任何数据记录。")
        else:
            print("已读取文件：" + F)
    # 若文件不存在
    else:
        print('没有找到' + F)
        # 临时赋值，处理异常问题，让程序正常运行。
        json_str = {"错误类型":"没有找到文件。"}
    return json_str

# 打印json文件
def print_json(json_str,F,key):
    length = len(json_str)
    if length == 0:
        print("文件" + F + "数据长度为0，没有任何数据记录。")
    else:
        K = get_node_value(json_str, key)
        print(K)

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