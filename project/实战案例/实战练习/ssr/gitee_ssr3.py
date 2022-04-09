# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from lxml import etree



class Spider(object):
    def __init__(self):
        for i in range(1, 11):
            ua = UserAgent()
            url = f'https://ssr1.scrape.center/page/{i}'
            headers = {
                'user-agent': ua.random,
            }
            # 解决进入网站前前需要登陆验证的问题（不是网页登陆）
            rep = requests.get(url, headers=headers, auth=('admin', 'admin'))
            # print(rep.status_code)
            # rep = requests.get(url, headers=headers, verify=False)
            rep = etree.HTML(rep.text)
            title = rep.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[2]/a/h2/text()')
            print(title)


if __name__ == '__main__':
    a = Spider()
