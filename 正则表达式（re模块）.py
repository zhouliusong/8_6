"""
座右铭:心不狠，站不稳！欧耶！
@project:8_6
@author:Mr.Zhou
@file:正则表达式（re模块）.PY
@ide:PyCharm
@time:2018-08-06 16:29:43
"""
import re
# 正则表达式：是对字符串的内容进行匹配查询的一种操作方式，通过预先定义的一些特殊字符的组合，形成一种只负责的匹配规则。再根据这些跪着来对字符串中的某一些内容进行提取或者查找。
# 常用的正则表达式转移字符：
'''
\d：匹配一个数字
\w：用于匹配一个数字或者字母
.:可以匹配前面字符后面的、跟着的任意字符。a.：可以匹配到ab，ac，ad，abcdef，
*：可以匹配前面字符0个或者多个。a*：可以匹配到0个或者，aa，aaa，aaaa.....
?：可以匹配前面字符0个或者1个。a?：可以匹配到0个a，或者1个a
+：可以匹配前面字符任意多个，但是至少为1个，不能为0个。a+：可以匹配到a,aa,aaa,:单数不能一个都匹配不到。
^：表示必须以某某字符开头。^a：只能匹配以a开头的字符。（a）
$：表示必须以某摩字符结尾。a$：只能匹配到以a结尾的字符（a）
.*：表示任意字符出现0个或者多个，也称之为贪婪匹配模式，就是尽可能的匹配符合要求的最大值。a.*b：可以匹配到ab；也可以匹配到asdb，akdyfgauefb。
.*?：这个组合叫做非贪婪模式，在能匹配成功的前提下，尽可能少的匹配符合要求的字符。
.+：表示任意字符至少出现一次，不能为0次。a.+b:(ab不能被匹配到)acb,agddfb
|：用于设置不同情况的正则表达式，表示或者
'''

# 目标字符串：123456abcefg
# 1、创建正则表达式对象compile()：括号里面填写的是字符串的匹配规则
# ()表示从目标字符串中提取的子串，一个()对应着一个分组信息。
patten_obj=re.compile('(\d+)(\w+)')
# 2、根据正则表达式对象，从目标字符创进行匹配。
# math()：第一个参数：正则表达式对象；第二个参数：目标字符串.
# math()：是从头开始匹配
res=re.match(patten_obj,'123456abcefg')
print(res.group(1))
print(res.group(2))
print(type(res.group(1)))

pattern_obj1=re.compile('(c.)')
res1=re.match(pattern_obj1,'cbdefg')
print(res1.group(1))

pattern_obj2=re.compile('(a*)')
res2=re.match(pattern_obj2,'aaabcdefg')
print(res2.group(1))

pattern_obj3=re.compile('(a?)')
res3=re.match(pattern_obj3,'aabcdefg')
print(res3.group(1))

pattern_obj11=re.compile('(a+)')
res11=re.match(pattern_obj11,'aaaaaaqweadf')
print(res11.group((1)))

pattern_obj12=re.compile('(^a)')
res12=re.match(pattern_obj12,'aafawqe')
print(res12.group(1))

# match()函数要求重头开始匹配，在下面情况下，找一a结尾的字符，那么只能识别a不能有其他字符
pattern_obj13=re.compile('(a$)')
res13=re.match(pattern_obj13,'a')
print(res13.group(1))

pattern_obj14=re.compile('(a.*b)')
res14=re.match(pattern_obj14,'afnfbkdhb')
print(res14.group(1))

pattern_obj15=re.compile('(a.*?b)')
res15=re.match(pattern_obj15,'afnfbkdhb')
print(res15.group(1))

pattern_obj16=re.compile('(a.+b)')
res16=re.match(pattern_obj16,'acbdb')
print(res16.group(1))

pattern_obj17=re.compile('((haha|heihei)123)')
res17=re.match(pattern_obj17,'heihei123')
# res18=re.match(pattern_obj17,'haha123')
print(res17.group(1))
print(res17.group(2))
# print(res18.group(1))
# print(res18.group(2))









