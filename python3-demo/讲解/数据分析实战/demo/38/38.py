#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/17 15:03 
# @Author : 韧桂 
# @Site :  
# @File : 38.py 
# @Software: PyCharm
#coding:utf-8

# import time
# from selenium import webdriver
# from lxml import etree
#
# #这里一定要设置编码格式，防止后面写入文件时报错
# import sys
# import importlib
# importlib.reload(sys)
#
# friend = '2477533480' # 朋友的QQ号，朋友的空间要求允许你能访问
# user = '2991769199'  # 你的QQ号
# pw = '2477533480'  # 你的QQ密码
#
# #获取浏览器驱动
# driver = webdriver.Chrome()
#
# # 浏览器窗口最大化
# driver.maximize_window()
#
# # 浏览器地址定向为qq登陆页面
# driver.get("http://i.qq.com")
#
# # 所以这里需要选中一下frame，否则找不到下面需要的网页元素
# driver.switch_to.frame("login_frame")
#
# # 自动点击账号登陆方式
# driver.find_element_by_id("switcher_plogin").click()
#
# # 账号输入框输入已知qq账号
# driver.find_element_by_id("u").send_keys(user)
#
# # 密码框输入已知密码
# driver.find_element_by_id("p").send_keys(pw)
#
# # 自动点击登陆按钮
# driver.find_element_by_id("login_button").click()
#
# # 让webdriver操纵当前页
# driver.switch_to.default_content()
#
# # 跳到说说的url, friend你可以任意改成你想访问的空间
# driver.get("http://user.qzone.qq.com/" + friend + "/311")
#
# next_num = 0  # 初始“下一页”的id
# while True:
#
#         # 下拉滚动条，使浏览器加载出动态加载的内容，
#         # 我这里是从1开始到6结束 分5 次加载完每页数据
#         for i in range(1,6):
#             height = 20000*i#每次滑动20000像素
#             strWord = "window.scrollBy(0,"+str(height)+")"
#             driver.execute_script(strWord)
#             time.sleep(4)
#
#         # 很多时候网页由多个<frame>或<iframe>组成，webdriver默认定位的是最外层的frame，
#         # 所以这里需要选中一下说说所在的frame，否则找不到下面需要的网页元素
#         driver.switch_to.frame("app_canvas_frame")
#         selector = etree.HTML(driver.page_source)
#         divs = selector.xpath('//*[@id="msgList"]/li/div[3]')
#
#         #这里使用 a 表示内容可以连续不清空写入
#         with open('qq_word.txt','a') as f:
#             for div in divs:
#                 qq_name = div.xpath('./div[2]/a/text()')
#                 qq_content = div.xpath('./div[2]/pre/text()')
#                 qq_time = div.xpath('./div[4]/div[1]/span/a/text()')
#                 qq_name = qq_name[0] if len(qq_name)>0 else ''
#                 qq_content = qq_content[0] if len(qq_content)>0 else ''
#                 qq_time = qq_time[0] if len(qq_time)>0 else ''
#                 print (qq_name,qq_time,qq_content)
#                 f.write(qq_content+"\n")
#
#         # 当已经到了尾页，“下一页”这个按钮就没有id了，可以结束了
#         if driver.page_source.find('pager_next_' + str(next_num)) == -1:
#          break
#
#         # 找到“下一页”的按钮，因为下一页的按钮是动态变化的，这里需要动态记录一下
#         driver.find_element_by_id('pager_next_' + str(next_num)).click()
#
#         # “下一页”的id
#         next_num += 1
#
#         # 因为在下一个循环里首先还要把页面下拉，所以要跳到外层的frame上
#         driver.switch_to.parent_frame()





# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import jieba
#
# #生成词云
# def create_word_cloud(filename):
#     text= open("{}.txt".format(filename)).read()
#     # 结巴分词
#     wordlist = jieba.cut(text, cut_all=True)
#     wl = " ".join(wordlist)
#
#     # 设置词云
#     wc = WordCloud(
#         background_color='white',   # 设置背景颜色
#         # mask=backgroud_Image,   # 设置背景图片
#
#
#         font_path='./SimHei.ttf',  # 设置字体，针对中文的情况需要设置中文字体，否则显示乱码
#         max_words=100, # 设置最大的字数.最大显示的词云数
#         # stopwords=STOPWORDS,# 设置停用词
#         max_font_size=150,  # 设置字体最大值
#         width=2000,     # 设置画布的宽度
#         height=1200,    # 设置画布的高度
#         random_state=30, # 设置多少种随机状态，即多少种颜色
#     )
#
#     myword = wc.generate(wl)  # 生成词云
#     # 展示词云图
#     plt.imshow(myword)
#     plt.axis("off")     #使用 plt.axis(“off”) 可以将坐标轴关闭。
#     plt.show()
#     wc.to_file('py_book.png')  # 把词云保存下
#
#
# if __name__ == '__main__':
#     create_word_cloud('word_py')


