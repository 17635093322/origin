import requests
from fake_useragent import UserAgent
from lxml import etree
from multiprocessing import Pool
import time

"""
import requests

url = "https://chongqing.anjuke.com/community/p2/?from=esf_list"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
  'Referer': 'https://chongqing.anjuke.com/sale/?from=esf_list',
  'Cookie': 'aQQ_ajkguid=0F33706E-B208-4D57-ABCD-9AAA36C58EBF; ajk-appVersion=; ctid=20; fzq_h=b93d6d66b06fa4d92971793f1e8d0538_1646454945189_8b6873da9eaf46b387ef0d0ae4d541da_2091376076; sessid=1CED8E4F-5E75-4DA0-B8F6-83817A2A1D34'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

"""
class zhufang:
    def __init__(self):
        self.url = 'https://chongqing.anjuke.com/community/p{}/'
        ua = UserAgent()
        self.headers = {
            'user-agent': ua.random,
            'Referer': 'https://chongqing.anjuke.com/sale/?from=esf_list',
            'cookie': 'aQQ_ajkguid=E370FE2F-B6F4-D899-5BBF-SX0305121902; isp=true; id58=CpQDXWIi5LaVZRg5riswAg==; 58tj_uuid=4ba6a8c4-49a7-4556-b0a3-9253ac9743d9; als=0; wmda_uuid=9480da00475d32b9fd7978361d9a866a; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; _ga=GA1.2.1382643901.1646453987; _gid=GA1.2.2130332990.1646453987; fzq_h=bcdfcf416dc3777c08bf0bce829fc30d_1646454010911_1bd8d72dcb9a49e1bec31d879260087f_2091376076; sessid=4D630DDA-D888-B447-4603-SX0306084403; init_refer=https%253A%252F%252Fwww.bing.com%252F; new_uv=4; twe=2; new_session=0; ajk_member_verify=2p0yWqZA1ORruEu9zT7Uwg5e0BkEsemZU0zRtnRF%2BKM%3D; ajk_member_verify2=MjQzODMyMTYzfHAxZjNrYmR8MQ%3D%3D; ajk_member_id=243832163; ajk-appVersion=; ctid=20; fzq_js_anjuke_ershoufang_pc=2540c793ea624408966db8546bffa028_1646529632183_23; fzq_js_anjuke_xiaoqu_pc=6e2786bd68c82b2d920b66fcfe66d511_1646529633736_23; obtain_by=2; ajkAuthTicket=TT=827a2ebd505efa1a9214d0a7942146e6&TS=1646529633975&PBODY=I3GXtWrr5_Y8WnNAms9HOIspzNNINO9YC2vw7VjhxRjmoiJBaUvnhnOkIkdvlBNaPIxCxTVYyiOI5mRck2xvl7JShG6q_jeDzUnyLD3CXjiFWKQ3Y7Ne4WIb63La7gHyQWYoP4xxzcRna1Ey8c15amSI9lr9Z91XbR8kAkuQxb4&VER=2&CUID=K4xFTamMESwUGOxaWqgfXHKyO1Hvr8W-; xxzl_cid=93acff6267ee4ce083751f1ad6b82d54; xzuid=e96eaccc-8d29-44f6-bd4e-f367f520c611'
        }
        self.proxies = {
            'http': 'http://117.32.76.137:4231',
            # 'https': 'https://117.32.76.137:4231'
        }


    def get_page(self, i):
        print(f'正在打印第{i}页')
        rep_page = requests.get(self.url.format(i), headers=self.headers,proxies=self.proxies)
        print(rep_page.status_code)
        xml_page = etree.HTML(rep_page.text)
        page = xml_page.xpath('//div[@class="list-cell"]/a/@href')
        for url in page:
            print(url)
            self.parse_data(url)
            # time.sleep(8)

    def parse_data(self,url):
        page_data = requests.get(url, headers=self.headers,proxies=self.proxies)
        page_xml = etree.HTML(page_data.text)
        title = page_xml.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div/h1/text()')
        message = page_xml.xpath('//*[@id="__layout"]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/div[1]/text()')
        message_title = page_xml.xpath('//*[@id="__layout"]/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/text()')
        print(title[0])
        for mt,m in zip(message_title,message):
            print(mt.strip(),end=':\t')
            print(m.strip())

    # def pool_total(self):
    #     pool = Pool(6)
    #     for num in range(1,50000):
    #         pool.apply_async(func=self.get_page, args=(num,))
    #     pool.close()
    #     pool.join()

if __name__ == '__main__':
    a = zhufang()
    a.get_page(1)
