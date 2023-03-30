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
import lxml

__author__ = 'lee'
url = "https://haikou.zbj.com/sem/index?pmcode=137535804&utm_source=bdpz&utm_medium=SEM"
resp = requests.get(url)
print(resp.text)




