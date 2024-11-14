import  pandas as pd
data = pd.DataFrame([['离合器',25],['里程表',50],['组合表',100],['缓速器',254]],columns=['产品名称','销售数量'],index=['A001','A002','A003','A004']) #创建二维数据结构并且自定义元素的列标签和行标签
print(data)