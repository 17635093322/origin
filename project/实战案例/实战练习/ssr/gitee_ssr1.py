# -*- coding: utf-8 -*-
# https://scrape.center/
import requests
from lxml import etree


class SSR1(object):
    def __init__(self):
        for i in range(1,11):
            self.url = f'https://ssr1.scrape.center/page/{i}'
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
            }
            rep = requests.get(self.url, headers=self.headers)
            rep = etree.HTML(rep.text)
            title = rep.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[2]/a/h2/text()')
            print(title)


if __name__ == '__main__':
    a = SSR1()
