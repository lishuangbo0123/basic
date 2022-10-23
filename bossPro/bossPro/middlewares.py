# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
import random
import json
import time
from scrapy.http.response import Response
from scrapy.http import HtmlResponse
from scrapy.http.response.text import TextResponse
url = "https://www.zhipin.com/wapi/zpgeek/mobile/search/joblist.json?city=101280600&querySource=1&page=4&city=&query="

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25"

]
headers ={
    'User-Agent': random.choice(USER_AGENTS),
    }
class BossproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def get_http_proxy(self):
        time.sleep(1)
        try:
            resp = requests.get("http://127.0.0.1:5010/get/").json()
            return resp
        except:
            # print('请求代理接口出错，重新请求')
            return self.get_http_proxy()
    def delete_proxy(self,proxy):
        # pass
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
    def get_random_proxy_response(self,request):
        # print('随机获取ip')
        proxy = self.get_http_proxy().get("proxy")
        if proxy:
            # try:
            html = requests.get(request.url, headers=headers, proxies={"http": f"http://{proxy}"})
            # 使用代理访问
            if html.status_code == 200:
                resp_text = json.loads(html.text)
                if resp_text['code'] == 5002:
                    self.delete_proxy(proxy)
                    # print(f'代理访问xxxx失败，删除无效代理{proxy}')
                    return self.get_random_proxy_response()
                # print(f'代理访问xxxxx成功{proxy},{resp_text["code"]}')
                return html
            else:
                # print(f'访问xxxxx失败{html.status_code}，重新获取代理')
                self.delete_proxy(proxy)
                return self.get_random_proxy_response()
            # except:
            #     print('访问xxxxx出错了，重新获取代理')
            #     return self.get_random_proxy()
        else:
            print('没有足够代理====================等待30秒')
            time.sleep(30)
            return self.get_random_proxy_response()

    def process_request(self, request, spider):
        request.headers["User-Agent"] = random.choice(USER_AGENTS)
        return None

    def process_response(self, request, response, spider):
        # print('拦截响应')
        if "job_detail" in request.url:
            # print('详情页')
            # print(f'test meta data is {request.meta["item"]}')
            bro = spider.bro
            bro.get(request.url)
            time.sleep(4)
            page_text = bro.page_source  # 包含了动态加载的新闻数据
            res = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            print(f'return respose an detail_url is {request.url}')
            return res
        else:
            resp = self.get_random_proxy_response(request)
            res = TextResponse(url=request.url, encoding='utf-8', body=resp.text)
            print(f'return respose an page_url is {request.url}')
            return res



    def process_exception(self, request, exception, spider):
        pass
        # print(f'拦截请求报错{exception}')
        # proxy = request.meta['proxy'].split('//')[-1]
        # self.delete_proxy(proxy)
        # print(f'删除无效代理{proxy}')
        # return request





