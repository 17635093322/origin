# -*- coding: utf-8 -*-
import requests
from lxml import etree
import pymysql


class WeiJi(object):
    def __init__(self):
        self.url = "https://www.wikidata.org/wiki/Wikidata:Database_reports/List_of_properties/all"
        self.proxies = {
            'http': '127.0.0.1:10809',
            'https': '127.0.0.1:10809'
        }
        self.headers = {
            'authority': 'www.wikidata.org',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
            'cookie': 'WMF-Last-Access=19-Mar-2022; WMF-Last-Access-Global=19-Mar-2022; GeoIP=HK:HCW:Central:22.29:114.15:v4; wikidatawikimwuser-sessionId=bf29c6fcf78b06180770; wikidatawikiwmE-sessionTickLastTickTime=1647652561685; wikidatawikiwmE-sessionTickTickCount=1; wikidatawikiel-sessionId=13f27d67645a82d02b42'
        }
        self.db = pymysql.connect(user='root', password='admin', database='spider', charset='utf8')
        self.cursor = self.db.cursor()

    def get_data(self):
        response = requests.request("GET", self.url, headers=self.headers, proxies=self.proxies)
        self.parse_data(response)

    def parse_data(self, rep):
        xml_text = etree.HTML(rep.text)
        IDs = xml_text.xpath('//tbody/tr/td[1]/a')
        labels = xml_text.xpath('//tbody/tr/td[2]')
        descriptions = xml_text.xpath('//tbody/tr/td[3]')
        aliasess = xml_text.xpath('//tbody/tr/td[4]')
        Data_types = xml_text.xpath('//tbody/tr/td[5]')
        Counts = xml_text.xpath('//tbody/tr/td[6]')
        for P_ID, label, description, aliases, Data_type, count in zip(IDs, labels, descriptions, aliasess, Data_types, Counts):
            self.save(P_ID, label, description, aliases, Data_type, count)

    def save(self, P_ID, label, description, aliases, Data_type, count):
        sql = 'insert into weiji(P_ID,label,description,aliases,Data_type,Counts) values(%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql, [P_ID.text, label.text, description.text, aliases.text, Data_type.text, count.text])
        self.db.commit()
        print(f'{P_ID.text}' + '数据添加完毕')


if __name__ == '__main__':
    a = WeiJi()
    a.get_data()
