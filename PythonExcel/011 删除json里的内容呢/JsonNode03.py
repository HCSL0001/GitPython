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

print(data,type(data))
dic_str = json.loads(str(data).replace("'","\""))
print(dic_str)