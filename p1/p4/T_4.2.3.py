# findall()函数
# 返回字符串所有的数字
import re
import requests
a = 'one1two2three3'
infos = re.findall('\d', a)
print(infos)
res=requests.get('http://bj.xiaozhu.com/')
prices=re.findall('<span class="result_price">&#165;<i>(.*?)</i>/晚</span>',res.text)
for price in prices:
    price(price)

