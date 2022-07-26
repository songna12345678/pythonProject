# sub函数
# 语法re.sub(pattern,repl,string,count=0,flags=0)
# pattern为正则表达式 repl为替代的字符串 string为要被查找的原始字符串 counts为模式匹配后替换所有的匹配
# flags为标志位 用于控制正则表达式的匹配方式 如何区分大小写 多行匹配等
import re

phone = '123-4567-1234'
new_phone = re.sub('\D', '', phone)
print(new_phone)  # sub()方法用于替换
