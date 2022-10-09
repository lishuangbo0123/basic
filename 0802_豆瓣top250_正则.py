import requests
import re
import csv
url = "https://movie.douban.com/top250"
headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers = headers)
str = resp.text


pattern = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&n.*?<span property="v:best" content="(?P<score>.*?)"></span>.*?<span>(?P<number>.*?)人评价</span>',re.S)
result = pattern.finditer(str)

with open("csv.data","w") as f:
    csvwritter = csv.writer(f)
    for it in result:
        name = it.group("name")
        year = it.group("year").strip()
        score = it.group("score")
        number = it.group("number")
        print(name,year,score,number)
        dic = it.groupdict()
        dic["year"] = year

        csvwritter.writerow(dic.values())