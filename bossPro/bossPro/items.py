# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    salary = scrapy.Field()
    company = scrapy.Field()
    workplace = scrapy.Field()
    labels = scrapy.Field()
    hr_name = scrapy.Field()
    detail_url = scrapy.Field()
    job_desc = scrapy.Field()

