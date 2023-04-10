import scrapy
from scrapy_redis.spiders import RedisSpider

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pratPro.webdriver_start_parmas import get_driver

class PratSpider(RedisSpider):
    name = "prat"
    redis_key = 'prat'
    # allowed_domains = ["dsadsa.com"]
    # start_urls = ["http://dsadsa.com/"]

    def __init__(self):
        self.bro = get_driver()

    def parse(self, response,**kwargs):
        print(self.redis_key + '===============================')

        yield {"prat":{"c": 3,'d': 4 }}