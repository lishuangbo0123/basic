import requests
query = input("请输入明星")
url = f"https://www.sogou.com/web?query={query}"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
resp = requests.get(url,headers = headers)
print(resp.text)