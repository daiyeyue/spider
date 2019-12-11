'''
findall案例
'''
import re

pattern = re.compile(r'\d+')

s = pattern.findall("i am 18 years odl and 185 high")

print(s)
print(type(s))
for i in range(0,len(s)):
    print(s[i])

s = pattern.finditer("i am 18 years odl and 185 high")

print(type(s))

for i in s:
    print(i.group())
