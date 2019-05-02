#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/29 21:52 
# @Author : 韧桂 
# @Site :  
# @File : 25讲_KNN.py 
# @Software: PyCharm
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_digits
# from sklearn.model_selection import train_test_split
# from sklearn import preprocessing
#
# # 加载数据
# digits = load_digits()
# data = digits.data
# # 数据探索
# print(data.shape)
# # 查看第一幅图像
# print(digits.images[0])
# # 第一幅图像代表的数字含义
# print(digits.target[0])
# # 将第一幅图像显示出来
# plt.gray()
# plt.imshow(digits.images[0])
# plt.show()
#
#
# # 分割数据，将 25% 的数据作为测试集，其余作为训练集（你也可以指定其他比例的数据作为训练集）
# train_x, test_x, train_y, test_y = train_test_split(data, digits.target, test_size=0.25, random_state=33)
# # 采用 Z-Score 规范化
# ss = preprocessing.StandardScaler()
# train_ss_x = ss.fit_transform(train_x)
# test_ss_x = ss.transform(test_x)



# -*- coding: utf-8 -*-
# 手写数字分类
from sklearn.model_selection import train_test_split  #做数据集的拆分
from sklearn import preprocessing #使用 preprocessing 中的 StandardScaler 和MinMaxScaler 做数据的规范化
from sklearn.metrics import accuracy_score  #进行分类器准确率的计算
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt  #工具包显示图像

# 加载数据
digits = load_digits()
data = digits.data
# 数据探索
print(data.shape)
# 查看第一幅图像
print(digits.images[0])
# 第一幅图像代表的数字含义
print(digits.target[0])
# 将第一幅图像显示出来
plt.gray()
plt.imshow(digits.images[0])
plt.show()

# 分割数据，将25%的数据作为测试集，其余作为训练集
# test_x和test_y 对应是测试集的特征矩阵和分类结果。
train_x, test_x, train_y, test_y = train_test_split(data, digits.target, test_size=0.25, random_state=33)

# 采用Z-Score规范化   划分成训练集和测试集
ss = preprocessing.StandardScaler()
#我在train的时候用到了：train_ss_x = ss.fit_transform(train_x)
# 实际上：fit_transform是fit和transform两个函数都执行一次。所以ss是进行了fit拟合的。
# 只有在fit拟合之后，才能进行transform。
# 在进行test的时候，我们已经在train的时候fit过了，所以直接transform即可。
# 另外，如果我们没有fit，直接进行transform会报错，因为需要先fit拟合，才可以进行transform。
train_ss_x = ss.fit_transform(train_x)
test_ss_x = ss.transform(test_x)

# 创建KNN分类器
knn = KNeighborsClassifier()
#创建完 KNN 分类器之后，我们就可以输入训练集对它进行训练，这里我们使用 fit() 函数，
# 传入训练集中的样本特征矩阵和分类标识，会自动得到训练好的 KNN 分类器。
knn.fit(train_ss_x, train_y)
predict_y = knn.predict(test_ss_x)  #predict()。用训练好的分类器进行预测
print("KNN准确率: %.4lf" % accuracy_score(predict_y, test_y))

# 创建SVM分类器   把训练集的数据传入构造好的 knn，并通过测试集进行结果预测，与测试集的结果进行对比，得到 KNN 分类器准确率，
svm = SVC()
svm.fit(train_ss_x, train_y)
predict_y=svm.predict(test_ss_x)
print('SVM准确率: %0.4lf' % accuracy_score(predict_y, test_y))

# 采用Min-Max规范化
mm = preprocessing.MinMaxScaler()
train_mm_x = mm.fit_transform(train_x)
test_mm_x = mm.transform(test_x)

# 创建Naive Bayes分类器
mnb = MultinomialNB()
mnb.fit(train_mm_x, train_y)
predict_y = mnb.predict(test_mm_x)
print("多项式朴素贝叶斯准确率: %.4lf" % accuracy_score(predict_y, test_y))

# 创建CART决策树分类器
dtc = DecisionTreeClassifier()
dtc.fit(train_mm_x, train_y)
predict_y = dtc.predict(test_mm_x)
print("CART决策树准确率: %.4lf" % accuracy_score(predict_y, test_y))