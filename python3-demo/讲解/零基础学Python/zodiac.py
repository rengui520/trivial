# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # @Time : 2019/3/26 20:35
# # @Author : 韧桂
# # @Site :
# # @File : zodiac.py
# # @Software: PyCharm
#
# #元组
zodiac_name = (u'魔蝎座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
               u'巨蟹座', u'水瓶座', u'处女座', u'天枰座', u'天蝎座', u'射手座')
# zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
#                (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12,23))
#
# # 用户输入月份和日期
# int_month = int(input('请输入月份：'))
# int_day = int(input('请输入日期：'))
#
# # for zd_num in range(len(zodiac_days)):
# #     if zodiac_days[zd_num] >= (int_month, int_day):
# #         print(zodiac_name[zd_num])
# #         break
# #     elif int_month == 12 and int_day > 23:
# #         print(zodiac_name[0])
# #         break
#
# n = 0
# while zodiac_days[n] < (int_month, int_day):
#     if int_month == 12 and int_day > 23:
#         break
#     n += 1
# print(zodiac_name[n])
#
#
# # (month, day) = (2, 15)
# #
# # zodiac_day = filter(lambda x: x<=(month, day), zodiac_days)
# # print(zodiac_day)
# # zodiac_len = len(list(zodiac_day)) % 12   #list得出数字，len得出个数
# # print(zodiac_name[zodiac_len])
#
#
# #列表，可增加删减数据
#

# 列表推导式和字典推导式
# alist = []
# for i in range(1, 11):
#     if (i % 2 ==0):
#         alist.append(i*i)
# print(alist)
#
# blist = [i*i for i in range(1, 11) if(i % 2) == 0]
# print(blist)

# z_num = {}
# for i in zodiac_name:
#     z_num[i] = 0
# print(z_num)
# z_num = {i:0 for i in zodiac_name}
# print(z_num)

# 文件内建函数和方法
# open 打开文件
# read 输入
# readline 输入一行
# seek 文件内移动
# write 输出
# close 关闭文件