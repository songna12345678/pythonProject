import re

a = 'xxIxxjshdxxlovexxsffaxxpythonxx'
infos = re.findall('xx(.*?)xx', a)
print(infos)  # findall方法返回的为列表结构

# search()函数
# 表达式re.match(pattern,string,flags=0)
# pattern为匹配的正则表达式   string为匹配的字符串   flags为标志位，用于控制正则表达式的匹配方式，如是否区分大小写，多行匹配等

a = 'one1two2three3'
infos = re.search('\d+', a)
print(infos)
print(infos.group())  # group方法获取信息
