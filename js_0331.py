#!/usr/bin/env bash
# (命令解释器位置)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   js_0331
  Description :
  Author :    lee
  date：     2023/3/31
-------------------------------------------------
"""
__author__ = 'lee'
import execjs   #需要使用execjs模块
import requests
import os
import js

directory_path = os.path.dirname(os.path.abspath(__file__)) #当前文件所在文件夹路径
node = execjs.get()
execjs.compile(js,cwd=f"{directory_path}/node_modules") #这里是配置node_modules，这样才能调用js里的crypto-js

ctx = node.compile(open(file='tielu.js', encoding ='utf-8').read())
sign = ctx.eval(f'get_param()')
print(sign)


url = f'https://ec.minmetals.com.cn/open/homepage/tzggs/by-bz-page'
#接口的请求参数是,此参数在js文件中写死了
# a = {
#     "bz": "01",
#     "xxzy": "",
#     "fbdw": "",
#     "pageIndex": 1,
# }
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Cookie': '__jsluid_s=c81ab624f53ed61718deaf0b3195c622; SUNWAY-ESCM-COOKIE=5d5d561e-32dd-4b38-be0f-ef068afa6769',
    "Referer": "https://ec.minmetals.com.cn/open/home/platform-info/",
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Content-Length':'184',
    'Content-Type':'application/json',
    'Host':'ec.minmetals.com.cn',
    'Origin':'https://ec.minmetals.com.cn',
    'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile':'?',
    'sec-ch-ua-platform':'"macOS"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
}
data = {
    'param':sign
}
resp = requests.post(url,headers=headers,data=data)
print(resp.json())

