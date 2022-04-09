import requests, pymysql, time
from lxml import etree
from fake_useragent import UserAgent



class HowNet(object):
    def __init__(self):
        ua = UserAgent()
        self.data = {
            # 第一页参数是true，改成false
            'IsSearch': 'false',
            'QueryJson': '{"Platform":"","DBCode":"CCND","KuaKuCode":"","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":1,"Items":[{"Title":"主题","Name":"SU","Value":"CEO","Operate":"%=","BlurType":""}],"ChildItems":[]}]}}',
            # 需要更换的参数
            'SearchSql': 'B05771AD1998C261E930AA83A97C744BB18F75DA64C80593E5850E3D561A42AE98F1425EE8BB4DF91EC4F11F6DE1BFFA8A56B40A38082E404C8E191DEFE41197094BCF00F789BD738CB537084833491D51CD656CE50F16EB415EA51DF68E392275F3B67958D70F3E2C4586E878B78C3DADDF8AB31B474CD8E7082297116068ADA26AF6625248A9E752568DAA4C96893CE537B5C3449B07F23C137C1B288C342C21B59C4C06A77C3D066C201C80A311875400323944C3CCC831EE646CA0BDAB92D8F516EB1CEB22D4172BEF7878482941F34DA047247D7AE6B92A72E25DF573D9CEA6CF945DE366949341FD7B178FD5E6800AB8EDAE806EE9C208CCC219ABF8B67839F826AEAD968C0B5610135DAEE85A2398D550B8EF0190C6EF6015EED53E621EDC74CFF605F88F3F22E30451A77AD7055D3FF85BA0E95C213C226A9D5F60105068EDF5F047E17048EDBC3D15663DA1F87D92CE62499BCC5FD955DC99D13865100E42E3069630BB54C65C2A2A163DCAA48AE26C2C9BB3040FD6C290676C7D9C2A741EE495AB281FDBE2BC375F88A0A52EDF5DDD38E0517D2472CF08DF12CDF52009178EC209C0B2D90A125D0FA10BFB27DECD25D6C7D103B260D755A2BAED2EBC50A2F1C0EC75734B62539800575C0FA7BBC147B0643704F4D139D94DF1C18FDF9FA2BE97BC8D40606FDCA210CD0F387635716C67C4B549D7F6759DA2DFA59DE6C62DE4306347E062E0D3DCA7CA6251E31E8F20B2DCECF1E89C23ED054A5900',
            'PageName': 'Defaultresult',
            'HandlerId': '0',
            'DBCode': 'CCND',
            'KuaKuCodes': '',
            # 翻页参数
            'CurPage': '1',
            'RecordsCntPerPage': '50',
            'CurDisplayMode': 'listmode',
            'CurrSortField': 'RELEVANT',
            'CurrSortFieldType': 'desc',
            'IsSortSearch': 'false',
            'IsSentenceSearch': 'false',
            'Subject': '',
        }
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': ua.random,
            'Origin': 'https://kns.cnki.net',
            'Referer': 'https://kns.cnki.net/kns8/defaultresult/index',
            'Cookie': 'Ecp_ClientId=1220304113901847233; Ecp_loginuserbk=dx0876; cnkiUserKey=5b38ab12-1160-6a2c-d27f-71d14e9a1447; knsLeftGroupSelectItem=1%3B2%3B; Ecp_ClientIp=124.167.221.204; Hm_lvt_6e967eb120601ea41b9d312166416aa6=1646366093; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217f5310f08c287-0b7657ca9f6dea-a3e3164-1327104-17f5310f08d459%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217f5310f08c287-0b7657ca9f6dea-a3e3164-1327104-17f5310f08d459%22%7D; Ecp_loginuserjf=zq1255934192@gmail.com; yeswholedownload=%3Bwjhx202102015; Ecp_Userid=1089240840; dperpage=50; Ecp_showrealname=1; dsorder=relevant; _pk_ref=%5B%22%22%2C%22%22%2C1646724161%2C%22https%3A%2F%2Fcn.bing.com%2F%22%5D; _pk_ses=*; Ecp_session=1; ASP.NET_SessionId=hixq3vrsjsg0qsmgr4wcdaz3; SID_kns8=123106; CurrSortField=%e7%9b%b8%e5%85%b3%e5%ba%a6%2frelevant%2c(%e5%8f%91%e8%a1%a8%e6%97%b6%e9%97%b4%2c%27time%27); CurrSortFieldType=DESC; LID=WEEvREcwSlJHSldSdmVqMVc3NWZPZU05SVVSVEtWTC9Ka29rMU92QlZqVT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; dblang=ch; _pk_id=5f8b1dd0-01e9-42d3-ad94-4119a4ce71e4.1646365148.16.1646727005.1646724161.; Ecp_LoginStuts={"IsAutoLogin":true,"UserName":"dx0876","ShowName":"%E4%B8%AD%E5%8C%97%E5%A4%A7%E5%AD%A6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"FjmdUG"}; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVqMVc3NWZPZU05SVVSVEtWTC9Ka29rMU92QlZqVT0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=03%2f08%2f2022%2016%3a30%3a42; c_m_expire=2022-03-08%2016%3a30%3a42'
        }
        self.proxies = {
            'http': 'http://125.105.30.147:4245'
        }
        self.db = pymysql.connect(
            user='root', password='admin', database='spider', charset='utf8'
        )
        self.cursor = self.db.cursor()

    def get_data(self):
        i = 1
        while True:
            print(f'正在打印第{i}页')
            self.data['CurPage'] = i
            try:
                rep = requests.post("https://kns.cnki.net/KNS8/Brief/GetGridTableHtml", headers=self.headers, data=self.data, proxies=self.proxies)
                # print(rep.text)
                rep = etree.HTML(requests.post("https://kns.cnki.net/KNS8/Brief/GetGridTableHtml", headers=self.headers, data=self.data, proxies=self.proxies).text)
                res_kanwu = rep.xpath('//td[@class="source"]/a')
                print(res_kanwu)
                res_title = rep.xpath('//td[@class="name"]/a')
                print(res_title)
                res_date = rep.xpath('//td[@class ="date"]')
                print(res_date)
                res_link = rep.xpath('//td[@class ="operat"]/a[1]/@href')
                # print(res_link)
                i += 1
                for r_ka, r_ti, r_da, r_li in zip(res_kanwu, res_title, res_date, res_link):
                    print(r_ka.xpath('string(.)').strip())
                    title_kan = r_ka.xpath('string(.)').strip()
                    print(r_ti.xpath('string(.)').strip())
                    title = r_ti.xpath('string(.)').strip()
                    print(r_da.xpath('string(.)').strip())
                    title_time = r_da.xpath('string(.)').strip()
                    print('https://kns.cnki.net' + r_li)
                    title_url = 'https://kns.cnki.net' + r_li
                    print('==' * 60)
                    # self.save(title_kan, title, title_time, title_url)
            except Exception:
                print('数据加载完毕')
                break


    def save(self, title_kan, title, title_time, title_url):
        sql = 'insert into HowNet_data(title_kan, title, title_time, title_url) values(%s,%s,%s,%s)'
        self.cursor.execute(sql, [title_kan, title, title_time, title_url])
        self.db.commit()


if __name__ == '__main__':
    HN = HowNet()
    HN.get_data()