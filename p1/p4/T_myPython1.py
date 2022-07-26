import re
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    # 加入请求头
}

f = open('D:/data/python/p4/myPython1.txt', 'a+')  # 新建TXT文档，追加的方式)


def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'), re.S)
        for content in contents:
            f.write(content + '\n')
    else:
        pass


if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/1.html']
    for url in urls:
        get_info(url)
        time.sleep(1)
f.close()
