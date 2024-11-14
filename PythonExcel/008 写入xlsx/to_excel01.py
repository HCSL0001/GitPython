import pandas as pd
data = pd.DataFrame([['可乐',15,3,45],['雪碧',6,5,30],['橙汁',10,4,40],['矿泉水',20,2,40]]) #创建一个DataFrame对象
data.to_excel('G:\\Code\\PythonExcel\\008 写入xlsx\\产品表01.xlsx',sheet_name='产品表') #将DataFrame对象中的数据写入工作簿“产品表.xlsx”的工作表“产品表”中
print(data)