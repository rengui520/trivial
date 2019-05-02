#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/14 20:40 
# @Author : 韧桂 
# @Site :  
# @File : 豆瓣电影下载-数据分析.py 
# @Software: PyCharm
# coding:utf-8
import requests
import json
import re
import os

query = '王祖贤'
path = os.getcwd() # 当前路径，可以替换成别的路径
picpath = path + '/' + query # 设置的图片目录
print(picpath) # 输出设置的图片目录
if not os.path.isdir(picpath): # 如果图片目录未创建则创建一个
    os.mkdir(picpath)


def download(src, id):
    dir = picpath + '/' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
    except requests.exceptions.ConnectionError:
        # print 'error, %d 当前图片无法下载', %id
        print('图片无法下载')
    fp = open(dir, 'wb')
    fp.write(pic.content)
    fp.close()


''' for 循环 请求全部的 url '''
for i in range(0, 22471, 20): #
    url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
    html = requests.get(url).text # 得到返回结果
    response = json.loads(html, encoding='utf-8') # 将 JSON 格式转换成 Python 对象
    print('已下载 ' + str(i) + ' 张图片')
    for image in response['images']:
        image['src'] = image['src'].replace('thumb', 'l')
        # image['src'] = re.sub(r'thumb', r'l', image['src'])
        print(image['src']) # 查看当前下载的图片网址
        download(image['src'], image['id']) # 下载一张图片