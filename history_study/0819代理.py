import time
import requests
params = {
    "api":"202208191944238427",
    "akey":"c2461f846c7db79e",
    "timespan":6,
    "type":3
}
resp_prox = requests.get("http://www.zdopen.com/ShortProxy/GetIP/",params=params)
dic = resp_prox.json()
print(dic)
count = dic["data"]["count"]
prox_list = dic["data"]["proxy_list"]
cishu = 1
for prox_dic in prox_list:
    ip = prox_dic["ip"]
    port = prox_dic["port"]
    prox = {
        "https": f"http://202208191944238427:17799574@{ip}:{port}"
    }

    resp = requests.get("https://www.baidu.com", proxies=prox)
    resp.encoding = "utf-8"
    print(f"第{cishu}次数据是-------{resp.text}")
    cishu += 1
    time.sleep(2)


prox = {
        "https":"http://27.158.193.98:17165"
    }
# proxies = {
#         'http': 'http://202208191944238427:17799574@117.68.193.226:24099',
#         'https': 'http://202208191944238427:17799574@117.68.193.226:24099'}
#
# resp = requests.get("https://www.baidu.com", proxies=proxies)
# resp.encoding = "utf-8"
# print(resp.text)

