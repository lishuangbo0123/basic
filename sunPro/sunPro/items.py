# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    number = scrapy.Field()
    link = scrapy.Field()

    def get_mysql_select(self):
        number1 = self['number']
        mysql_text_1 = f"select count(*) from sun where number = '{number1}'"
        print(type(mysql_text_1))
        return mysql_text_1

    def get_mysql_insert(self):

        print(type(mysql_text_4))
        return mysql_text_4

    def get_mysql_update(self):

        print(type(mysql_text_5))
        return mysql_text_5




class DetailItem(scrapy.Item):
    detail_desc = scrapy.Field()
    number = scrapy.Field()

    def get_mysql_select(self):

        return mysql_text_1

    def get_mysql_insert(self):

        return mysql_text_2

    def get_mysql_update(self):

        return mysql_text_3

