#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/3/1 15:10 
# @Author : 韧桂 
# @Site :  
# @File : 0301.py 
# @Software: PyCharm
#实战淘宝

from fake_useragent import UserAgent

for i in range(10):
    ua = UserAgent()
    headers = {'User-Agent': ua.chrome}
    print(headers)
'''
import requests
import json
import pandas as pd
import time

# 构造循环爬取的函数
def format_url(base_url, num):
    urls = []
    for i in range(0, num * 44, 44):
        urls.append(base_url[:-1] + str(i))
    return urls

# 解析和爬取单个网页
def parse_page(url, cookies, headers):
    result = pd.DataFrame()
    html = requests.get(url, headers=headers, cookies=cookies)
    bs = html.text
    # 获取头部索引地址
    start = bs.find('g_page_config = ') + len('g_page_config = ')
    # 获取尾部索引地址
    end = bs.find('"shopcardOff":true}') + len('"shopcardOff":true}')
    js = json.loads(bs[start:end + 1])

    # 所有数据都在这个auctions中
    for i in js['mods']['itemlist']['data']['auctions']:
        # 产品标题
        product = i['raw_title']
        # 店铺名称
        market = i['nick']
        # 店铺地址
        place = i['item_loc']
        # 价格
        price = i['view_price']
        # 收货人数
        sales = i['view_sales']
        url = 'https:' + i['detail_url']
        r = pd.DataFrame({'店铺': [market], '店铺地址': [place], '价格': [price],
                          '收货人数': [sales], '网址': [url], '产品标题': [product]})
        result = pd.concat([result, r])
    time.sleep(5.20)
    return result


# 汇总
def main():
    # 爬取的基准网页（s = 0）
    base_url = 'https://s.taobao.com/search?q=%E6%B4%97%E5%8F%91%E6%B0%B4&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s=0'
    # 定义好headers和cookies
    cookies = {'cookie': 't=8f4adecbdd77f0ef46d60f9d9cfb02b4; cna=4UPQFFMgrSsCAaxg2EK0c5kU; _cc_=UtASsssmfA%3D%3D; tg=0; thw=cn; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; enc=7ThSyMKaBCJFcVRm1iOOKnEkCqrbJyw4YVXl%2BM3Dvf4EY%2BbwfPlFLNY32rXSuq%2FhkpbYpXtYH5Mhfe5PmaNcTg%3D%3D; l=bB_sGSjnvsxf29xxBOCZCuI8Lu79dIRAguPRwCYMi_5LT68_ThQOl-FQoFJ6Vf5RsLYB4z6vzNp9-etlw; hng=CN%7Czh-CN%7CCNY%7C156; uc3=vt3=F8dByEv0IsqJJWO2AR8%3D&id2=UU8BrRGmvFGIJA%3D%3D&nk2=txBM4zigV%2BQ%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; tracknick=%5Cu4E91%5Cu4E2D%5Cu4FEF%5Cu89C8; lgc=%5Cu4E91%5Cu4E2D%5Cu4FEF%5Cu89C8; mt=ci=28_1; v=0; uc1=cookie14=UoTZ5be3BbiIsg%3D%3D; cookie2=1cb29459e8a9abae1e47ae2c0b2d1984; _tb_token_=531e5a5ae0f6e; JSESSIONID=8BC6B958D23E080FB3727DE4EF470ED5; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; isg=BEBAPjZGCHpuofRXe37sWckUEc7SYd1-3EC5BbrRDNvuNeBfYtn0IxYHSdVQhdxr; swfstore=227002'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    # 设置好存储结果的变量
    final_result = pd.DataFrame()

    # 循环爬取5页
    for url in format_url(base_url, 5):
        final_result = pd.concat([final_result, parse_page(url, cookies=cookies, headers=headers)])
    return final_result

if __name__ == "__main__":
    final_result = main()
'''