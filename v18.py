
'''
破解有道词典
V1
'''

from urllib import request, parse


def youdao(key):

    #url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    #浏览器F12，从form data来
    data = {
        "i": key,
        "from":"AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15729354211480",
        "sign": "0db23eae3ca774eff323fa6ee2b6e3ef",
        "ts":"1572935421148",
        "bv":"d2685b66b612e42764cb7b20e19ecbe4",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action":"FY_BY_REALTIME"
        #"typoResult": "false"
    }

    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    # 浏览器F12，从Request Header来
    headers = {
                  "Accept": "application/json,text/javascript,*/*;q=0.01",
                  #"Accept-Encoding": "gzip,deflate",
                  "Accept-Language": "zh-CN,zh;q=0.9",
                  "Connection": "keep-alive",
                  "Content-Length": "236",
                  "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                  "Cookie": "OUTFOX_SEARCH_USER_ID=-1344555455@10.108.160.18; JSESSIONID=aaa6ZS9B3xsXJ-bboP54w; OUTFOX_SEARCH_USER_ID_NCOO=2018561729.187486; ___rl__test__cookies=1572935421143",
                  "Host": "fanyi.youdao.com",
                  "Origin": "http://fanyi.youdao.com",
                  "Referer": "http://fanyi.youdao.com/",
                  "User-Agent": "Mozilla/5.0( X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36 X-Requested-With: XMLHttpRequest"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)

if __name__ == '__main__':
    youdao("boy")
