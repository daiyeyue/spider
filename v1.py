from urllib import request
from io import BytesIO
import gzip
'''
使用urllib.request请求一个网页内容，并把内容打印出来
'''


if __name__ == '__main__':

    #url = "http://jobs.zhaopin.com/195435110251173.htm?ssidkey=y&ss=409&ff=03&sg=2644e782b8b143419956320b22910c91&so=1"
    #url = "http://jobs.zhaopin.com/148733833250658.htm"
    #url = "www.baidu.com"
    url = "http://oa.jiudaotech.com:8888/portal/#/login"
    # 打开相应url并把相应页面作为返回
    rsp = request.urlopen(url)
    print(type(rsp))

    # 把返回结果读取出来
    # 读取出来内容类型为bytes
    html = rsp.read()
    print(type(html))
    print(html)


    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode("utf-8")

    print(html)
