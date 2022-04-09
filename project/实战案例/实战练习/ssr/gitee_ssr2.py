# -*- coding: utf-8 -*-
import ssl, requests
from fake_useragent import UserAgent
from lxml import etree
from urllib.request import Request, urlopen

for i in range(1, 11):
    ua = UserAgent()
    url = f'https://ssr1.scrape.center/page/{i}'
    headers = {
        'user-agent': ua.random,
    }

    # context = ssl._create_unverified_context()
    # request = Request(url, headers=headers)
    # response = urlopen(request, context=context)
    # info = response.read().decode()
    # print(info)
    # 关闭证书验证
    rep = requests.get(url, headers=headers, verify=False)
    rep = etree.HTML(rep.text)
    title = rep.xpath('//*[@id="index"]/div[1]/div[1]/div/div/div/div[2]/a/h2/text()')
    print(title)
