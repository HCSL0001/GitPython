from pathlib import Path
import json

F = "test.json"

path = Path(F) #指定文件

if path.exists():
    try:
        contents = path.read_text() #读取文件
        numbers = json.loads(contents) #将数据赋值给contents
        print(numbers)
    except:
        print('没有记录')
else:
    print('None')