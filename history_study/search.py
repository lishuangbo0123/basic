#!/usr/bin/env bash
# (命令解释器位置)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   search
  Description :
  Author :    lee
  date：     2023/3/30
-------------------------------------------------
"""
__author__ = 'lee'
import os

path = input("请输入要检索的路径:")
keyWord = input("请输入搜索的关键字")

for dirpath, dirnames, filenames in os.walk(path):
    # print("--------------------------------")
    # print(f'当前目录：{dirpath}')
    # print(f"当前目录所有子目录名")
    for dirname in dirnames:
        # print(dirname)
        pass
    # print(f"当前目录所有文件名：")
    for filename in filenames:
        # print(filename)
        if keyWord in filename:
            print(f"所在路径{dirpath} 文件名：{filename}")
    # print("--------------------------------")