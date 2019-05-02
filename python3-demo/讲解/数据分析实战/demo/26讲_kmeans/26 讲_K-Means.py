#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/30 10:41 
# @Author : 韧桂 
# @Site :  
# @File : 26 讲_K-Means.py 
# @Software: PyCharm


# 13 讲 Min-Max 规范化
# from sklearn import preprocessing
# import numpy as np
# # 初始化数据，每一行表示一个样本，每一列表示一个特征
# x = np.array([[5000.], [58000.], [16000.]])
# # 将数据进行 [0,1] 规范化
# min_max_scaler = preprocessing.MinMaxScaler()
# minmax_x = min_max_scaler.fit_transform(x)
#
# print(minmax_x)


# from sklearn.cluster import KMeans
#
# KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1, algorithm='auto')


# coding: utf-8
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd

import numpy as np
# 输入数据
data = pd.read_csv('./data.csv', encoding='gbk')
train_x = data[[u"2019年国际排名", u"2018世界杯", u"2015亚洲杯"]].astype(np.float)   #astype转换类型


df = pd.DataFrame(train_x)
kmeans = KMeans(n_clusters=3)
# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
# kmeans 算法
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类'},axis=1,inplace=True)
print(result)

# # coding: utf-8
# from sklearn.cluster import KMeans
# from sklearn import preprocessing
# import pandas as pd
# import numpy as np
# # 输入数据
# data = pd.read_csv('./data.csv', encoding = 'gbk')
# data.head()
# train_x = data[["2019年国际排名","2018世界杯","2015亚洲杯"]]
# df = pd.DataFrame(train_x)
# kmeans = KMeans(n_clusters=5)
# # 规范化
# min_max_scaler=preprocessing.StandardScaler()
# train_x=min_max_scaler.fit_transform(train_x)
# # kmeans 算法
# kmeans.fit(train_x)
# predict_y = kmeans.predict(train_x)
# # 合并聚类结果，插入到原数据中
# result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
# result.rename({0:u'聚类'},axis=1,inplace=True)
# print(result)
