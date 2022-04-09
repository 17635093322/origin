# -*- coding: utf-8 -*-
import requests, time, math, random
from lxml import etree


class maoyan(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            # 'Referer': 'https://www.maoyan.com/board/4?timeStamp=1648805269260&channelId=40011&index=2&signKey=b6ea666934edf23e41e1e45bd6e6cdac&sVersion=1&webdriver=false',
            'Cookie': '__mta=50093593.1648804601804.1649040901725.1649041241226.55; uuid_n_v=v1; _lxsdk_cuid=17fe4699f75c8-07a2802662fff-9771539-144000-17fe4699f75c8; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1648804602,1648978974,1649039081; uuid=9B639EE0B3C111ECACD4DDCD5E77F45025557C16BDF149EDBB475878A01F73FA; _lxsdk=9B639EE0B3C111ECACD4DDCD5E77F45025557C16BDF149EDBB475878A01F73FA; _csrf=c1ab1c599bfa036220e1ce52ac00545bc60bd123aac5771801aaadc957749408; lt=KB05Fa33U3QzvJrj6EAoCxZAA20AAAAAQREAAG-ynZgXkJ5u_evCkj91VgLQbHmL13EYLUTs8nBsrNELmK-2M1yQkNLTYbU_Dq64mg; lt.sig=vrVDjcLHgTzeAVdcjCYIuflRPaE; uid=2707622511; uid.sig=hoTY5jen0jilhxYtHVDD8ej_zi4; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; __mta=50093593.1648804601804.1649040901725.1649041239666.55; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1649041241; _lxsdk_s=17ff2637de3-7d4-495-8d5%7C%7C130',
            'Host': 'www.maoyan.com'
        }
        self.params = {
            'timeStamp': math.floor(time.time()*1000),
            'channelId': 40011,
            'index': 1,
            'signKey': '2c6e9e706eaba14642b39ec41eccdff0',
            'sVersion': 1,
            'webdriver': 'false',
            'offset': 10,
        }
        rep = requests.get(url='https://www.maoyan.com/board/4', params=self.params, headers=self.headers)
        rep.encoding = rep.apparent_encoding

        print(random.randint(1, 10))
        print(math.floor(time.time()*1000))
        print(rep.text)
        self.parse_data(rep.text)

    def parse_data(self, rep):
        rep_xml = etree.HTML(rep)
        dds = rep_xml.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
        for dd in dds:
            print(dd)


if __name__ == '__main__':
    a = maoyan()