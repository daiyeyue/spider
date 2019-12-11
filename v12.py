from urllib import request


if __name__ == '__main__':

    url = "http://www.renren.com/972734682"

    headers = {
        "Cookie": "anonymid=k2e7uieu5u63hr; depovince=GW; _r01_=1; jebe_key=39a4c481-a4bd-4b6c-a7c3-a61e075a6d18%7C5f2ab1e402a976c0338ca4042c2455ac%7C1572496696694%7C1%7C1572496697596; jebecookies=25664c04-2dfe-4827-9105-682b55005b14|||||; JSESSIONID=abcwu4KKZK_dD9B7u4L4w; ick_login=4d9896ea-68de-4b25-b0ed-246f3d4d5379; _de=C5D376DBECF9C2A7C036652B0B72DDAA; p=212b6b25b3d65731588196864135446d2; first_login_flag=1; ln_uact=18665633547; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=ce2aeb280d569667ac140b3f71d60ff92; societyguester=ce2aeb280d569667ac140b3f71d60ff92; id=972734682; xnsid=da1e84b0; ver=7.0; loginfrom=null; jebe_key=39a4c481-a4bd-4b6c-a7c3-a61e075a6d18%7C5f2ab1e402a976c0338ca4042c2455ac%7C1572496696694%7C1%7C1572593569548; wp_fold=0"
    }


    req = request.Request(url, headers=headers)

    #rsp = request.urlopen(req)
    #print(rsp.read())

    html = request.urlopen(req).read().decode()
    # html = html.decode()
    # print(html)
    print(html)


    with open("rsp.html", "w",encoding='utf-8') as f:
        f.write(html)
