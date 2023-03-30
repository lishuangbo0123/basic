

# -- coding: utf-8 --
import requests
import json
from lxml import etree
# url = "https://www.zhipin.com/wapi/zpgeek/mobile/search/joblist.json?city=101280600&querySource=1&page=4&city=&query="
# url ='https://www.zhipin.com/job_detail/75fadf30a41e10961n150968FFNW.html'
# url ='https://www.zhipin.com/job_detail/75fadf30a41e10961n150968FFNW.html'
url ='https://wz.sun0769.com/political/index/politicsNewest?id=1&page=2'
# url = 'https://httpbin.org/get'
# url = 'http://v2.api.juliangip.com/dynamic/getips?num=1&pt=1&result_type=json&trade_no=1799709907102020&sign=9057bae5a1cd9222a126eff9492e742b'
headers ={
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Referer': 'https://www.zhipin.com/?ka=pc',
    # 'Cookie': "lastCity=101280600; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1666073105; wd_guid=5abdd3bc-f09b-4008-bdc4-6afbb0e86687; historyState=state; _bl_uid=tFlyg9mndwXs3gxqsj68m0Uhs48q; __zp_seo_uuid__=2227810d-bdef-44a6-af5b-680cb6e3983e; __g=-; __zp_stoken__=0a14edEx1GxF9ch9MJhEUYXAkZH1cfxMzUEwgRko3UwVYZG8Ib396D31hKwc/XFs8E29hWlcJXxhMPGJ0XgsGOwpvbGR2TQ8qUzFxC0pEYw4DXiEcZFhSCHNHIGJ9HH4Pbk51R18MFkAsaxNEWG1mSgsLUAFyFDYPC0MaCw97BQgMG3QyECsiVzFfRxY/JUwGHEQFZGBNDQ==; __l=r=https://www.baidu.com/link?url=BK-CjEX5ofTmyTWCqEdsixOoMs1EsWWqzNO-5h4Vx3Ss26dFn6STiRPcbaaASfi_&wd=&eqid=e5197bd900018d4900000006634e637d&l=/www.zhipin.com/web/geek/job?query=python&city=101280600&page=2&s=3&g=&friend_source=0&s=3&friend_source=0; __c=1666073105; __a=84328899.1666073105..1666073105.27.1.27.27; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1666081815",
}


def get_proxy():
    try:
        return requests.get("http://127.0.0.1:5010/get?type=http").json()
    except:
        return get_proxy()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

def get_proxy_count():
    return requests.get("http://127.0.0.1:5010/count").json()
# your spider code

def getHtml():
    # a = get_proxy()
    # print(a)
    # proxy = a.get("proxy")
    # html = requests.get(url, headers=headers, proxies={"http": f"http://{proxy}"})
    html = requests.get(url, headers=headers)
    # html.encoding = 'utf-8'
    print(html.request.headers)
    print(html.text)
    # dic = {}
    # dic = json.loads(html.text)
    # print(dic['code'])
    # return html


getHtml()