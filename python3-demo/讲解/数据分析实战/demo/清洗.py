#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/16 18:07 
# @Author : 韧桂 
# @Site :  
# @File : 清洗.py 
# @Software: PyCharm

# 1.
# import pandas as pd
# df = pd.read_csv("D://Data_for_sci/food.csv")
# df.index
#
# df
#
# # Data cleaning for lowercase
# df['food'] = df['food'].str.lower()
# df
#
# # Delet NaN
# df = df.dropna()
# df.index = range(len(df)) # reset index
# df
#
# # Get bacon's mean value and delet second one
# df.loc[0,'ounces'] = df[df['food'].isin(['bacon'])].mean()['ounces']
# df.drop(df.index[4],inplace=True)
# df.index = range(len(df)) # reset index
# df
#
# #Get pastrami's mean value and delet second one
# df.loc[2,'ounces'] = df[df['food'].isin(['pastrami'])].mean()['ounces']
# df.drop(df.index[4],inplace=True)
# df.index = range(len(df)) # reset index
# df


# 2.
import pandas as pd
"""利用Pandas清洗美食数据"""

# 读取csv文件
df = pd.read_csv("c.csv")

df['food'] = df['food'].str.lower() # 统一为小写字母
df.dropna(inplace=True) # 删除数据缺失的记录
df['ounces'] = df['ounces'].apply(lambda a: abs(a)) # 负值不合法，取绝对值

# 查找food重复的记录，分组求其平均值
d_rows = df[df['food'].duplicated(keep=False)]
g_items = d_rows.groupby('food').mean()
g_items['food'] = g_items.index
print(g_items)

# 遍历将重复food的平均值赋值给df
for i, row in g_items.iterrows():
    df.loc[df.food == row.food, 'ounces'] = row.ounces
df.drop_duplicates(inplace=True) # 删除重复记录

df.index = range(len(df)) # 重设索引值
print(df)

# 3.
# 完整性：ounces 列数据中存在NAN
# 全面性：food列数据中存在大小写不一致问题
# 合法性：ounces列数据存在负值
# 唯一性：food列数据存在重复
# # -*- coding: utf-8 -*
# import pandas as pd
# import numpy as np
# from pandas import Series, DataFrame
# df = pd.read_csv('./fooddata.csv')
# # 把ounces 列中的NaN替换为平均值
# df['ounces'].fillna(df['ounces'].mean(), inplace=True)
# # 把food列中的大写字母全部转换为小写
# df['food'] = df['food'].str.lower()
# # 把ounces 列中的负数转化为正数
# df['ounces']= df['ounces'].apply(lambda x: abs(x))
# #删除food列中的重复值
# df.drop_duplicates('food',inplace=True)
# print (df)

