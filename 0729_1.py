# 格式化快捷键
from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)
print(resp.read().decode("utf-8"))
with open('mybaidu.html', mode='w',encoding = 'utf-8') as f:
    f.write(resp.read().decode('utf-8'))
    print("over")