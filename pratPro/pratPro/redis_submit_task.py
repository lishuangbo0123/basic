import json
import time

from redis import StrictRedis
from pratPro import settings




def get_param(url,method):
    if '?' in url:
        url_str = url.split('?',1)[0]
        url_end = url.split('?',1)[1]
        key_value_list = url_end.split('&')
        meta_dic = {}
        for item in key_value_list:
            key_str = item.split('=')[0]
            value_str = item.split('=')[1]
            meta_dic[key_str] = value_str
        params = dict(
            url=url_str,
            method=method,
            meta=meta_dic
        )
        return params
    else:
        meta_dic = {}
        params = dict(
            url=url,
            method=method,
            meta=meta_dic
        )
        return params


def submit_redis_url(redis_key,method,url):


    with StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db= settings.REDIS_DB
    ) as redis_client:

        params = get_param(url,method)
        print(f'即将lpush--{json.dumps(params)}')
        redis_client.lpush(redis_key, json.dumps(params))
        redis_client.close()


test = ['1asd','2bfd','3re','4fds','5rew','6rewqq','7dfsxz','8uiy','9das','10gfdr']

# submit_redis_url('ail', 'GET', f'https://www.baidu.com/s?wd=1asd')

for i in range(10):

    submit_redis_url('ail', 'GET', f'https://www.baidu.com/s?wd={test[i]}')

    submit_redis_url('prat', 'GET', f'https://www.sogou.com/web?query={test[i]}')

    submit_redis_url('third_a', 'GET', f'https://www.so.com/s?q={test[i]}')
