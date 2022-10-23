# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

headers ={
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    # 'Referer': 'https://www.zhipin.com/?ka=pc',
    # 'Cookie': "lastCity=101280600; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1666073105; wd_guid=5abdd3bc-f09b-4008-bdc4-6afbb0e86687; historyState=state; _bl_uid=tFlyg9mndwXs3gxqsj68m0Uhs48q; __zp_seo_uuid__=2227810d-bdef-44a6-af5b-680cb6e3983e; __g=-; __zp_stoken__=0a14edEx1GxF9ch9MJhEUYXAkZH1cfxMzUEwgRko3UwVYZG8Ib396D31hKwc/XFs8E29hWlcJXxhMPGJ0XgsGOwpvbGR2TQ8qUzFxC0pEYw4DXiEcZFhSCHNHIGJ9HH4Pbk51R18MFkAsaxNEWG1mSgsLUAFyFDYPC0MaCw97BQgMG3QyECsiVzFfRxY/JUwGHEQFZGBNDQ==; __l=r=https://www.baidu.com/link?url=BK-CjEX5ofTmyTWCqEdsixOoMs1EsWWqzNO-5h4Vx3Ss26dFn6STiRPcbaaASfi_&wd=&eqid=e5197bd900018d4900000006634e637d&l=/www.zhipin.com/web/geek/job?query=python&city=101280600&page=2&s=3&g=&friend_source=0&s=3&friend_source=0; __c=1666073105; __a=84328899.1666073105..1666073105.27.1.27.27; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1666081815",
}
class TestbossproSpiderMiddleware:
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


class TestbossproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

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
