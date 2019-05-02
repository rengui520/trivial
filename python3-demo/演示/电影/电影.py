#coding:utf-8
import requests
import time
from bs4 import BeautifulSoup
with open('E:\\wenben\\20190316\\2019031602.txt', 'w', encoding='utf-8') as f:
    url = 'http://nlook1.cn/index.php?s=/vod-type-id-1-type--area--year--star--state--order-hits-p-.html'
    urls = ['http://nlook1.cn/index.php?s=/vod-type-id-1-type--area--year--star--state--order-hits-p-{}.html'.format(str(i)) for i in range(1, 3)]

    def get_attactions(url, date=None):
        wb_date = requests.get(url)
        soup = BeautifulSoup(wb_date.text, 'lxml')
        titles = soup.select('a > img')
        imgs = soup.select('a > img')
        movies = soup.select('p.image > a')
        print(titles)
        time.sleep(1)
        for title, img, movie in zip(titles, imgs, movies):
            f.write("{},,{},{}\n".format(title.string,img.get('data-original'),'http://nlook1.cn/index.php?s=/vod-play-id-' + movie.get('href')[-10:-5] + '-sid-2-pid-1.html'))

    for single_url in urls:
        get_attactions(single_url)
        print(single_url)