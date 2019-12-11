from urllib import request
from bs4 import BeautifulSoup
import re


url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

print("==" * 12)
print(soup.head)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)  ##是一个字典类型
print(soup.link.attrs['type'])
print(soup.name)
print(soup.attrs)


print("==" * 12)
tags = soup.find_all(name="meta")
print(tags)  ##返回来是列表
print("==" * 12)

print("==" * 12)
tags = soup.find_all(re.compile('^me'), content="always")
for tag in tags:
    print(tag)
print("==" * 12)

