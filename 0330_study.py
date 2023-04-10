#!/usr/bin/env bash
# (命令解释器位置)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   0330_study
  Description :
  Author :    lee
  date：     2023/3/30
-------------------------------------------------
"""

import requests
# async def func(url):    #此时调用func()就变成了协程对象了而非函数调用
#     print(url)
#     await asyncio.sleep(2)      # await 挂起操作一般放在携程对象前面
#     print('111')
#
# async def main():       #async 将函数添加异步
#     list = ['http:ds.com',
#             'http://dsadsii.com',
#             'http://uiorqe.com']
#     task = []
#     for url in list:
#         f = func(url)
#         task.append(asyncio.create_task(f))   #3.8之后只能用这种
#     await asyncio.wait(task)
#
import asyncio
import aiohttp
from aiohttp import TCPConnector
async def func(url):
    name = url.split('=')[-1]+'.jpg'
    print(name)
    async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
        print('session')
        async with session.get(url) as resp:
            print('resp')
            with open(name,mode = 'wb') as f:
                print('f')
                f.write(await resp.content.read())
    print('搞定')

async def main():
    urls = ['https://gimg3.baidu.com/search/src=http%3A%2F%2Fpics4.baidu.com%2Ffeed%2F72f082025aafa40f9cd5860c0719f24479f0195d.jpeg%40f_auto%3Ftoken%3D04c214efbe950dfd24705b401969503c&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=f360,240&n=0&g=0n&q=75&fmt=auto?sec=1680368400&t=ac26023c6a3651842e5a4937499667eb',
            'https://gimg3.baidu.com/search/src=http%3A%2F%2Fpics3.baidu.com%2Ffeed%2Fcc11728b4710b912be52771b6e800d08904522c9.jpeg%40f_auto%3Ftoken%3De45bff04edbcb054bffe597e0e6e7517&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=f360,240&n=0&g=0n&q=75&fmt=auto?sec=1680368400&t=c09217e39e177786531120250a592328',
            'https://gimg3.baidu.com/search/src=http%3A%2F%2Fpics3.baidu.com%2Ffeed%2F9d82d158ccbf6c81567a2e471043403e32fa405d.jpeg%40f_auto%3Ftoken%3D52df31c0e4c37d19af27b08cdebe6276&refer=http%3A%2F%2Fwww.baidu.com&app=2021&size=f360,240&n=0&g=0n&q=75&fmt=auto?sec=1680368400&t=266f1a2ef8a9dff5f0a2ea2620d3508f']
    task = []
    for url in urls:
        f = func(url)
        task.append(asyncio.create_task(f))
    await asyncio.wait(task)



if __name__ == '__main__':
    # asyncio.run(main())

    dicts = {}
    dicts[([1, 2])] = 'abc'
    print(dicts)