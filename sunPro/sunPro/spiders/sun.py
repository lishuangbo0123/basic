import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SunproItem,DetailItem

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=3']
    link = LinkExtractor(allow=r'id=1&page=\d+')
    link_1 = LinkExtractor(allow=r'/political/politics/index\?id=\d+')
    rules = (
        Rule(link, callback='parse_item', follow=True),
        Rule(link_1, callback='parse_detail_item', follow=False),
    )

    def parse_item(self, response):
        sun_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for sun in sun_list:
            item = SunproItem()
            title = sun.xpath('./span[3]/a/text()').extract_first()
            item['title'] = title
            number = sun.xpath('./span[1]/text()').extract_first()
            item['number'] = number
            link = 'https://wz.sun0769.com' + sun.xpath('./span[3]/a/@href').extract_first()
            item['link'] = link
            print(title,number,link)
            yield item

    def parse_detail_item(self,response):
        detail_desc = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        item = DetailItem()
        item['detail_desc'] = detail_desc
        number = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[5]/text()').extract_first().split('：')[-1]
        item['number'] = number
        print(f'detail item data is {detail_desc},{number}')
        yield item