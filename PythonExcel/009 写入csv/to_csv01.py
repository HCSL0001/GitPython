import pandas as pd

# 创建一个DataFrame对象
data = {'名称': ['Tom', 'Jerry', 'Spike', 'Tyke'],
        '年龄': [18, 19, 20, 21],
        '性别': ['Male', 'Male', 'Male', 'Male']}
df = pd.DataFrame(data)

# 将DataFrame对象的数据保存到csv文件
df.to_csv('data01.csv', encoding='gbk',index=False)

data = pd.read_csv('/Python/PythonExcel/009 写入csv/data01.csv', nrows=4, sep=',', encoding='gbk') #读取CSV文件的前4行数据,指定分隔符为“-”、编码方式为GBK
print(data)