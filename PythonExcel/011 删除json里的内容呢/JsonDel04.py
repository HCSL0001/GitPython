import json

data = {
    "key11":"321",
    "key2":"321"
}

# 异常处理 当key1不在JSON里面
"""
try:
    data.pop("key1")
except:
    print("没有找到“key1”")
else:
    json_str = json.dumps(data)

    with open("JsonDel04.json","w") as f:
        f.write(json_str)
"""

if "key1" in data:
    data.pop("key1")

json_str = json.dumps(data)

with open("JsonDel04.json","w") as f:
    f.write(json_str)

print(data)