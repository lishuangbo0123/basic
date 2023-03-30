# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   log.py
  Description :
  Author :    lee
  date：     2022/10/23
-------------------------------------------------
  Change Activity:
   2022/10/23:
-------------------------------------------------
"""
__author__ = 'lee'
import logging
class Log():
    def __init__(self,level='DEBUG'):
        #日志器对象
        self.log = logging.getLogger(__file__.__name__)
        self.log.setLevel(level)
    def console_handler(self,level='DEBUG'):
        #控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        #处理器添加格式器
        formatter = console_handler.setFormatter(self.get_formatter()[0])
        return console_handler
    def file_handler(self,level='DEBUG'):
        file_handler = logging.FileHandler('./log.txt',encoding = 'utf-8',mode = 'a')
        file_handler.setLevel(level)
        #处理器添加格式器
        file_handler.setFormatter(self.get_formatter()[1])
        return file_handler

    def getformatter(self):
        #格式器
        #定义输出格式
        console_fmt = logging.Formatter(fmt = "%(name)s----->%(message)s----->%(asctime)s")
        file_fmt = logging.Formatter(fmt = "%(name)s----->%(message)s----->%(asctime)s")
        return console_fmt,file_fmt
    def get_log(self):
        #日志器添加控制台处理器
        self.log.addHandler(self.console_handler())
        #日志器添加文件处理器
        self.log.addHandler(self.file_handler())
        return self.log