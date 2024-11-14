import pandas as pd
data = pd.read_excel('G:\\Code\\PythonExcel\\006 读取xlsx文件\\统计表.xlsx',sheet_name=0,usecols=[0,2]) #从工作薄的第1个工作表中第1列和第3列数据
print(data)