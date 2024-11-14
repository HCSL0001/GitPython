import  json

with open('numbers.json', 'r', encoding='utf-8') as file:
    json_str = file.read()

data = json.loads(json_str)

print(data)
print((data[0]))
print(json_str[1])