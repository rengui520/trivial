#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/16 12:56 
# @Author : 韧桂 
# @Site :  
# @File : 36.py 
# @Software: PyCharm
# from sklearn.datasets import load_boston
#
# boston=load_boston()
# print(boston.keys())

import pandas as pd
# 数据加载
train_data = pd.read_csv('./Titanic_Data/train.csv')
test_data = pd.read_csv('./Titanic_Data/test.csv')
print(train_data.info())
print(test_data.info())
