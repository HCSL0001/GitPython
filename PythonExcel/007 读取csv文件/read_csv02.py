import pandas as pd
data = pd.read_csv('/Python/PythonExcel/007 读取csv文件/员工档案表1.csv', sep='-', encoding='gbk') #读取CSV文件数据,指定分隔符为“-”、编码方式为GBK
print(data)