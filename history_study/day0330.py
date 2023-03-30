#!/usr/bin/env bash
# (命令解释器位置)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   test_0329
  Description :
  Author :    lee
  date：     2023/3/29
-------------------------------------------------
"""
import requests
from lxml import etree

__author__ = 'lee'
url = "https://www.baidu.com/"
resp = requests.get(url)
# print(resp.text)
tree = etree.HTML(resp.text)
# first_name = '-----------'.join(tree.xpath("//*[@id='kw']/parent::*/@id"))
first_name = tree.xpath('//*[contains(name(),"input")]/@type')
first_name = tree.xpath('//input/@type')
print(first_name)





