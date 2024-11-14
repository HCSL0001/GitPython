import pandas as pd
data = pd.read_excel('G:\\Code\\PythonExcel\\006 读取xlsx文件\\统计表.xlsx',sheet_name=0,usecols=[2]) #读取工作薄中第1个工作表的第3列数据
print(data)