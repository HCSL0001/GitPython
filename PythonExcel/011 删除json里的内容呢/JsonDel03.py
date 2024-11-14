import json

data = {
    "key1":"value1",
    "key2":"value2"
}

del data["key1"]

json_str = json.dumps(data)

with open("JsonDel03.json","w") as f:
    f.write(json_str)

print(data)