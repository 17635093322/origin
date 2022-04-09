# -*- coding: utf-8 -*-
import requests
from jsonpath import jsonpath


class Spider(object):
    def __init__(self):
        for page_num in range(0,10):
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
            }
            self.params = {
                'limit': 10,
                'offset': page_num*10,
            }
            rep = requests.get(url='https://spa3.scrape.center/api/movie/', headers=self.headers, params=self.params)
            print(jsonpath(rep.json(), 'results[*].name'))


if __name__ == '__main__':
    a = Spider()