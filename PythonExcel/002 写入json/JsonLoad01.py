import  json

with open('numbers.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(data)