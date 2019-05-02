#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/31 15:59 
# @Author : 韧桂 
# @Site :  
# @File : 31讲.py 
# @Software: PyCharm


from efficient_apriori import apriori
# 设置数据集
data = [('牛奶','面包','尿布'),
           ('可乐','面包', '尿布', '啤酒'),
           ('牛奶','尿布', '啤酒', '鸡蛋'),
           ('面包', '牛奶', '尿布', '啤酒'),
           ('面包', '牛奶', '尿布', '可乐')]
# 从上边代码中看出来，data 是个 List 数组类型，其中每个值都可以是一个集合。也可以把 data 数组中的每个值设置为 List 数组类型，比如：
# data = [['牛奶','面包','尿布'],
#            ['可乐','面包', '尿布', '啤酒'],
#            ['牛奶','尿布', '啤酒', '鸡蛋'],
#            ['面包', '牛奶', '尿布', '啤酒'],
#            ['面包', '牛奶', '尿布', '可乐']]

# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(data, min_support=0.5,  min_confidence=1)
# 最核心的代码。其中 data 是我们要提供的数据集，它是一个 list 数组类型。min_support 参数为最小支持度，
# 在 efficient-apriori 工具包中用 0 到 1 的数值代表百分比，比如 0.5 代表最小支持度为 50%。
# min_confidence 是最小置信度，数值也代表百分比，比如 1 代表 100%。
print(itemsets)
print(rules)















