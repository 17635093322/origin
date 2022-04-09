# -*- coding: utf-8 -*-
import requests, time, math, random, hashlib
from jsonpath import jsonpath


class YouDao(object):
    def __init__(self):
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1503896094.9209864; OUTFOX_SEARCH_USER_ID="-1938012796@10.105.137.202"; _ga=GA1.2.166450095.1647220778; P_INFO=17635093322|1647220933|1|youdaonote|00&99|null&null&null#shx&140600#10#0|&0||17635093322; _ntes_nnid=638bf226e56a4389a52d801b7f4b0fa8,1647431180930; hb_MA-AF8F-B2A48FFDAF15_source=cn.bing.com; _gid=GA1.2.1442215172.1648987332; JSESSIONID=aaaeQ8WJ_k4Pr97epuZ-x; fanyi-ad-id=305426; fanyi-ad-closed=0; ___rl__test__cookies=1649054756979',
            'Referer': 'https://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
        }
        self.data = {
            'i': '小猫',
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': f'{math.floor(time.time())}{random.randint(1,10)}',
            'sign': '',
            'lts': math.floor(time.time()),
            'bv': '70f10884355e7360fdfde6199e8b5094',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }

        """
        sign: n.md5("fanyideskweb" + 输入的数据 + salt + "Ygy_4c=r#e#4EX^NUGUc5")
        """
        self.data['i'] = input('请输入你想搜索的词语：')
        self.data['sign'] = f"fanyideskweb{self.data['i']}{self.data['salt']}Ygy_4c=r#e#4EX^NUGUc5"
        md5 = hashlib.md5()
        md5.update(self.data['sign'].encode())
        self.data['sign'] = md5.hexdigest()
        rep = requests.post(self.url, headers=self.headers, data=self.data)
        self.run(rep)

    def run(self, rep):
        print(jsonpath(rep.json(), '$..tgt')[0])





if __name__ == '__main__':
    a = YouDao()

























