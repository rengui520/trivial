#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/4/24 10:39 
# @Author : 韧桂 
# @Site :  
# @File : spider.py 
# @Software: PyCharm
from selenium import webdriver
from lxml import etree
import pandas as pd
import json
import csv
import codecs

director = u'宁浩'
# 写 CSV 文件
file_name = './' + director + '.csv'

def getUrl(html):
    for i in range(0, 45, 15):
        url = 'https://movie.douban.com/subject_search?search_text=' + director + '&cat=1002&start=0' + str(i)
        # scrapyPage(url)
        driver = webdriver.Chrome()
        driver.get(url)
        # print(driver.page_source)
        html = driver.page_source
        html = etree.HTML(html)

# url = ['https://movie.douban.com/subject_search?search_text=' + director + '&cat=1002&start=' + str(i) for i in range(0, 45, 15)]

def dataWriteCsv(datas):
	file_csv = open(file_name, 'w+', newline='', encoding='utf-8-sig')
	writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL )

	for data in datas:
		writer.writerow(data)
		print("保存文件成功，处理结束")

def scrapyPage(html):
    # html = etree.HTML(html)
    # 设置电影名称，导演演员 的 XPATH
    movie = html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div/div/a/text()')
    # movie_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']/text()")
    name = html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div/div[4]/text()')
    # name_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']/text()")

    items = (movie, name)
    for item in items:
        print(item)
        dataWriteCsv(item)

if __name__ == '__main__':
    # getUrl()
    scrapyPage()