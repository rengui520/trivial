#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/23 17:56
# @Author : 韧桂
# @Site :
# @File : douban_movie_spider.py
# @Software: PyCharm


# 下载某个导演的电影数据集
from lxml import etree
import time
from selenium import webdriver
import csv

driver = webdriver.Chrome()
# 设置想要下载的导演 数据集
director = u'漫威'
# 写 CSV 文件
file_name = './' + director + '.csv'
base_url = 'https://movie.douban.com/subject_search?search_text='+director+'&cat=1002&start='
out = open(file_name,'w', newline='', encoding='utf-8-sig')
csv_write = csv.writer(out, dialect='excel')
flags=[]

# 下载指定页面的数据
def download(request_url):
	driver.get(request_url)
	time.sleep(1)
	html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
	html = etree.HTML(html)
	# 设置电影名称，导演演员 的 XPATH
	movie_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']")
	name_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']")
	# 获取返回的数据个数
	num = len(movie_lists)
	if num > 15: # 第一页会有 16 条数据
		# 默认第一个不是，所以需要去掉
		movie_lists = movie_lists[1:]
		name_lists = name_lists[1:]
	for (movie, name_list) in zip(movie_lists, name_lists):
		# 会存在数据为空的情况
		if name_list.text is None:
			continue
		# 显示下演员名称
		print(name_list.text)
		names = name_list.text.split('/')
		# 判断导演是否为指定的 director
		if names[0].strip() == director and movie.text not in flags:
			# 将第一个字段设置为电影名称
			names[0] = movie.text
			flags.append(movie.text)
			csv_write.writerow(names)
	# print('OK') # 代表这页数据下载成功
	print(num)
	if num >= 14: # 有可能一页会有 14 个电影
		# 继续下一页
		return True
	else:
		# 没有下一页
		return False

# 开始的 ID 为 0，每页增加 15
start = 0
while start<10000: # 最多抽取 1 万部电影
	request_url = base_url + str(start)
	# 下载数据，并返回是否有下一页
	flag = download(request_url)
	if flag:
		start = start + 15
	else:
		break
out.close()
# print('finished')



# from selenium import webdriver
# from lxml import etree
# import pandas as pd
# import json
# import csv
# import codecs
#
# director = u'宁浩'
# # 写 CSV 文件
# file_name = './' + director + '.csv'
#
# def getUrl():
#     for i in range(0, 45, 15):
#         url = 'https://movie.douban.com/subject_search?search_text=' + director + '&cat=1002&start=0' + str(i)
#         scrapyPage(url)
# # url = ['https://movie.douban.com/subject_search?search_text=' + director + '&cat=1002&start=' + str(i) for i in range(0, 45, 15)]
#
# def dataWriteCsv(datas):
# 	file_csv = open(file_name, 'w+', newline='', encoding='utf-8-sig')
# 	writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL )
#
# 	for data in datas:
# 		writer.writerow(data)
# 		print("保存文件成功，处理结束")
# 	# dataframe = pd.DataFrame(datas)
# 	#
# 	# # 将DataFrame存储为csv,index表示是否显示行名，default=True
# 	# dataframe.to_csv(file_name, index=False, sep=',')
#
#
# # def dataWriteCsv(content):
#     # with open(file_name, "w") as csvfile:
#     #     writer = csv.writer(csvfile)
#
#     # out = open(file_name,'w', newline='', encoding='utf-8-sig')
#     # csv_write = csv.writer(out, dialect='excel')
#     # flags=[]
#
#
#
#     # file_csv = codecs.open(file_name, 'w+', encoding='utf-8-sig')
#     # writer = csv.writer(file_csv, dialect='excel')
#
#
#
# def scrapyPage(url):
#     driver = webdriver.Chrome()
#     driver.get(url)
# # print(driver.page_source)
#
#     html = driver.page_source
#     html = etree.HTML(html)
#     # 设置电影名称，导演演员 的 XPATH
#     movie = html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div/div/a/text()')
#     # movie_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']/text()")
#     name = html.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div/div/div/div[4]/text()')
#     # name_lists = html.xpath("/html/body/div[@id='wrapper']/div[@id='root']/div[1]//div[@class='item-root']/div[@class='detail']/div[@class='meta abstract_2']/text()")
#
#     items = (movie, name)
#     for item in items:
#         print(item)
#         dataWriteCsv(item)
#
# if __name__ == '__main__':
#     getUrl()




# query = '王祖贤'
# for i in range(0, 22471, 20): #
#     url = 'https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i)
#     print(url)
# url = ['https://www.douban.com/j/search_photo?q=' + query + '&limit=20&start=' + str(i) for i in range(0, 30, 15)]
# print(url)

# director = '张艺谋'
# url = ['https://movie.douban.com/subject_search?search_text=' + director + '&cat=1002&start=' + str(i) for i in range(0, 45, 15)]
#
# print(url)


