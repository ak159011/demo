import re

# 第一个参数表示匹配规则，第二个参数是要匹配到的字符串
# re.match('',x)
# x = re.search(r'^d.*\d+$', '121beanstalk123214214lookaround222 68996')
# print(x)
# try :
#     y = x.group()
# except AttributeError as e:
#     print('AttributeError')
# else :
#     print(y)
#     print(x.groups())
# x='42huh832idiom'
# m=re.search(r'h(\d+)i',x)
# n=re.search(r'h[0-9a-z]+o',x)
# y=re.search(r'^\d+',x)
# print(y.group())
# print(m.group(1))
# print(n.group())

n = input(':')
if re.fullmatch(r'\d+(\.?\d+)?', n):
    print(n, '是个数字')
    print(float(n))
else :
    print('不是数字')
