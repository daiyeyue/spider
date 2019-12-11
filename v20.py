'''
爬去豆瓣电影数据
了解ajax的基本爬去方式

'''
from urllib import request
from urllib import error
import requests
import json



url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"
#url = r"http://movie.douban.com/"
#url = "http://www.baidu.com/"

#try:
rsp = request.urlopen(url)
# rsp = requests.post(url)
# print(rsp)
data = rsp.read().decode()

data = json.loads(data)

print(data)
# except error.URLError as e:
#     print(e)