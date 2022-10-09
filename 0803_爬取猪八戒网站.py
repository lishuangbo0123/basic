
from lxml import etree
import requests
import csv
url = "https://shenzhen.zbj.com/wzkf/f.html?fr=newpdy.it.20.8.04&r=1"
resp = requests.get(url)

resp.close()
html = etree.HTML(resp.text)
divs = html.xpath('/html/body/div/div/div/div[3]/div/div[2]/div[4]/div/div')
with open("猪八戒.csv","w") as f:
    csvwriter = csv.writer(f)
    for div in divs:
        price = div.xpath('./div[2]/div[1]/span/text()')[0].strip('￥')
        name = div.xpath('./div[2]/a[1]/text()')[0].strip('')
        local = div.xpath('./div[2]/a[2]/div/div[1]/div[2]/text()')[0].strip()
        com_name = div.xpath('./div[2]/a[2]/div/div[1]/div[1]/text()')[0].strip()
        csvwriter.writerow([price,name,local,com_name])




