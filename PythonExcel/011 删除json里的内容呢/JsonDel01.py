import json

def open_json_file(file_path):
    """
    打开JSON文件并解析其中的数据

    参数：
    -file_path:JSON 文件路径

    返回:
    -json_data: 解析后的JSON数据
    """

    with open(file_path,'r') as file:
        json_data = json.load(file)
    return json_data

def find_content_to_delete(json_data,content):
    """
    找到需要删除的内容

    参数:
    -json_data:JSON 数据
    -content: 需要删除的内容

    返回:
    - index: 需要删除的内容在JSON数据中的索引，若不存在则返回-1
    """

    for index,item in enumerate(json_data):
        if item == content:
            return  index
    return -1

def delete_content(json_data,index):
    """
    从JSON数据中删除指定索引的内容

    参数:
    -json_data:JSON 数据
    -index: 需要删除的内容的索引

    返回:
    - updated_json_data: 更新后的JSON数据
    """

    updated_json_data = json_data[:]
    del updated_json_data[index]
    return updated_json_data

def write_to_json_file(file_path,updated_json_data):
    """
    从JSON数据中删除指定索引的内容

    参数:
    -json_data:JSON 数据
    -index: 需要删除的内容的索引

    返回:
    - updated_json_data: 更新后的JSON数据
    """

    with open(file_path,'w') as file:
        json.dump(updated_json_data,file)
