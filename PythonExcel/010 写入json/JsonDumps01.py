from pathlib import Path
import json

numbers = [6,3,5,7,11,13],[6,3,5,7,11,13]#创建一个数组

path = Path('numbers.json') #指定储存文件
if path.exists():
    contents = json.dumps(numbers) #将numners数组转换成JSON的数据表现形式
    path.write_text(contents) #写入文件
else:
    print('None')