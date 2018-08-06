"""
座右铭:心不狠，站不稳！欧耶！
@project:8_6
@author:Mr.Zhou
@file:正则表达式常用函数.PY
@ide:PyCharm
@time:2018-08-06 17:37:02
"""
import re
# match()：是从目标字符串的开头位置开始匹配，仅限于开头位置，匹配成功则返回match对象，否则返回None
pattern_obj=re.compile('(my)')
res=re.match(pattern_obj,'myaskdga')
print(res.group(1))

# search()：从目标字符串的任意位置开始匹配数据，仅匹配成功一次，如果目标字符串有多个符合要求的结果，也只能找到一个。
pattern_obj=re.compile('(my)') # my加上括号输出的是后可以用group()函数，不加输出的时候只能用res[0]的方式
res=re.search(pattern_obj,'hahamyaskmydga')
print(res[0])
# print(res.group(1))

# findall()：搜索整个目标字符创，会将所有匹配日成功的字符串都返回出来
pattern_obj=re.compile('my')
res=re.findall(pattern_obj,'myaskmydga')
print('=====',res[0])
print('=====',res[1])
# for x in res:
#     print(x)

# split()：以匹配到的符合要求的字符串为分隔符，将目标字符串分割成一个列表
pattern_obj=re.compile('(my)')
res=re.split(pattern_obj,'trmyaskmydga')
print('+++++',res)

# sub()：使用一个新的字符来替换目标字符串中符合匹配要求的字符。
pattern_obj=re.compile('-')
res=re.sub(pattern_obj,'+','a-b-c')
print(res)







