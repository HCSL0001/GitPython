import pandas as pd
data = pd.read_excel('G:\\Code\\PythonExcel\\006 读取xlsx文件\\统计表.xlsx',sheet_name=0,index_col=0) #读取工作薄中第1个工作表的数据并将第1列的内容设置为行标签
print(data)