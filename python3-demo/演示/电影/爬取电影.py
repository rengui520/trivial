#*-*-coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
with open('E:\\wenben\\20190316\\2019031601.txt','w',encoding='utf-8') as f:
	url = 'http://nlook1.cn/index.php?s=/vod-type-id-1-type--area--year--star--state--order-hits.html'
	urls = ['http://nlook1.cn/index.php?s=/vod-type-id-1-type--area--year--star--state--order-hits-{}.html'.format(str(i)) for i in range(1,4)]
	
	def get_attactions(url,date=None):
		wb_date = requests.get(url)
		soup = BeautifulSoup(wb_date.text,'lxml')
		titles = soup.select('ul.a > p')
		imgs = soup.select('ul.a > img')
		movies = soup.select('li.col-md-2 col-sm-3 col-xs-4 > a')
		time.sleep(1)
		for title,img,movie in zip(titles,imgs,movies):
			f.write("{},,{},{}\n".format(img.get('data-original'),title.get_text(),'http://nlook1.cn/index.php?s=/vod-play-id-'+ movie.get('href')[6:13]+'-sid-1-pid-1.html'))
	for single_url in urls:
		get_attactions(single_url)
		print(single_url)
