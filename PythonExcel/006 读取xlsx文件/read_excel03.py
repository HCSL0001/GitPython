import pandas as pd
data = pd.read_excel('G:\\Code\\PythonExcel\\006 读取xlsx文件\\统计表.xlsx',sheet_name=0,names=['产品名称','销售数量','产品单价','销售金额']) #读取工作薄中第1个工作表的数据并重新设置列标签
print(data)