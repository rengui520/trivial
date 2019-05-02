#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/2/17 18:04 
# @Author : 韧桂 
# @Site :  
# @File : 0217.py 
# @Software: PyCharm
import os
import re
from urllib.parse import urlencode
import requests
from hashlib import md5
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
from config import *
import pymongo
from json.decoder import JSONDecodeError
from multiprocessing import Pool  #引入进程池


client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]

def get_page_index(offset, keyword):  #将可变的参数传入进去，抓取网页源代码
    data = {
        'aid': '24',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400'}
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            return response.text
        return None
    except RequestException:
        print('请求索引页出错')
        return None

def parse_page_index(html):    #抓取文章的url
    try:
        data1 = json.dumps(html)  #用json.loads 方法将json字符串转换成json格式的变量
        data = json.loads(data1)  #用json.loads 方法将json字符串转换成json格式的变量
        # if html is None:
        #先加一判断，来保证json数据含有data这个属性的。含有data属性后，再将data其遍历，再将其里面的每一条数据量按照url地址提取出来
        if data and 'data' in data.keys():  #data.keys返回的是json的所有的键名
            for item in data.get('data'):   #判断data是在这个键名里，说明是含有data这个信息的
                yield item.get('article_url')   #再对这个data进行遍历,把每一个item进行循环，把article_url提取出来。通过yield构造一个生成器，就可以把所有的article_url提取出来
    except JSONDecodeError:
        pass

def get_page_detail(url):  # 提取详情页的组图信息
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400'}
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错',url)
        return None

def parse_page_detail(html,url):#解析详情页内容
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()  #get_text提取文本信息
    print(title)
    #images_pattern = re.compile('BASE_DATA.galleryInfo = .*?gallery: JSON.parse(.*?),',re.S)
    images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\)')  #利用转义符保留括号进行匹配
    result = re.search(images_pattern,html)  #search方法对整个文档传入正则对象，再把字符串传进来。group(1),定义的第一个括号里的内容
    if result:  #判断匹配是否成功
        #print(result.group(1))
        data = json.loads(re.sub(r'\\', '', result.group(1)))  #去掉的是两个连续的反斜杠。正则处理后，实际上是一个字典形式的字符串，我们使用json.loads()将其转换，具体注释同上
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images: download_image(image)  #获取
            return {
                'title': title,
                'url': url,
                'images': images
            }

def save_to_mongo(result):#定义存储mongodb的方法
    if db[MONGO_TABLE].insert_one(result):  #insert已被弃用。使用insert_one或insert_many代替。
        print('存储到MongoDB成功', result)
        return True
    return False

def download_image(url):
    print('正在下载' ,url)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400'}
        response = requests.get(url, headers=headers)
        if response.status_code ==200:
            save_image(response.content)  #content返回二进制内容，text返回网页结果
        return None
    except RequestException:
        print('请求图片出错',url)
        return None

def save_image(content):   #下载图片
    #file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest() ,'jpg') #定义文件名称，第一个为路径、第二个为文件名、第三个为后缀。format构造字符串，当前脚本路径，md5可解决因多次运行程序而产生重复图片的问题
    file_path = '{0}/{1}.{2}'.format('E:/wenben/20190219', md5(content).hexdigest() ,'jpg')   #指定存储目录
    if not os.path.exists(file_path):  #如果文件不存在，则保存
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()

def main(offset):
    html = get_page_index(offset, KEYWORD)
    for url in parse_page_index(html):    #调用生成器，提取所有的url，利用for循环输入生成器，把html传入进去
        #print(url)
        html = get_page_detail(url)
        if html:   #如果成功返回
            result = parse_page_detail(html,url)  #调用解析函数
            #print(result)
            if result:
                save_to_mongo(result)  #调用save_to_mongo方法

if __name__ == '__main__':
    #main()
    groups = [x * 20 for x in range(GROUP_START, GROUP_END + 1)]  #range方法左包括，右不包括
    pool = Pool()  #声明进程池
    pool.map(main, groups)  #pool.map方法开启多进程。第一个为要执行的目标元素，第二个为参数集合
    pool.close()
    pool.join()

