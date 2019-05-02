#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/23 16:02 
# @Author : 韧桂 
# @Site :  
# @File : 0323.py 
# @Software: PyCharm
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# # 数据准备
# N = 1000
# x = np.random.randn(N)
# y = np.random.randn(N)
# # 用 Matplotlib 画散点图
# plt.scatter(x, y,marker='x')
# plt.show()
# # 用 Seaborn 画散点图
# df = pd.DataFrame({'x': x, 'y': y})
# sns.jointplot(x="x", y="y", data=df, kind='scatter');
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# # 数据准备
# x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
# # 使用 Matplotlib 画折线图
# plt.plot(x, y)
# plt.show()
# # 使用 Seaborn 画折线图
# df = pd.DataFrame({'x': x, 'y': y})
# sns.lineplot(x="x", y="y", data=df)
# plt.show()


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# # 数据准备
# a = np.random.randn(100)
# s = pd.Series(a)
# # 用 Matplotlib 画直方图
# plt.hist(s)
# plt.show()
# # 用 Seaborn 画直方图
# sns.distplot(s, kde=False)
# plt.show()
# sns.distplot(s, kde=True)
# plt.show()



import matplotlib.pyplot as plt
import seaborn as sns
#
# # 解决seaborn数据集导入报错的问题
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# # 数据准备
# data = sns.load_dataset('car_crashes')
# print(data.head(10))
#
# # 用 seaborn 探索成对关系
# sns.pairplot(data)
#
# # 用 seaborn 画散点图
# sns.jointplot(x='total', y='speeding', data=data, kind='scatter')
#
# # 用 seaborn 画核密度图
# sns.jointplot(x='total', y='speeding', data=data, kind='kde')
#
# # 用 seaborn 画 Hexbin 图
# sns.jointplot(x='total', y='speeding', data=data, kind='hex')
#
# plt.show()


# 第一题：seaborn car_crashes成对关系探索
iris=sns.load_dataset("car_crashes")
sns.pairplot(iris)
plt.show()
# 第二题：由第一题可以看出酒精和速度由类似线性关系，因此做酒精和速度二元变量的分布图
iris=sns.load_dataset("car_crashes")
print(iris.head(10))
sns.jointplot(x='alcohol',y='speeding',data=iris,kind='scatter')
sns.jointplot(x='alcohol',y='speeding',data=iris,kind='kde')
sns.jointplot(x='alcohol',y='speeding',data=iris,kind='hex')
