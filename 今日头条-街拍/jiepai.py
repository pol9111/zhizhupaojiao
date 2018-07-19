import requests, os, random, time
from urllib.parse import urlencode
from multiprocessing.pool import Pool
from hashlib import md5

def get_page(offset):
    '''
    加载单个Ajax请求的结果
    :param offset:
    :return:页面的json内容
    '''
    HEADERS =  {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",}
    ips = [
        {"http": "http://82.202.70.132:8080"},
        {"http": "http://85.198.82.142:53281"},
        {"http": "http://168.194.155.19:53281"},
        {"http": "http://188.119.30.106:9090"},
        {"http": "http://115.233.209.134:3128"},
        {"http": "http://170.238.63.244:53281"},
        {"http": "http://169.255.237.170:53281"},
        {"http": "http://91.197.105.40:8080"},
        {"http": "http://185.253.88.10:80"},
    ]
    params = {
        "offset": offset,
        "format":"json",
        "keyword": "街拍",
        "autoload": "true",
        "count": "20",
        "cur_tab": "1",
    }
    url = "https://www.toutiao.com/search_content/?" + urlencode(params)
    try:
        rs = requests.get(url, headers=HEADERS, proxies=random.choice(ips))
        if rs.status_code == 200:
            return rs.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    '''
    提取每条数据的image_list字段中的每一张图片链接
    :param json:
    :return:图片链接和图片所属的标题的生成器
    '''
    if json.get('data'):
        for item in json.get('data'):
            if item.get('image_list'):
                title = item.get('title')
                images = item.get('image_list')
                for image in images:
                    yield {
                        'image': 'http:' + image.get('url'),
                        'title': title
                    }
            else:
                pass


def save_image(item):
    '''
    保存图片, 图片的名称使用其内容的MD5值, 这样可以去除重复
    :param item:
    :return:
    '''
    os.chdir('F:\py_first\jiepai')
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        rs = requests.get(item.get('image'))
        if rs.status_code == 200:
            # 图片路径
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(rs.content).hexdigest(), 'jpg')
            # 如果没有这张图片
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(rs.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')

def main(offset):
    '''
    遍历offset，提取图片链接
    :param offset:
    :return:
    '''
    time.sleep(10)
    print('网站有反爬请等待10秒') # 或更长
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 100

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END+1)])
    pool.map(main, groups)
    pool.close()
    pool.join()





