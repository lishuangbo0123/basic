from bs4 import BeautifulSoup
import requests
import csv
headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
url = "https://movie.douban.com/top250"
resp = requests.get(url,headers = headers)
# print(resp.text)
content = BeautifulSoup(resp.text,"html.parser")
list1 = content.find("ol",class_="grid_view")
list = list1.find_all("li")
with open("top250.csv", "w") as f:

    for i in list:

        title = i.find_all("span",class_ = "title")[0].text
        print(title)
        year = i.find_all("div",class_ = "bd")[0].find_all('p')[0].text
        print(year)
        score = i.find_all("div",class_ = "bd")[0].find_all("span",class_= "rating_num")[0].text
        print(score)
        number= i.find("div",class_ = "bd").find_all("div",class_="star")[0].find_all("span")[3].text[:-3]
        print(number)
        csvwritter = csv.writer(f)
        csvwritter.writerow([title,year,score,number])





