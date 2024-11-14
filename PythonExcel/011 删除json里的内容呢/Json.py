import  json

json_str = '[' \
           '{"name":"Alice","age":25},' \
           '{"name":"Bob","age":30}' \
           ']'

data = json.loads(json_str)

new_array = []

for item in data:
    name = item["name"]
    age = item["age"]
    new_array.append({"name":name,"age":age})

print(new_array)