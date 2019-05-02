#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/13 17:23 
# @Author : 韧桂 
# @Site :  
# @File : pandas-demo.py 
# @Software: PyCharm
import numpy as np
import pandas as pd

# 一、创建 Pandas Series ,三种方法
s1 = pd.Series([1, 2, 3, 4])
# print(s1)
# print(s1.values)   #查看数据
# print(s1.index)   #查看数据
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
# print(s3.values)
# print(s3.index)
# 1    1
# 2    2
# 3    3
# dtype: int64
# [1 2 3]
# Index(['1', '2', '3'], dtype='object')
#
# #Index相当于字典的key，随意指定

s4 = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
# print(s4)
# print(s4['A'])  #访问index是A 的元素
# print(s4[s4>2])  #访问index 大于2 的元素
#
# print(s4.to_dict())#转换成python的字典
# A    1
# B    2
# C    3
# D    4
# dtype: int64
# 1
# C    3
# D    4
# dtype: int64
# {'A': 1, 'B': 2, 'C': 3, 'D': 4}

s5 = pd.Series(s4.to_dict())
# print(s5)
# A    1
# B    2
# C    3
# D    4
# dtype: int64

index_1 = ['A', 'B', 'C', 'D', 'E']
s6 = pd.Series(s5, index=index_1)
# print(s6)
# print(pd.isnull(s6))
# print(pd.notnull(s6))
# A    1.0
# B    2.0
# C    3.0
# D    4.0
# E    NaN
# dtype: float64

# A    False
# B    False
# C    False
# D    False
# E     True
# dtype: bool

# A     True
# B     True
# C     True
# D     True
# E    False
# dtype: bool

# s6.name = 'demo'
# s6.index.name = 'demo index'
# print(s6)
# print(s6.index)
# print(s6.values)

# demo index
# A    1.0
# B    2.0
# C    3.0
# D    4.0
# E    NaN
# Name: demo, dtype: float64
# Index(['A', 'B', 'C', 'D', 'E'], dtype='object', name='demo index')
# [ 1.  2.  3.  4. nan]


#二、Dataframe

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import webbrowser
link = 'https://www.tiobe.com/tiobe-index/'
# webbrowser.open(link)

df = pd.read_clipboard()  #从剪贴板解析内容，把它转换成一个pandas的dataframe
print(df)
print(type(df))
# print(df.columns)
# print(df.Ratings)

#    Mar 2019  Mar 2018  Change Programming Language  Ratings Change.1
# 0         1         1     NaN                 Java  14.880%   -0.06%
# 1         2         2     NaN                    C  13.305%   +0.55%
# 2         3         4  change               Python   8.262%   +2.39%
# 3         4         3  change                  C++   8.126%   +1.67%
# 4         5         6  change    Visual Basic .NET   6.429%   +2.34%
# 5         6         5  change                   C#   3.267%   -1.80%
# 6         7         8  change           JavaScript   2.426%   -1.49%
# 7         8         7  change                  PHP   2.420%   -1.59%
# 8         9        10  change                  SQL   1.926%   -0.76%
# 9        10        14  change          Objective-C   1.681%   -0.09%
# <class 'pandas.core.frame.DataFrame'>

# Index(['Mar 2019', 'Mar 2018', 'Change', 'Programming Language', 'Ratings',
#        'Change.1'],
#       dtype='object')

# 0    14.880%
# 1    13.305%
# 2     8.262%
# 3     8.126%
# 4     6.429%
# 5     3.267%
# 6     2.426%
# 7     2.420%
# 8     1.926%
# 9     1.681%
# Name: Ratings, dtype: object


df_new = DataFrame(df, columns=['Programming Language', 'Mar 2018'])  #形成新的DataFrame
# print(df_new)
#   Programming Language  Mar 2018
# 0                 Java         1
# 1                    C         2
# 2               Python         4
# 3                  C++         3
# 4    Visual Basic .NET         6
# 5                   C#         5
# 6           JavaScript         8
# 7                  PHP         7
# 8                  SQL        10
# 9          Objective-C        14

# print(df['Mar 2018'])
# 0     1
# 1     2
# 2     4
# 3     3
# 4     6
# 5     5
# 6     8
# 7     7
# 8    10
# 9    14
# Name: Mar 2018, dtype: int64

# print(type(df['Mar 2018']))
# <class 'pandas.core.series.Series'>

df_new = DataFrame(df, columns=['Programming Language', 'Mar 2018', 'Mar 2020'])
# print(df_new)
# df_new['Mar 2020'] = range(0, 10)  #1
# print(df_new)
# df_new['Mar 2020'] = np.arange(0, 10)   #2
# print(df_new)
# df_new['Mar 2020'] = pd.Series(np.arange(0, 10))   #3
# print(df_new)
#
#   Programming Language  Mar 2018  Mar 2020
# 0                 Java         1       NaN
# 1                    C         2       NaN
# 2               Python         4       NaN
# 3                  C++         3       NaN
# 4    Visual Basic .NET         6       NaN
# 5                   C#         5       NaN
# 6           JavaScript         8       NaN
# 7                  PHP         7       NaN
# 8                  SQL        10       NaN
# 9          Objective-C        14       NaN
#   Programming Language  Mar 2018  Mar 2020
# 0                 Java         1         0
# 1                    C         2         1
# 2               Python         4         2
# 3                  C++         3         3
# 4    Visual Basic .NET         6         4
# 5                   C#         5         5
# 6           JavaScript         8         6
# 7                  PHP         7         7
# 8                  SQL        10         8
# 9          Objective-C        14         9

df_new['Mar 2020'] = pd.Series([100, 200], index=[1,2])  #指定残数的数值
# print(df_new)
#   Programming Language  Mar 2018  Mar 2020
# 0                 Java         1       NaN
# 1                    C         2     100.0
# 2               Python         4     200.0
# 3                  C++         3       NaN
# 4    Visual Basic .NET         6       NaN
# 5                   C#         5       NaN
# 6           JavaScript         8       NaN
# 7                  PHP         7       NaN
# 8                  SQL        10       NaN
# 9          Objective-C        14       NaN

