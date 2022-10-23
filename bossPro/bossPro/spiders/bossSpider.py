# -- coding: utf-8 --
import scrapy
import json
import re
from ..items import BossproItem
import requests
import time
from selenium import webdriver
from lxml import etree
def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))
class BossspiderSpider(scrapy.Spider):
    name = 'bossSpider'
    # allowed_domains = ['www.xxx.com']
    query = "python"
    page = 1
    number = 1
    start_urls = [f'https://www.zhipin.com/wapi/zpgeek/mobile/search/joblist.json?city=101280600&querySource=1&page={page}&city=&query={query}']
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='/Users/lee/PycharmProjects/0729/bossPro/bossPro/spiders/chromedriver')
    def detail_parse(self, response):
        item = response.meta['item']
        resp = response.text
        resp = etree.HTML(resp)
        job_desc = ''
        # job_desc_list = re.compile('<div class="job-sec-text">(?P<job_desc>.*?)</div>',re.S).findall(resp)
        # print(job_desc_list)
        # if job_desc_list[0].find('<br>'):
        #     job_desc = (" ").join(job_desc_list[0].split("<br>"))
        # else:
        #     job_desc = job_desc_list
        # # print(f'job_desc1111111111============{job_desc}')
        desc = resp.xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/div[2]/text()')
        print(desc)
        if len(desc) != 0:
            job_desc = ('').join(desc)
        else:
            print('no get job desc data,apply again get')
        # print(job_desc)

        print(f'this item is {item["company"]}')
        item['job_desc'] = job_desc
        self.number += 1
        print(f'current page is{self.page} and no is {self.number}')
        yield item

    def parse(self, response):
        # print(f'------------------------------------------------{response.text}')
        resp_text = response.text
        resp_text = json.loads(resp_text)

        if resp_text['code'] == 5002:
            print('您的 IP 存在异常访问行为，暂时被禁止访问！')
        else:
            hasMore = resp_text['zpData']['hasMore']
            html = str(resp_text['zpData']['html'])
            # print(html)
            job_name = re.compile(r'<span class="title-text">(?P<job_name>.*?)</span>',re.S).findall(html)
            salary = re.compile(r'<span class="salary">(?P<salary>.*?)</span>',re.S).findall(html)
            company = re.compile(r'<span class="company">(?P<company>.*?)</span>',re.S).findall(html)
            workplace = re.compile(r'<span class="workplace">(?P<workplace>.*?)</span>',re.S).findall(html)
            labels = re.compile(r'<div class="labels">(?P<labels>.*?)</div>',re.S).findall(html)
            hr_name = re.compile(r'<div class="name">(?P<hr_name>.*?)</div>').findall(html)
            detail_url = re.compile(r'<a href="(?P<detail_url>.*?)" ka',re.S).findall(html)
            # print(hr_name)
            for i in range(0,len(job_name)):
                item = BossproItem()
                item['job_name'] = job_name[i]
                item['salary'] = salary[i]
                item['company'] = company[i]
                item['workplace'] = workplace[i]
                label_text = labels[i]
                label_list = re.compile('<span>(?P<labels>.*?)</span>',re.S).findall(label_text)
                item['labels'] = (' ').join(label_list)
                item['hr_name'] = hr_name[i]
                new_url = 'https://www.zhipin.com'+detail_url[i]
                item['detail_url'] = new_url
                # print(item)
                # yield scrapy.Request(new_url,callback=self.detail_parse,meta={'item':item,'dont_redirect': True,'handle_httpstatus_list': [301,302]})
                yield scrapy.Request(new_url, callback=self.detail_parse, meta={'item': item})
            if hasMore :
                #有下一页
                self.page += 1
                next_url = f'https://www.zhipin.com/wapi/zpgeek/mobile/search/joblist.json?city=101280600&querySource=1&page={self.page}&city=&query={self.query}'
                yield scrapy.Request(next_url,callback=self.parse)



    # def start_requests(self):
    #     for pageNum in range(1,10,1):
    #         url = f'https://www.zhipin.com/wapi/zpgeek/mobile/search/joblist.json?city=101280600&querySource=1&page={pageNum}&city=&query={self.query}'
    #         yield scrapy.Request(url=url,callback=self.parse)
