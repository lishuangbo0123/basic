import re
import requests
url = "https://m.dytt8.net/index2.htm"
url2 = "https://m.dytt8.net/"
resp = requests.get(url)
resp.encoding = "gb2312"
str = resp.text
# print(str)
pattern = re.compile(r'''<strong>2022新片精品</strong>(?P<content>.*?)</table>''',re.S)
result = pattern.finditer(str)
# print(result)
for it in result:
    content = it.group("content")
    # print(content)
    pattern2 = re.compile(r'''\[<a href="/html/gndy/dyzz/index.html">最新电影下载</a>\]<a href='(?P<url>.*?)'>''',re.S)
    result2 = pattern2.finditer(content)
    for it2 in result2:
        href = it2.group("url")
        resp2 = requests.get(url2+href)
        resp2.encoding = "gb2312"
        print(resp2.text)
