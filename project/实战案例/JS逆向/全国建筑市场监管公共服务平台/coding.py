# -*- coding: utf-8 -*-
import execjs, requests, json, time
from fake_useragent import UserAgent
from jsonpath import jsonpath


class Spider(object):
    def __init__(self):
        ua = UserAgent()
        self.headers = {
            'user-agent': ua.random
        }
        for page_number in range(0, 30):
            print('==' * 60)
            print(f'正在打印{page_number}')
            self.params = {
                'pg': page_number,
                'pgsz': 15,
                'total': 450,
            }
            response = requests.get('http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list', params=self.params, headers=self.headers)
            self.parse(response.text)
            time.sleep(10)

    def parse(self, rep):
        file = open('config_.js', 'r')
        js = execjs.compile(file.read())
        t = rep
        res = js.call('h', t)
        res_json = json.loads(res)
        # print(res)
        for QY_ID, QY_NAME in zip(jsonpath(res_json, '$..QY_ID'), jsonpath(res_json, '$..QY_NAME')):
            print(f'正在打印{QY_NAME}')
            self.get_data_continue(QY_ID)

    def get_data_continue(self, QY_ID):
        ua = UserAgent()
        params = {
            'qyId': QY_ID,
            'pg': self.params['pg'],
            'pgsz': self.params['pgsz'],
        }
        headers = {
            'user-agent': ua.random,
            'accessToken': 'jkFXxgu9TcpocIyCKmJ+tfpxe/45B9dbWMUXhdY7vLX9SezvkbVHECpLfg0iAd2xhpUUKvcMtoMqfGfwdLCb8g==',
        }
        time.sleep(2)
        rep_data = requests.get('http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/caDetailList', headers=headers, params=params)
        file = open('config_.js', 'r')
        js = execjs.compile(file.read())
        t = rep_data.text
        res = js.call('h', t)
        res_dict = json.loads(res)
        # print(res)
        print(jsonpath(res_dict, '$..APT_NAME'))


if __name__ == '__main__':
    a = Spider()

























