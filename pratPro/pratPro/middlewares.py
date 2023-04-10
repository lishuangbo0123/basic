# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time
from scrapy.http import HtmlResponse
import os
import threading
import asyncio
from concurrent.futures import ThreadPoolExecutor #线程池和进程池
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class PratproSpiderMiddleware:
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
        spider.logger.info("Spider opened: %s" % spider.name)


class PratproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    async   def process_request(self, request, spider):
        # request.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
        selenium_url = request.url
        if request.meta:
            selenium_url = selenium_url + '?'
            for k, v in dict(request.meta).items():
                selenium_url = selenium_url + str(k) + '=' + str(v) + '&'
            selenium_url = selenium_url[:-1]

        print(f'middlewares.py  address is  {id(self)}selenium_url ====== {selenium_url}and redis_key ======={spider.redis_key}')
        print("当前进程：", os.getpid(), " 父进程：", os.getppid())
        t = threading.current_thread()
        print('Thread id : %d' % t.ident)
        bro = spider.bro
        bro.get(selenium_url)
        await asyncio.sleep(5)
        # page_text = bro.page_source
        # return HtmlResponse(url=selenium_url, body=page_text, encoding='utf-8', request=request)






    def process_response(self, request, response, spider):

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
        spider.logger.info("Spider opened: %s" % spider.name)
