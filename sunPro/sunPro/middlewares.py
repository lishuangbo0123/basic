# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import requests
import time
import json
from scrapy.http import Headers
from scrapy.http.response.html import HtmlResponse
url = 'https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1'
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
headers ={
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Language':'zh-CN,zh;q=0.9',
    # 'Accept-Encoding':'gzip, deflate, br',
    # 'Referer': 'https://www.zhipin.com/?ka=pc',
    # 'Cookie': "lastCity=101280600; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1666073105; wd_guid=5abdd3bc-f09b-4008-bdc4-6afbb0e86687; historyState=state; _bl_uid=tFlyg9mndwXs3gxqsj68m0Uhs48q; __zp_seo_uuid__=2227810d-bdef-44a6-af5b-680cb6e3983e; __g=-; __zp_stoken__=0a14edEx1GxF9ch9MJhEUYXAkZH1cfxMzUEwgRko3UwVYZG8Ib396D31hKwc/XFs8E29hWlcJXxhMPGJ0XgsGOwpvbGR2TQ8qUzFxC0pEYw4DXiEcZFhSCHNHIGJ9HH4Pbk51R18MFkAsaxNEWG1mSgsLUAFyFDYPC0MaCw97BQgMG3QyECsiVzFfRxY/JUwGHEQFZGBNDQ==; __l=r=https://www.baidu.com/link?url=BK-CjEX5ofTmyTWCqEdsixOoMs1EsWWqzNO-5h4Vx3Ss26dFn6STiRPcbaaASfi_&wd=&eqid=e5197bd900018d4900000006634e637d&l=/www.zhipin.com/web/geek/job?query=python&city=101280600&page=2&s=3&g=&friend_source=0&s=3&friend_source=0; __c=1666073105; __a=84328899.1666073105..1666073105.27.1.27.27; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1666081815",
}
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

class SunproSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class SunproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def get_http_proxy(self):
        try:
            resp = requests.get("http://127.0.0.1:5010/get/").json()
            return resp
        except:
            time.sleep(1)
            return self.get_http_proxy()
    def delete_proxy(self,proxy):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
    def get_random_proxy_response(self,request):
        proxy = self.get_http_proxy().get("proxy")
        if proxy:
            resp = requests.get(request.url, headers=headers, proxies={"http": f"http://{proxy}"})
            if resp.status_code == 200:
                # resp_text = json.loads(resp.text)
                # if resp_text['code'] == 5002:
                #     self.delete_proxy(proxy)
                #     # print(f'代理访问xxxx失败，删除无效代理{proxy}')
                #     return self.get_random_proxy_response()
                # # print(f'代理访问xxxxx成功{proxy},{resp_text["code"]}')
                # print(f'proxy requests data is {resp.text}')
                return resp
            else:
                # print(f'访问xxxxx失败{html.status_code}，重新获取代理')
                self.delete_proxy(proxy)
                return self.get_random_proxy_response(request.url)
        else:
            print('no proxy ip,please wait 30s')
            time.sleep(30)
            return self.get_random_proxy_response(request.url)
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # print('intercept request')
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # print(type(request.headers))
        # request.headers = Headers()
        # request.headers.setlist("User-Agent",random.choice(USER_AGENTS))
        # request.headers.setlist("Accept-Encoding", 'gzip, deflate')
        # request.headers.setlist("Accept", '*/*')
        # request.headers.setlist("Connection", 'keep-alive')
        # print(request.headers)
        # resp = self.get_random_proxy_response(request)cle
        return None

    def process_response(self, request, response, spider):
        # print('intercept response')
        # print(f'first response is{response.status} and content is {response.text}')
        if 'index/politicsNewest' in request.url:
            resp = self.get_random_proxy_response(request)
            resp = HtmlResponse(url = request.url,encoding='utf-8',body=resp.text)
            print(f'get response data and url is{request.url}')
            return resp
        else:
            resp = self.get_random_proxy_response(request)
            resp = HtmlResponse(url=request.url, encoding='utf-8', body=resp.text)
            print(f'get detail data and url is{request.url}')
            return resp

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
