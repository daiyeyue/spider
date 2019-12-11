'''
利用request下载页面
自动检测页面编码

'''

from urllib import request
#import urllib
import chardet

if __name__ == '__main__':
    #url = 'http://stock.eastmoney.com/news/1407,20170807763593890.html'
    url = "http://oa.jiudaotech.com:8888/portal/#/login"

    #rsp = urllib.request.urlopen(url)
    rsp = request.urlopen(url)

    html = rsp.read()

    #利用 chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    print(cs.get("encoding", "utf-8"))


    # 使用get取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)