import scrapy

from ..items import ImageProItem


class ImgspiderSpider(scrapy.Spider):
    name = 'imgSpider'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/']

    def parse(self, response):
        # print(response.text)
        img_list = response.xpath('/html/body/div[3]/div[2]/div')
        for img in img_list:
            imgurl = img.xpath('./img/@data-original').extract_first()
            # print(imgurl)
            item = ImageProItem()
            item['imgurl'] = 'http:' + imgurl
            yield item
