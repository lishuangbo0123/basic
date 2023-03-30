import json
import requests
from Crypto.Cipher import AES
from base64 import b64encode



data = {"rid":"R_SO_4_1972390361",
            "threadId":"R_SO_4_1972390361",
            "pageNo":"1",
            "pageSize":"20",
            "cursor":"-1",
            "offset":"0",
            "orderType":"1",
            "csrf_token":""}
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "pVRhY85vIPBxX15h"
encSecKey = "ccb111841a59ede4c53e48f364674105ca75c9f605c103a74d810c98632a3d77cc70ac10c4decea2621e22e60161e93ce6012fd6cc56b29cf7626f793faa3d2ed0f0fd85a616990af4a8c28a8283b30376a69c37e6421d4203cecd08cae1876fd01f27cc184ca98c1125858aac3364d11d516d7ffac48543abec4ed91dede515"
def get_encSecKey():
    return encSecKey

def get_enctext():
    d_str = json.dumps(data)
    first = AES_encode(d_str,g)
    second = AES_encode(first,i)
    return second

def str_to16(s):
    pad = 16 - len(s)%16
    s += chr(pad) * pad
    return s

def AES_encode(a,b):
    z = "0102030405060708"
    aes_c = AES.new(key = b.encode("utf-8"),mode = AES.MODE_CBC,IV = z.encode("utf-8"))
    a = str_to16(a)
    result = aes_c.encrypt(a.encode("utf-8"))
    return str(b64encode(result),"utf-8")

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
data_real = {
    "params":get_enctext(),
    "encSecKey":get_encSecKey()
}
resp = requests.post(url,data = data_real)
print(resp.text)
