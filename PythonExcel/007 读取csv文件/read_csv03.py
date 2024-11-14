import pandas as pd
data = pd.read_csv('/Python/PythonExcel/007 读取csv文件/员工档案表1.csv', usecols=[0, 3], sep='-', encoding='gbk') #读取CSV文件的第1列和第4列数据,指定分隔符为“-”、编码方式为GBK
print(data)

data1 = pd.read_csv('/Python/PythonExcel/007 读取csv文件/员工档案表1.csv', usecols=['员工编号', '部门', '入职时间'], sep='-', encoding='gbk') #读取CSV文件的第1列和第4列数据,指定分隔符为“-”、编码方式为GBK
print(data1)