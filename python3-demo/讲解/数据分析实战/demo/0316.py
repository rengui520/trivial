#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/16 16:39 
# @Author : 韧桂 
# @Site :  
# @File : 0316.py 
# @Software: PyCharm

#3-1 Pandas Series
#Series 序列，DataFrame 数据框
import numpy as np
import pandas as pd

#创建 pandas Series，三种方法
s1 = pd.Series([1, 2, 3, 4])
# print(s1)
# print(s1.values)  #查看数据     #数值
# print(s1.index)  #从零开始，到4，间隔是1   #标识号
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
# [1 2 3 4]
# RangeIndex(start=0, stop=4, step=1)

s2 = pd.Series(np.arange(10))
# print(s2)
# 0    0
# 1    1
# 2    2
# 3    3
# 4    4
# 5    5
# 6    6
# 7    7
# 8    8
# 9    9
# dtype: int32

s3 = pd.Series({'1':1, '2':2, '3':3})
# print(s3)
# 1    1
# 2    2
# 3    3
# dtype: int64

s4 = pd.Series([1, 2, 3,4], index=['A', 'B', 'C', 'D'])
# print(s4)
# A    1
# B    2
# C    3
# D    4
# dtype: int64

# print(s4['A'])
# print(s4[s4>2])
# 1
# C    3
# D    4
# dtype: int64
# print(s4.to_dict())  #Series转换为字典
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}


