#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/25 23:48 
# @Author : Aries 
# @Site :  
# @File : 0125.py 
# @Software: PyCharm
# coding:utf-8
from lxml import etree
import requests
from requests.exceptions import RequestException
import json

def get_one_page(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    s = etree.HTML(html)
    u1s = s.xpath('//*[@id="server-search-app"]/div[2]/div[2]/div/div[2]/ul[5]')

    for u1 in u1s:
        title = u1.xpath('./li/div/div[1]/a/text()')[0].strip()
        image = u1.xpath('./li/a/div/div[1]/img/@src')[0].strip()
        time = u1.xpath('./li/a/div/span/text() ')[0].strip()
        author = u1.xpath('./li/div/div[3]/span[4]/a/text()')[0].strip()
        play = u1.xpath('./li/div/div[3]/span[1]/text()')[0].strip()


        items = (title, image, time, author, play)
        print(items)
        write_to_file(items)


def write_to_file(content):
    with open('E:/wenben/2019012601.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def getUrl():
    for i in range(5):
        url = 'https://search.bilibili.com/all?keyword=python&page={}'.format(i+1)
        html = get_one_page(url)



if __name__ == '__main__':
    getUrl()
