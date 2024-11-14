import json

numbers = [6,3,5,7,11,13,'销售']

with open('numbers.json', 'w', encoding='utf-8') as file:
    json.dump(numbers, file, ensure_ascii=False, sort_keys=True)
    #json.dump(numbers, file, ensure_ascii=False, sort_keys=True, indent=4)
    #ensure_ascii=False确保非ASCII字符不会被转义成ASCII，sort_keys=True会对字典的键进行排序，indent=4使得输出的JSON易于阅读，有缩进。