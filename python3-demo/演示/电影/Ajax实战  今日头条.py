#coding:utf-8
import requests
from urllib.parse import urlencode
from requests import codes
import os
from hashlib import md5
from multiprocessing.pool import Pool

def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
# '''
#         get_page()加载单个Ajax请求的结果。其中唯一变化的参数就是offset，所以我们将它当作参数传递。
#         用urlencode()方法构造请求的GET参数，然后用requests请求这个链接，如果返回状态码为200，则调用response的json()方法将结果转为JSON格式，然后返回。
#
#         今日头条的数据是用 json 来请求的，所以我们在 Network 的 Headers 中可以看到它的请求参数，这部分就是我们需要的请求体中的参数。
#         我们就可以利用 urlencode() 来构造这请求参数
#
#         接下来，在实现一个解析方法：提取每条数据的image_detail字段中的每一张图片链接（在image_list中） ，将图片链接和图片属性的标题一并返回，此时可以构造一个生成器。
#         '''

def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': 'https:' + image.get('url'),
                    'title': title
                }

def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image'))
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(file_name=md5(resp.content).hexdigest(),file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)



                #接下来，实现一个保存图片的方法save_image()，其中item就是前面get_image()方法返回的一个字典。再该方法中，首先根据item的title来创建文件夹，然后请求
                #这个图片链接，获取图片的二进制数据，以二进制的形式写入文件。图片的名称可以使用其内容的MD5值，这样可以去除重复。

#def save_image(item):
    #if not os.path.exists(item.get('title')):
        #os.makedirs(item.get('title'))
    #try:
        #response = requests.get(item.get('image'))
        #if response.status_code == 200:
            #file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
            #if not os.path.exists(file_path):
                #with open(file_path, 'wb') as f:
                    #f.write(response.content)

            #else:
                #print('Already Downloaded', file_path)
    #except requests.ConnectionError:
        #print('Failed to Save Image，item ')

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)
        '''
        最后，只需要构造一个offset数组，遍历offset，提取图片链接，并将其下载即可。
        '''

GROUP_START = 0
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
    '''
    这里定义了分页的起始页和终止页数，分别为GROUP_START和GROUP_END，还利用了多线程的线程池，调用其map()方法实现多线程下载。
    '''