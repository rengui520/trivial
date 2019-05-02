#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/2 14:25 
# @Author : 韧桂 
# @Site :  
# @File : 0302.py 
# @Software: PyCharm
from urllib.parse import urlencode
from fake_useragent import UserAgent
import requests

keyword = '风景'

'''
#启动代理池
#proxy_pool_url = 'http://0.0.0.0:5555/get'

#代理需设置全局变量
proxy = None  #先一开始用本机IP进行爬取
max_count = 5

def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None
'''

base_url = 'https://weixin.sogou.com/weixin?'

for i in range(10):
    ua = UserAgent()
    headers = { 'User-Agent': ua.chrome,
                'Cookie': 'SUID=E524B5754A42910A000000005C486694; GOTO=Af99047; SNUID=110C47812B2EA82D933368D72BFC4F7C; SUID=3B276DAB3320910A000000005C791795; SUV=1551439765053021; ABTEST =0|1551439780|v1; weixinIndexVisited=1; sct=2; IPLOC=US; JSESSIONID=aaaV_HTrCV-bs5r5SmZKw',
                'DNT': '1',
                'Host': 'weixin.sogou.com',
                'Referer': 'https://weixin.sogou.com/weixin?query=%E9%A3%8E%E6%99%AF&_sug_type_=&sut=10105&lkt=1%2C1551444385751%2C1551444385751&s_from=input&_sug_=y&type=2&sst0=1551444385855&page=4&ie=utf8&w=01019900&dr=1',
                'Upgrade-Insecure-Requests': '1'
               }


def get_html(url, count=1):
    #global proxy
    try:
        #if proxy:  # 判断是否有代理
            #proxies = {
             #   'http': 'http://' + proxy
            # }
            #response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        #else:
            #response = requests.get(url, allow_redirects=False, headers=headers)
        response = requests.get(url, allow_redirects=False, headers=headers)  #allow_redirects=False阻止状态码跳转
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            #Need Proxy
            #pass
            print('302')
            '''
            proxy = get_proxy()
            if proxy:
                print('Using Proxy', proxy)
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
            '''
    except ConnectionError as e:
        #print('Error Occurred', e.args)  #判断请求次数
        #proxy = get_proxy()
        #count += 1   #请求次数加一
        return get_html(url)  #重新请求


def get_index(keyword, page):
    data = {
        'query': keyword,
        '_sug_type_': '',
        'sut': '10105',
        'lkt': '1',
        'lkt': '1551444385751',
        'lkt': '1551444385751',
        's_from': 'input',
        '_sug_': 'y',
        'type': '2',
        'sst0': '1551444385855',
        'page': page,
        'ie': 'utf8',
        'w': '01019900',
        'dr': '1'
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

#循环验证，请求100次，看是否出现反爬虫
def main():
    for page in range(1, 101):
        html = get_index(keyword, page)
        print(html)


if __name__ == '__main__':
    main()