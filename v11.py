from urllib import request

if __name__ == '__main__':

    url = "http://www.renren.com/972734682"

    rsp = request.urlopen(url)
    #print(rsp.read().decode('gb18030'))
    #print(rsp.read().decode())

    html = rsp.read().decode()
    print(html)
    #print(len(html))

    with open("rsp.html", "w",encoding='utf-8') as f:
        f.write(html)