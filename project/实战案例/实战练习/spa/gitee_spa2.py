# -*- coding: utf-8 -*-
import requests, execjs, time, hashlib, base64
from jsonpath import jsonpath


class Spider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
        }
        for page_num in range(0,10):
            # 方法一
            file = open('spa2_config.js', 'r')
            js = execjs.compile(file.read())
            token = js.call('params', page_num)
            # 方法二
            # t = int(time.time())
            # s1 = f'/api/movie,{page_num*10},{t}'
            # o = hashlib.sha1(s1.encode('utf-8')).hexdigest()
            # s2 = f'{o},{t}'
            # s3 = s2.encode('utf-8')
            # token = base64.b64encode(s3)
            # token = token.decode()
            self.params = {
                'limit': 10,
                'offset': page_num*10,
                'token': token
            }
            print(token)
            rep = requests.get(url='https://spa2.scrape.center/api/movie/', headers=self.headers, params=self.params, timeout=60)
            print(jsonpath(rep.json(), '$..name'))


if __name__ == '__main__':
    a = Spider()