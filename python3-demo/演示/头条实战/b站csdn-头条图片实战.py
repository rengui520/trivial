import requests
from requests.exceptions import RequestException
from urllib.parse import urlencode
import json
from bs4 import BeautifulSoup
import re
# import pymongo
import os
from hashlib import md5
from multiprocessing import Pool


def get_page_index(offset, keyword):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count':  '20',
        'cur_tab': '3',
        'from': 'gallery'
    }
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求索引页失败", url)
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')


def get_page_detail(url):
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求出错", url)
        return None


def parse_page_detail(html, url):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    patterns = re.compile('gallery: JSON.parse\("(.*?)"\)', re.S)
    results = re.search(patterns, html)
    if results:
        result = results.group(1)
        data = json.loads(re.sub(r'\\', '', result))
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:
                download_iamge(image)
            return {
                'title': title,
                'url': url,
                'images': images
            }


def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MongDB成功', result)
        return True
    return False


def download_iamge(url):
    print('正在下载', url)
    headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_image(response.content)
        return None
    except RequestException:
        print("请求图片页面出错", url)
        return None


def save_image(content):
    file_path = '{0}\\{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    html = get_page_index(offset, '长泽雅美')
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html, url)
            # save_to_mongo(result)


# MONGO_URL = 'localhost'
# MONGO_DB = 'toutiao'
# MONGO_TABLE = 'toutiao'
# client = pymongo.MongoClient(MONGO_URL)
# db = client[MONGO_DB]
GROUP_START = 1
GROUP_END = 20



if __name__ == '__main__':
    groups = [x*20 for x in range(GROUP_START, GROUP_END+1)]
    pool = Pool()
    pool.map(main, groups)