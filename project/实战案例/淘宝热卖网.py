import json, time, re, hashlib
from requests_html import HTMLSession
from fake_useragent import UserAgent
from urllib.parse import quote



"""
if (d.H5Request === !0) {
    var f = "//" + (d.prefix ? d.prefix + "." : "") + (d.subDomain ? d.subDomain + "." : "") + d.mainDomain + "/h5/" + c.api.toLowerCase() + "/" + c.v.toLowerCase() + "/"
      , g = c.appKey || ("waptest" === d.subDomain ? "4272" : "12574478")
      , i = (new Date).getTime()
      , j = h(d.token + "&" + i + "&" + g + "&" + c.data)
      , k = {
        jsv: w,
        appKey: g,
        t: i,
        sign: j
    }
      , l = {
        data: c.data,
        ua: c.ua
    }
"""


class TaoBaoSpider(object):
    def __init__(self):
        # 准备
        ua = UserAgent()
        self.session = HTMLSession()
        # 需要更改的参数
        self.cookie = 't=abf2fdf8377714de91b1c485447112a6; cna=QE2vGp/PH0sCAXyn3cyPgjJ3; xlly_s=1; sgcookie=E1006YpxHPWQ06s%2B7G9DDw%2BCgzzuQvpN1fyV72%2F6LLoy0PfqZvjtTC%2FNFeaXIGOChfqRR9z2tZ9PHercic93WFAnvboqg4TZQlsuz%2BzVUn3oKmLMxw4a8rJyJLONP5mOBlMh; uc3=vt3=F8dCvUFlpq0S%2BfjDTXU%3D&id2=UUphzW5e%2BAhDAsL85Q%3D%3D&nk2=F5RHpxdtWCuIscQ%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; lgc=tb263353456; uc4=id4=0%40U2grFnGfyiy6gJPi22tS82iF4Q%2Fri72X&nk4=0%40FY4MtaiHnveHQvT3sVw4ToFWopauhg%3D%3D; tracknick=tb263353456; _cc_=URm48syIZQ%3D%3D; enc=YX63KJKKk%2F2uEKipvWd9cSieonQJ7sYQnwXmcg%2BGO76DcTLxIhtxl6SheOUVg1AkcLlOZvLE0Qk6%2BDiEtmjIJwVBhhTXJt4IWVG%2F59hvYjU%3D; _m_h5_tk=aa00791ed8863a22ca406d24470dad75_1646877755428; _m_h5_tk_enc=3c5764114831c4985cfb083be9415ace; mt=ci=-1_0; cookie2=12a582b67066aeeaab7eaa28c030a85f; _tb_token_=e3a03ed3ee8e5; thw=cn; uc1=cookie14=UoewBjJeeMHMVQ%3D%3D; l=eBg5fzhmLENkAezNBOfZlurza77OSIRvhuPzaNbMiOCP9MCp5fk5W6msduT9C3GVhsHHR3lrOrBaBeYBqn4jPGKnNSVsr4Dmn; tfstk=cLhRB9cMUnxoSj4x7YpmA2_94_YcZK_8xaZd9E4AgeDNxo5diwci6G3HFyra2EC..; isg=BPLyKJB7xCRsH_gRDU92byDcQzjUg_YdU4y1OLzLHqWQT5JJpBNGLfipP-tzVW61'
        # 请输入要查询的商品名称
        self.user_input = str(input('请输入你要查询的商品：'))
        # 请输入要的页数量
        self.user_page = int(input('请输入要的页数量:'))
        # 请求url
        self.url = 'https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/'
        # 请求头
        self.headers = {
            'user-agent': ua.random,
            'cookie': self.cookie,
            'referer': 'https://uland.taobao.com/'
        }

    def parse_start_url(self):
        # 获取当前时间戳
        time_temp = str(int(time.time()*1000))
        for page in range(self.user_page):
            print(f'正在加载第{page+1}页')
            data_dict = {"pNum":page,"pSize":"60","refpid":"mm_26632258_3504122_32538762","variableMap":"{\"q\":\"" + self.user_input +"\",\"navigator\":false,\"clk1\":\"201d2a18a9233e40110ded2fd7c89efa\",\"recoveryId\":\"201_33.63.157.64_20201524_1646814266174\"}","qieId":"36308","spm":"a2e0b.20350158.31919782","app_pvid":"201_33.63.157.64_20201524_1646814266174","ctm":"spm-url:;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26clk1%3D201d2a18a9233e40110ded2fd7c89efa%26keyword%3D%25E5%25A5%25B3%25E7%2594%259F%25E7%25A4%25BC%25E7%2589%25A9%26page%3D0"}
            data = quote(str(data_dict))
            params = f'?jsv=2.5.1&appKey=12574478&t={time_temp}&sign={self.parse_sign(time_temp, data_dict)}&api=mtop.alimama.union.xt.en.api.entry&v=1.0&AntiCreep=true&timeout=20000&AntiFlood=true&data='
            page_url = self.url + params + data
            rep = self.session.get(page_url, headers=self.headers).json()["data"]["recommend"]['resultList']
            self.parse_data(rep)


    def parse_sign(self, time_temp, data_dict):
        token = str(re.findall('_m_h5_tk=(.*?)_', self.cookie)[0])
        res = token + "&" + time_temp + "&" + "12574478" + "&" + str(data_dict)
        sign = hashlib.md5(res.encode()).hexdigest()
        return sign

    def parse_data(self, data):
        for res in data:
            shop_name = res['itemName']
            # 店铺的名称
            shop_title = res['shopTitle']
            # 发货地址
            provcity = res['provcity']
            # 详情页地址
            info_url = res['url']
            # 最低价格
            promotionPrice = res['promotionPrice']
            # 最高价格
            price = res['price']
            # 月销量
            monthSellCountFuzzyString = res['monthSellCountFuzzyString']
            req = {
                'user_requests': [shop_title, shop_name, provcity, promotionPrice, price, monthSellCountFuzzyString, info_url]
            }
            print(req['user_requests'])

if __name__ == '__main__':
    a = TaoBaoSpider()
    a.parse_start_url()

