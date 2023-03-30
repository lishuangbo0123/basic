#!/usr/bin/env bash
# (命令解释器位置)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   加密
  Description :
  Author :    lee
  date：     2022/10/24
-------------------------------------------------
"""
__author__ = 'lee'

import execjs
import requests
import re

url = 'https://sso.kongzhong.com/ajaxLogin?j=j&jsonp=j&service=https://passport.kongzhong.com/&_=1666689558577'
headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'KZLBS=bea9e7c1e9b0a090; kzu-er=432432; Hm_lvt_1287c2225a527abe3386233dd9316f99=1666689170; Hm_lpvt_1287c2225a527abe3386233dd9316f99=1666689211; SSO-KGZLT=79f35dff-0324-4c60-8d5e-a9d12b81a249; SSO-KGZQRT=F1C30D06CA20EFA7A4BC614DC8692DB0',
    'Host':'sso.kongzhong.com',
    'Referer':'https://passport.kongzhong.com/',
    'sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"macOS"',
    'Sec-Fetch-Dest':'script',
    'Sec-Fetch-Mode':'no-cors',
    'Sec-Fetch-Site':'same-site',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
resp = requests.get(url,headers=headers)
print(resp.text)
dc = re.compile(r'KZLoginHandler.jsonpCallbackKongZ\(\{"dc":"(.*?)","kzmsg":"","service":"https:\/\/passport.kongzhong.com\/","state":"0"\}\)').findall(resp.text)[0]
print(dc)

node = execjs.get()
with open('changkw.js', encoding='utf-8') as f:
    js_code = f.read()
ctx = node.compile(js_code)
# funcName = 'getPwd("{0}","{1}")'.format('123456',dc)
# funcName = f'getPwd("{"123456"}","{dc}")'
funcName = f'getPwd("123456","{dc}")'
pwd = ctx.eval(funcName)
print(pwd)























