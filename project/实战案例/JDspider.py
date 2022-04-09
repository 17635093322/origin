# -*- coding: utf-8 -*-
import requests , emoji
from fake_useragent import UserAgent
from jsonpath import jsonpath


class Spider(object):
    def __init__(self):
        # 浏览器伪装实例化
        ua = UserAgent()
        # 请求头
        self.headers = {
            'user-agent': ua.random,
            'Host': 'club.jd.com',
            'Referer': 'https://item.jd.com/',
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
            # 'callback': 'fetchJSON_comment98',
            'productId': '100032149194',
            'score': '0',
            'sortType': '5',
            'page': 0,
            'pageSize': '10',
            'isShadowSku': '0',
            'rid': '0',
            'fold': '1',
        }
        # *args
        # headers=self.headers, params=self.params, proxies=self.proxies, json=self.json, data=self.data
        # get请求
        for i in range(10):
            print(f'正在请求第{i + 1}页')
            rep = requests.get('https://club.jd.com/comment/productPageComments.action', params=self.params,headers=self.headers)
            # post请求
            # rep = requests.post(url)
            # 修改为网页默认的编码格式
            rep.encoding = rep.apparent_encoding
            # 打印响应页源代码
            # print(rep.text)
            # 获取数据
            self.get_data(rep)
            self.params['page'] = i + 1

    def get_data(self, rep):
        json_data = rep.json()
        titles = jsonpath(json_data, '$..referenceName')
        colors = jsonpath(json_data, '$..productColor')
        times = jsonpath(json_data, '$..creationTime')
        for title, color, time in zip(titles, colors, times):
            print(emoji.emojize(title + '\t' + color + '\t' + time))


if __name__ == '__main__':
    a = Spider()

