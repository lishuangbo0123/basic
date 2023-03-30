#!/usr/bin/env bash
# (命令解释器位置)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   youdao_sign
  Description :
  Author :    lee
  date：     2022/10/26
-------------------------------------------------
"""
__author__ = 'lee'
import execjs
import requests
import time

lts = str(int(time.time()*1000))
salt = lts+'4'
query = 'dog'
node = execjs.get()
ctx = node.compile(open(file='youdao.js', encoding ='utf-8').read())
# sign = ctx.eval(f"getSign('123456','{salt}')")
sign = ctx.eval("getSign('{0}','{1}')".format('123456',salt))
print(sign)
data = {
    'i':query,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':salt,
    'sign':sign,
    'lts': lts,
    'bv':'f9f67f3d3eed9d205bcaf899ac4474bd',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_REALTlME',
}
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
"Cookie": "OUTFOX_SEARCH_USER_ID=494191938@10.108.162.133; OUTFOX_SEARCH_USER_ID_NCOO=1962589213.6533651; ___rl__test__cookies=1666774884960",
'Referer':'https://fanyi.youdao.com/',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}
resp = requests.post(url,headers=headers,data=data)
print(resp.json())

