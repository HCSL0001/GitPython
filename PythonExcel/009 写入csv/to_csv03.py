import pandas as pd

data = pd.DataFrame([['可乐',15,3,45],['雪碧',6,5,30],['橙汁',10,4,40],['矿泉水',20,2,40]])
data.to_csv('G:\\Code\\PythonExcel\\009 写入csv\\data03.csv',header=['产品名称','销售数量','销售单价','销售额'],sep='*',encoding='gbk',index=False) #将DataFrame对象中的数据写入CSV文件”产品表.csv“。

Rdata = pd.read_csv('/Python/PythonExcel/009 写入csv/data03.csv', nrows=4, sep='-', encoding='gbk') #读取CSV文件的前4行数据,指定分隔符为“-”、编码方式为GBK
print(Rdata)