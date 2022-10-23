import scrapy


class TestbossSpider(scrapy.Spider):
    name = 'testBoss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/wapi/zpgeek/mobile/search/joblist.json?city=101280600&querySource=1&page=4&city=&query=']
    custom_settings ={
        "DEFAULT_REQUEST_HEADERS" : {
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'Accept-Encoding': 'gzip, deflate, br',
            # 'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
            }
    }
    def parse(self, response):
        print(response.text)
