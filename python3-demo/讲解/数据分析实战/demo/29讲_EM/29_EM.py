#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/30 21:04 
# @Author : 韧桂 
# @Site :  
# @File : 29_EM.py 
# @Software: PyCharm

# from sklearn.mixture import GaussianMixture
# gmm = GaussianMixture(n_components=1, covariance_type='full', max_iter=100)


# -*- coding: utf-8 -*-
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler
import numpy as np

# 数据加载，避免中文乱码问题
data_ori = pd.read_csv('./heros.csv', encoding='gb18030')
features = [u'最大生命', u'生命成长', u'初始生命', u'最大法力', u'法力成长', u'初始法力', u'最高物攻', u'物攻成长', u'初始物攻', u'最大物防', u'物防成长', u'初始物防',
            u'最大每5秒回血', u'每5秒回血成长', u'初始每5秒回血', u'最大每5秒回蓝', u'每5秒回蓝成长', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
data = data_ori[features]

pd.set_option('mode.chained_assignment', None)  #消除 SettingWithCopyWarning 警告
data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%'))/100)

data[u'攻击范围']=data[u'攻击范围'].map({'远程':1,'近战':0})
#之所以热力图不显示最大攻速和攻击范围，是因为这两列的数据的类型是string，想要在热力图也显示这两项的话可以在构建热力图前就进行数据清洗



# 对英雄属性之间的关系进行可视化分析
# 设置 plt 正确显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 用热力图呈现 features_mean 字段之间的相关性
corr = data[features].corr()
plt.figure(figsize=(14, 14))
# annot=True 显示每个方格的数据
sns.heatmap(corr, annot=True)
plt.show()

# 相关性大的属性保留一个，因此可以对属性进行降维
features_remain = [u'最大生命', u'初始生命', u'最大法力', u'最高物攻', u'初始物攻', u'最大物防', u'初始物防', u'最大每5秒回血', u'最大每5秒回蓝',
                   u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
data = data_ori[features_remain]
data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%')) / 100)
data[u'攻击范围'] = data[u'攻击范围'].map({'远程': 1, '近战': 0})
#非数值的类型需要先转化为数值类型，比如“远程”转化为1，“近战”转化为0。这样才能做矩阵的运算。

# 采用 Z-Score 规范化数据，保证每个特征维度的数据均值为 0，方差为 1
ss = StandardScaler()
data = ss.fit_transform(data)
# 构造 GMM 聚类
gmm = GaussianMixture(n_components=30, covariance_type='full')
gmm.fit(data)
# 训练数据
prediction = gmm.predict(data)
print(prediction)
# 将分组结果输出到 CSV 文件中
data_ori.insert(0, '分组', prediction)
data_ori.to_csv('./hero_out.csv', encoding='gb18030', index=False, sep=',')  #中文的话需要需要注意这个,不然会乱码



# # -*- coding: utf-8 -*-
# import sys
# # reload(sys)
# # sys.setdefaultencoding('utf8')
#
# import pandas as pd
# import csv
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.mixture import GaussianMixture
# from sklearn.preprocessing import StandardScaler
#
# # 数据加载，避免中文乱码问题
# data_ori = pd.read_csv('./heros.csv', encoding='gb18030')
# features = [u'最大生命', u'生命成长', u'初始生命', u'最大法力', u'法力成长', u'初始法力', u'最高物攻', u'物攻成长', u'初始物攻', u'最大物防', u'物防成长', u'初始物防',
#             u'最大每5秒回血', u'每5秒回血成长', u'初始每5秒回血', u'最大每5秒回蓝', u'每5秒回蓝成长', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
# data = data_ori[features]
#
# # 对英雄属性之间的关系进行可视化分析
# # 设置 plt 正确显示中文
# plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
# # 用热力图呈现 features_mean 字段之间的相关性
# corr = data[features].corr()
# plt.figure(figsize=(14, 14))
# # annot=True 显示每个方格的数据
# sns.heatmap(corr, annot=True)
# plt.show()
#
# pd.set_option('mode.chained_assignment', None)
# data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%')) / 100)
# data[u'攻击范围'] = data[u'攻击范围'].map({u'远程': 1, u'近战': 0})
#
# # 采用 Z-Score 规范化数据，保证每个特征维度的数据均值为 0，方差为 1
# ss = StandardScaler()
# data = ss.fit_transform(data)
#
# #print(data)
#
# # 构造 GMM 聚类
# gmm = GaussianMixture(n_components=3, covariance_type='full')
# gmm.fit(data)
# # 训练数据
# prediction = gmm.predict(data)
# print(prediction)
#
# # 将分组结果输出到 CSV 文件中
# data_ori.insert(0, '分组', prediction)
# data_ori.to_csv('./hero_out2.csv', index=False, sep=',', encoding='utf-8')
#
# from sklearn.metrics import calinski_harabaz_score
# print(calinski_harabaz_score(data, prediction))