import  pandas as pd
data = pd.DataFrame({'产品名称':['离合器','里程表','组合表','缓速器'],'销售数量':[25,50,100,254]},index=['A001','A002','A003','A004']) #使用字典创建数据结构并且设置行标签
print(data)