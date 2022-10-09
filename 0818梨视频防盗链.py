import requests
import re
from datetime import datetime
re_com = re.compile(r"contId=(?P<cont_id>.*?)&")
url = "https://www.pearvideo.com/videoStatus.jsp?contId=1719574&mrd=0.45130293229554286"
cont_id_list = re_com.findall(url)
cont_id = cont_id_list[0]
# https://video.pearvideo.com/mp4/adshort/20210206/1660836967102-15601109_adpkg-ad_hd.mp4  获取到的数据
# https://video.pearvideo.com/mp4/adshort/20210206/cont-1719574-15601109_adpkg-ad_hd.mp4  需要下载的请求数据
headers = {
    "Referer": "https://www.pearvideo.com/video_1719574"
}
resp = requests.get(url,headers=headers)
dic = resp.json()
download_url_1 = dic["videoInfo"]["videos"]["srcUrl"]
systemTime = dic["systemTime"]
download_url_2 = download_url_1.replace(systemTime,f"cont-{cont_id}")
resp2 = requests.get(download_url_2)

time1 = str(datetime.now())
with open("time1.mp4",mode="wb") as f:
    f.write(resp2.content)

print("over")

