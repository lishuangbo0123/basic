import requests
from bs4 import BeautifulSoup
import pymysql
import time
import fake_useragent
# 服务器
conn = pymysql.Connect(host='106.13.1.144',port=3306,user='database1',password='admin',database='database1',charset='utf8',ssl={'ssl':{}})
cursor = conn.cursor()
# try:
#     cursor.execute(f'insert into zhihu values({item["title"]})')
#     conn.commit()
#     print('提交数据' + item["title"])
# except Exception as e:
#     print(e)
#     conn.rollback()

# 网络请求
for i in range(1,200):
    url = 'https://www.kuaidaili.com/free/inha/%d/'%i
    UA = fake_useragent.UserAgent()
    headers = {
        'User-Agent': UA.data_randomize
    }
    resp = requests.get(url = url,headers = headers)
    resp.close()
    bs_obj = BeautifulSoup(resp.text,'html.parser')
    resp1 = bs_obj.find('table',class_ = 'table table-bordered table-striped').find('tbody').find_all('tr')
    # print(resp1)
    for tr in resp1:
        ip_address = tr.find('td',attrs={"data-title":"IP"}).text
        ip_port = tr.find('td', attrs={"data-title": "PORT"}).text
        ip_hidden = tr.find('td', attrs={"data-title": "匿名度"}).text
        ip_type = tr.find('td', attrs={"data-title": "类型"}).text
        ip_location = tr.find('td', attrs={"data-title": "位置"}).text
        ip_speed = tr.find('td', attrs={"data-title": "响应速度"}).text
        ip_time = tr.find('td', attrs={"data-title": "最后验证时间"}).text
        # print(url,ip_address,ip_port,ip_hidden,ip_type,ip_location,ip_speed,ip_time)
        ip = ip_address
        port = ip_port
        proxies = {
            'https' : 'https://'+ip+':'+port,
            'http': 'http://' + ip + ':' + port
        }
        url1 = 'https://www.baidu.com/'
        try:
            resp_yz = requests.get(url1, proxies=proxies, timeout=1)
            resp_yz.encoding = 'utf-8'
            print(resp_yz.status_code)
            if resp_yz.status_code == 200:
                print('------------------当前代理可使用:',proxies)
            resp_yz.close()
        except:
            # print('当前代理：',proxies,'请求超时，检测不合格')
            pass
    time.sleep(2)






