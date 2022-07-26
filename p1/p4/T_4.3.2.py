import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 6.1;WOW64) AppleWebKIt/537.36(KHTML,like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
f = open('D:/data/python/p4/doupo.txt', 'a+')  # 新建TXT文档，追加的方式


def get_info(url):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>', res.content.decode('utf-8'), re.S)
        print(type(contents))
        for content in contents:
            f.write(str(content) + '\n')
    else:
        pass


if __name__ == '__main__':
    urls = ['http://www.doupoxs.com/doupocangqiong/{}.html'.format
            (str(i)) for i in range(2, 3)]
    for url in urls:
        get_info(url)
        time.sleep(1)

f.close()