# #-*- coding:utf-8 -*-
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import jieba
# from PIL import Image
# import numpy as np
# # 生成词云
# def create_word_cloud(f):
#      print('根据词频计算词云')
#      text = " ".join(jieba.cut(f,cut_all=False, HMM=True))
#      wc = WordCloud(
#            font_path="./SimHei.ttf",
#            max_words=100,
#            width=2000,
#            height=1200,
#     )
#      wordcloud = wc.generate(text)
#      # 写词云图片
#      wordcloud.to_file("wordcloud.jpg")
#      # 显示词云文件
#      plt.imshow(wordcloud)
#      plt.axis("off")
#      plt.show()
#
# f = '数据分析全景图及修炼指南\
# 学习数据挖掘的最佳学习路径是什么？\
# Python 基础语法：开始你的 Python 之旅\
# Python 科学计算：NumPy\
# Python 科学计算：Pandas\
# 学习数据分析要掌握哪些基本概念？\
# 用户画像：标签化就是数据的抽象能力\
# 数据采集：如何自动化采集数据？\
# 数据采集：如何用八爪鱼采集微博上的“D&G”评论？\
# Python 爬虫：如何自动化下载王祖贤海报？\
# 数据清洗：数据科学家 80% 时间都花费在了这里？\
# 数据集成：这些大号一共 20 亿粉丝？\
# 数据变换：大学成绩要求正态分布合理么？\
# 数据可视化：掌握数据领域的万金油技能\
# 一次学会 Python 数据可视化的 10 种技能'


# -*- coding:utf-8 -*-
# 网易云音乐 通过歌手 ID，生成该歌手的词云
import requests
import sys
import re
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from PIL import Image
import numpy as np
from lxml import etree

headers = {
    'Referer': 'http://music.163.com',
    'Host': 'music.163.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Chrome/10'
}


# 得到某一首歌的歌词
def get_song_lyric(headers, lyric_url):
    res = requests.request('GET', lyric_url, headers=headers)
    if 'lrc' in res.json():
        lyric = res.json()['lrc']['lyric']
        new_lyric = re.sub(r'[\d:.[\]]', '', lyric)
        return new_lyric
    else:
        return ''
        print(res.json())


# 去掉停用词
def remove_stop_words(f):
    stop_words = ['作词', '作曲', '编曲', 'Arranger', '录音', '混音', '人声', 'Vocal', '弦乐', 'Keyboard', '键盘', '编辑', '助理',
                  'Assistants', 'Mixing', 'Editing', 'Recording', '音乐', '制作', 'Producer', '发行', 'produced', 'and',
                  'distributed']
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


# 生成词云
def create_word_cloud(f):
    print('根据词频，开始生成词云!')
    f = remove_stop_words(f)
    cut_text = " ".join(jieba.cut(f, cut_all=False, HMM=True))
    wc = WordCloud(
        font_path="./wc.ttf",
        max_words=100,
        width=2000,
        height=1200,
    )
    print(cut_text)
    wordcloud = wc.generate(cut_text)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


# 得到指定歌手页面 热门前 50 的歌曲 ID，歌曲名
def get_songs(artist_id):
    page_url = 'https://music.163.com/artist?id=' + artist_id
    # 获取网页 HTML
    res = requests.request('GET', page_url, headers=headers)
    # 用 XPath 解析 前 50 首热门歌曲
    html = etree.HTML(res.text)
    href_xpath = "//*[@id='hotsong-list']//a/@href"
    name_xpath = "//*[@id='hotsong-list']//a/text()"
    hrefs = html.xpath(href_xpath)
    names = html.xpath(name_xpath)
    # 设置热门歌曲的 ID，歌曲名称
    song_ids = []
    song_names = []
    for href, name in zip(hrefs, names):
        song_ids.append(href[9:])
        song_names.append(name)
        print(href, '  ', name)
    return song_ids, song_names


# 设置歌手 ID，毛不易为 12138269
artist_id = '12138269'
[song_ids, song_names] = get_songs(artist_id)
# 所有歌词
all_word = ''
# 获取每首歌歌词
for (song_id, song_name) in zip(song_ids, song_names):
    # 歌词 API URL
    lyric_url = 'http://music.163.com/api/song/lyric?os=pc&id=' + song_id + '&lv=-1&kv=-1&tv=-1'
    lyric = get_song_lyric(headers, lyric_url)
    all_word = all_word + ' ' + lyric
    print(song_name)
# 根据词频 生成词云
create_word_cloud(all_word)

