import requests
import re  # 导入相应的库名

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    # 加入请求头
}
info_lists = []  # 初始化列表 用于装入爬虫信息


def judgment_sex(class_name):  # 定义获取用户性别的函数
    if class_name == 'womenIcon':
        return '女'
    else:
        return '男'


def get_info(url):
    res = requests.get(url)
    ids = re.findall('<h2>(.*?)</h2>', res.text, re.S)
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', res.text, re.S)
    sexs = re.findall('<div class="articleGender (.*?)">', res.text, re.S)
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', res.text, re.S)
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', res.text, re.S)
    comments = re.findall('<i class="number">(\d+)</i>评论', res.text, re.S)
    for id, level, sex, content, laugh, comment in zip(ids, levels, sexs, contents, laughs, comments):
        info = {
            'id': id,
            'level': level,
            'sex': judgment_sex(sex),  # 调用judgment_sex()函数
            'content': content,
            'comment': comment
        }
        info_lists.append(info)  # 获取数据，并append到列表中


if __name__ == '__main__':  # 程序主入口
    urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i))
            for i in range(1, 3)]
    for url in urls:
        get_info(url)  # 循环调用获取爬虫信息的函数
    for info_list in info_lists:
        f = open('D:/data/python/p4/qiushi.txt', 'a+')
        # 遍历列表，创建TXT文件
        try:
            f.write(info_list['id'] + '\n')
            f.write(info_list['level'] + '\n')
            f.write(info_list['sex'] + '\n')
            f.write(info_list['content'] + '\n')
            f.write(info_list['laugh'] + '\n')
            f.write(info_list['comment'] + '\n')
            f.close()  # 写入数据到TXT中
        except UnicodeEncodeError:
            pass  # pass 掉错误编码
