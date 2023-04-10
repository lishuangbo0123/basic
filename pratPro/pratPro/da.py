# from scrapy import cmdline
#
# cmdline.execute('scrapy runspider ail.py'.split())
# cmdline.execute('scrapy runspider prat.py'.split())
# cmdline.execute('scrapy runspider third_a.py'.split())

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

#根据项目配置获取CrawlerProcess实例
process = CrawlerProcess(get_project_settings())

#添加需要执行的爬虫

process.crawl('prat')

#运行
process.start()
