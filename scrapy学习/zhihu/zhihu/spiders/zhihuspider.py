import scrapy
from zhihu.items import ZhihuItem

class ZhihuspiderSpider(scrapy.Spider):
#     name = 'zhihuspider'
#     #allowed_domains = ['www.xxx.com']
#     url = "https://www.zhihu.com"
#
#     start_urls = [url]
#     def parse(self, response):
#         # 内容  作者 文章链接 标题
#         div_list = response.xpath('//*[@id="TopstoryContent"]/div/div/div/div')
#         # print(len(div_list))
#         # print(div_list)
#         all_data = []
#         for div in div_list:
#             # xpath返回的是列表，但列表元素一定是Selector类型的对象
#             # extract可以将Selector中data参数存储的字符串提取出来
#             # 列表中调用了extract只有，则表示将列表中每一个Selector对象中data对应的字符串提取出来
#             # extract_first() 如果xpath返回的列表中只有一个列表元素，则可以直接用extract_first
#             title = div.xpath('./div/div/div/h2/div/a[1]/text()').extract()
#             print(title)
# # --------------------基于终端指令的本地数据化存储-----------------------
#             dic = {
#                 "title" : title
#             }
#             all_data.append(dic)
#         return all_data


    name = 'zhihuspider'
    # allowed_domains = ['www.xxx.com']
    url = "https://www.zhihu.com"
    start_urls = [url]
    def parse(self, response):
        # 内容  作者 文章链接 标题
        div_list = response.xpath('//*[@id="TopstoryContent"]/div/div/div/div')
        # print(len(div_list))
        # print(div_list)
        all_data = []
        for div in div_list:
            # xpath返回的是列表，但列表元素一定是Selector类型的对象
            # extract可以将Selector中data参数存储的字符串提取出来
            # 列表中调用了extract只有，则表示将列表中每一个Selector对象中data对应的字符串提取出来
            # extract_first() 如果xpath返回的列表中只有一个列表元素，则可以直接用extract_first
            title = div.xpath('./div/div/div/h2/div/a[1]/text() | ./div/div/div/div/h2/span/a/text() | ./div/div/div/div/h2/div/a[1]/text()').extract()
            print('-----' ,title)
            if len(title) != 0 :
                print(title)
                item = ZhihuItem()
                item['title'] = title[0]
                yield item#将item提交给管道


# //*[@id="TopstoryContent"]/div/div/div/div[13]/div/div/div/div/h2/div/a[1]/text()
# //*[@id="TopstoryContent"]/div/div/div/div[9]/div/div/div/div/h2/span/a/text()
# //*[@id="TopstoryContent"]/div/div/div/div[27]/div/div/div/h2/div/a[1]/text()
# //*[@id="TopstoryContent"]/div/div/div/div[28]/div/div/div/div/h2/span/a/text()



