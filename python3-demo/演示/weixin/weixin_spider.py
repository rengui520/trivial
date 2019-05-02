#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/4/17 16:37
# @Author : 韧桂
# @Site :
# @File : weixin_spider.py
# @Software: PyCharm
from urllib.parse import urlencode
import requests
# from fake_useragent import UserAgent

base_url = 'https://weixin.sogou.com/weixin?'

headers = {
    'Cookie': 'SUID=AD16F3684842910A000000005C8BBA37; SUID=AD16F3685F20940A000000005C8DC9DD; SUV=1552796127398265; weixinIndexVisited=1; IPLOC=CN4503; SNUID=90BCA5D6A8A221264F4A3753A819E9E7; ld=Slllllllll2tHVOAlllllVh1QQwlllllty1Unlllll9lllllRZlll5@@@@@@@@@@; LSTMV=513%2C66; LCLKINT=7794; ABTEST=0|1555323243|v1; sct=4; JSESSIONID=aaa5eAFG-dttfa3oafQOw; ppinf=5|1555489939|1556699539|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTYlOTclQUQlRTklOUMlODF8Y3J0OjEwOjE1NTU0ODk5Mzl8cmVmbmljazoxODolRTYlOTclQUQlRTklOUMlODF8dXNlcmlkOjQ0Om85dDJsdUhrWUMyd0pnSWltZV9uUWlpejMxVlFAd2VpeGluLnNvaHUuY29tfA; pprdig=VcvZyhwxPcKDiwxCwyw2Koh-Uv1YIPN-5G8q3E80pe6DG6QkpohqbvKPtVOCFIKEicErxAvHReq7mi_gcmksxeKFksKKI3oObOQ91d2W-rZ2S_OuSCBBT3w_WQJIFLXm29LuaWUEY4Og8qtFOqLFgpeS80WhdALO1xkagTvwTBc; sgid=01-38033375-AVy25JNahCvzudZ4dtHBSF8; ppmdig=15554899390000009d2b45d27208d0d2841bb54b91a41816',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    # 'User-Agent': UserAgent().random
}

keyword = '风景'
proxy_pool_url = 'http://127.0.0.1:5000/get'

proxy = None  #刚开始先不使用代理
max_count = 5  #定义最大请求次数

def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code ==200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_html(url, count=1):
    print('Crawling', url)
    print('Crying Count', count)

    global proxy #引用全局变量
    if count >= max_count: #判断请求次数
        print('Tried Too Many Counts')
        return None

    try:
        if proxy: #判断是否有代理
            # 设置代理
            proxies = {
                'http': 'http://' + proxy
            }

            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)

        if response.status_code ==200:
            return response.text
        if response.status_code == 302:
            # Need Proxy
            # pass
            print('302')
            proxy = get_proxy()
            if proxy:  #如果代理正常获取，打印输出代理
                print('Using Proxy', proxy)
                # count += 1
                # return get_html(url, count) #重新调用爬取方法
                return get_html(url) #重新调用爬取方法
            else:
                print('Get Proxy Failed')
                return None #如果获取不到代理，返回None
    except ConnectionError as e:
        print('Error Occurred', e.args)  #达到最大错误请求次数，把方法判断为失败，
        proxy = get_proxy()  #更换代理
        count +=1  #如果请求错误，把请求次数加1.
        return get_html(url, count) #递归调用时，把count传过来。

def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html

def main():
    for page in range(1,101):
        html = get_index(keyword, page)
        print(html)

if __name__ == '__main__':
    main()



# #递归
# class Solution:
#     def Sum_Solution(self, n):
#         return n and (n + self.Sum_Solution(n - 1))

# #reduce函数
# class Solution:
#     def Sum_Solution(self, n):
#         # write code here
#         def f(n,m):
#             return n+m
#         return reduce(f,list(range(1,n+1)))


# class Solution:
#     def __init__(self):
#         self.ans = 0
#
#     def Sum_Solution(self, n):
#         self.recur(n)
#         return self.ans
#
#     def recur(self, n):
#         self.ans += n
#         n -= 1
#         return n > 0 and self.Sum_Solution(n)

# class Solution:
#
#     def sum(self, n):
#         """求1 + 2 + 3 +...+ n"""
#         return sum(range(1, n + 1))
#
#
# if __name__ == '__main__':
#     obj = Solution()
#     s = obj.sum(100)
#     print(s)
