# -*- coding: utf-8 -*-
import requests, hashlib, time, base64, execjs
from jsonpath import jsonpath


class Spider(object):
    def __init__(self):
        for page_num in range(0, 10):
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
            }

            t = int(time.time())
            s1 = f'/api/movie,{t}'
            o = hashlib.sha1(s1.encode('utf-8')).hexdigest()
            str_str = str(f"{o},{t}")
            print(str_str)
            bytesStr = str_str.encode(encoding='utf-8')
            b64str = base64.b64encode(bytesStr)  # 最后的base64加密
            b64str = b64str.decode('utf-8')  # 将字节转换为str

            self.params = {
                'limit': 10,
                'offset': 0,
                'token': b64str
            }
            print(b64str)
            rep = requests.get(url='https://spa6.scrape.center/api/movie/', headers=self.headers, params=self.params, timeout=5)
            print(rep.status_code)



if __name__ == '__main__':
    a = Spider()
