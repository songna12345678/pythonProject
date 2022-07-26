from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome / 56.0.2924.87 Safari / 537.36'
}


def get_info(url):
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist > ul > li >a')
    times = soup.select('span.pc_temp_time')
    for rank, title, time in zip(ranks, titles, times):
        #print(title.get_text().replace('\n', '').replace('', '').split('-')[1])
        data = {
            'rank': rank.get_text().strip(),
            'singer': title.get_text().replace('\n', '').replace('	', '').split(' - ')[1],
            'song': str(title.get_text().split('-')[0]).strip('\n\t').strip('\n\t '),
            'time': time.get_text().strip()
        }
        print(data)


if __name__ == '__main__':
    urls = ['http://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in
            range(1, 2)]
    for url in urls:
        get_info(url)
    time.sleep(1)
