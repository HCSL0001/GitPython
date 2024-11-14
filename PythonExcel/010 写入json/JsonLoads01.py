from pathlib import Path
import json

path = Path('numbers.json') #指定文件

if path.exists():
    contents = path.read_text() #读取文件
    numbers = json.loads(contents) #将数据赋值给contents
    print(numbers)
else:
    print('None')