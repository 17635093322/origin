# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from jsonpath import jsonpath


class Spider(object):
    def __init__(self):
        # 浏览器伪装实例化
        ua = UserAgent()
        # 请求头
        self.headers = {
            'user-agent': ua.random,
        }
        # 代理IP
        # self.proxies = {
        #     'http': 'http://',
        #     'https': 'https://'
        # }
        # from data data请求参数
        # self.data = {}
        # requests payload json请求参数
        # self.json = {}
        # url所带参数
        self.params = {
            'id': 4748054353413042,
            'is_show_bulletin': 2,
            'is_mix': 0,
            'count': 10,
            'uid': 1669879400,
        }
        # *args
        # headers=self.headers, params=self.params, proxies=self.proxies, json=self.json, data=self.data
        # get请求
        rep = requests.get('https://weibo.com/ajax/statuses/buildComments', headers=self.headers, params=self.params)
        # post请求
        # rep = requests.post(url)
        # 修改为网页默认的编码格式
        rep.encoding = rep.apparent_encoding
        # 打印响应页源代码
        # print(rep.text)
        # 获取数据
        self.get_data(rep)

    def get_data(self, responses):
        json_data = responses.json()
        texts = jsonpath(json_data, '$..text')
        for text in texts:
            print(text)


if __name__ == '__main__':
    a = Spider()