#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/27 15:59 
# @Author : 韧桂 
# @Site :  
# @File : 19.py 
# @Software: PyCharm
import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn import tree
import graphviz

import os
os.environ["PATH"] += os.pathsep + 'D:/Program Files (x86)/Graphviz2.38/bin/'
# 数据加载
train_data = pd.read_csv('./Titanic_Data/train.csv')
test_data = pd.read_csv('./Titanic_Data/test.csv')
# 数据探索
# print(train_data.info())   # info 行数、列数、每列的数据类型、数据完整度
# print('-'*30)  # 打印 30 个 - 。
# print(train_data.describe())   #总数、平均值、标准差、最小值、最大值等；
# print('-'*30)
# print(train_data.describe(include=['O']))  #查看字符串类型（非数字）的整体情况；
# print('-'*30)
# print(train_data.head())  #使用 head 查看前几行数据（默认是前 5 行）；
# print('-'*30)
# print(train_data.tail())  #使用 tail 查看后几行数据（默认是最后 5 行）。


# 使用平均年龄来填充年龄中的 nan 值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
# 使用票价的均值填充票价中的 nan 值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)

print(train_data['Embarked'].value_counts())  #观察下 Embarked 字段的取值
# 使用登录最多的港口来填充登录港口的 nan 值
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S', inplace=True)

# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]

#Embarked 有 S、C、Q 三种可能，我们也可以改成 Embarked=S、Embarked=C  和 Embarked=Q 三个字段，数值用 0 或 1 来表示。
dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))

#fit_transform 这个函数，它可以将特征向量转化为特征值矩阵。然后我们看下 dvec 在转化后的特征属性是怎样的，即查看 dvec 的 feature_names_ 属性值，方法如下：
print(dvec.feature_names_)

# 决策树模型
# 构造 ID3 决策树
clf = DecisionTreeClassifier(criterion='entropy')
# 决策树训练
clf.fit(train_features, train_labels)

# 模型预测 & 评估
test_features=dvec.transform(test_features.to_dict(orient='record'))
# 决策树预测
pred_labels = clf.predict(test_features)

# 决策树准确率
acc_decision_tree = round(clf.score(train_features, train_labels), 6)
print(u'score 准确率为 %.4lf' % acc_decision_tree)

# K 折交叉验证统计决策树准确率
print(u'cross_val_score 准确率为 %.4lf' % np.mean(cross_val_score(clf, train_features, train_labels, cv=10)))

# 决策树可视化
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.view()