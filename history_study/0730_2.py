#coding=utf-8
import requests
url = "https://fanyi.baidu.com/sug"
kw = input("请输入单词")
data = {
    "kw" : kw
}
resp = requests.post(url,data=data)
print(resp.json())
