import requests
url = "https://passport.17k.com/ck/user/login"
data = {
    "loginName": "15005010623",
    "password": "a00000000"
}
session = requests.session()
resp = session.post(url,data = data)
# print(resp.text)
# print(resp.cookies)
url1 = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'
resp1 = session.get(url1)
# print(resp1.json())

resp2 = requests.get(url1,headers={"Cookie":"GUID=48375e5d-de69-4f5a-971d-4ace28cd6dca; c_channel=0; c_csc=web; BAIDU_SSP_lcr=https://www.baidu.com/link?url=iD88bhwRWh5wqJPUYf1f42sqMZJ0adEyQ8j4VkYp8wa&wd=&eqid=c3a021b300109a070000000662fddb74; Hm_lvt_9793f42b498361373512340937deb2a0=1659523188,1660803960; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F17%252F17%252F04%252F87210417.jpg-88x88%253Fv%253D1640233995000%26id%3D87210417%26nickname%3Dlllllll12345%26e%3D1676356284%26s%3D872e1ec5a0501dc9; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2287210417%22%2C%22%24device_id%22%3A%22182634a44aa128d-0bdb9dc8ecdce6-1c525635-2073600-182634a44ab1889%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2248375e5d-de69-4f5a-971d-4ace28cd6dca%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1660804679"})
print(resp2.json())