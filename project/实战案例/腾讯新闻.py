'''
1，什么是同步加载？
    同步模式，又称阻塞模式，会阻止浏览器的后续处理，停止了后续的解析，因此停止了后续的文件加载（如图像）,渲染,代码执行。
2，什么是异步加载？
    异步加载又称非阻塞，浏览器在下载执行Js同时，还会继续进行后续页面的处理

3，网页数据返回的方式：
    -- 直接返回网页文本  html
    -- ajax加载  -- JSON
    -- JavaScript渲染  -- JSON

4，我们去抓取网站，大致分为两种类别：
    -- 直接返回网页文本
    -- 通过接口（数据包）返回数据的  -- JSON

5，同步加载和异步加载的区分：观察刷新按钮有没有动
    动了-- 同步
    未动-- 异步
'''
import requests
from jsonpath import jsonpath  # pip install jsonpath
import sys
from openpyxl import workbook # pip install openpyxl
from fake_useragent import UserAgent
'''
1，基于速度的反爬  -- 》 放慢速度
2，基于headers的反爬    --》不断的切换UA
3，基于IP的反爬
'''
ua = UserAgent()
p = {
    'http': 'http://115.209.78.10:4256',
    'https': 'https://115.209.78.10:4256'
}
# 发起请求
def get_data(url):
    try:
        # headers = {
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        # }
        headers = {
            'user-agent': ua.random
        }
        # print(headers)
        response = requests.get(url, headers=headers,params=data,proxies=p)
        if response.status_code == 200:
            return response.json()
        raise Exception('NO data~')
    except:
        sys.setrecursionlimit(5)  # 设置限制
        return get_data(url)  # 1000

# 解析数据
def parse_data(data):
    try:
        # $表示根节点 ..跳过任意层级
        title = jsonpath(data, '$..title')  # 标题
        urls = jsonpath(data, '$..url')  # 详情链接
        media_names = jsonpath(data, '$..media_name')  # 媒体  Flase
        for titles, links, media_name in zip(title, urls, media_names):
            print(titles)
            print(links)
            print(media_name)
            print('==' * 20)
            save_data(titles, links, media_name)
    except:
        sys.exit(1) # 终止程序 0为正常退出 （1-127）为不正常退出

# 保存为Excel
def save_data(tit,link,name):
    my_list = [tit,link,name]  # 以列表形式写入数据
    ws.append(my_list)
    wb.save('腾讯.xlsx')  # 保存

if __name__ == '__main__':  # 程序入口
    wb = workbook.Workbook()  # 创建Excel对象
    ws = wb.active  # 激活表对象
    ws.append(['标题', '链接', '媒体'])
    for i in range(0,182,20):
        page_url = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list'
        print('正在下载当前页的URL为：{}'.format(page_url))
        # 构架get参数在字典里
        data = {
            'sub_srv_id': '24hours',
            'srv_id': 'pc',
            'offset': '{}'.format(i),  # 翻页参数 0,20,40....180
            'limit': '20',  # 一页有多少条新闻
            'strategy': '1',
            'ext': '{"pool":["top"],"is_filter":7,"check_type":true}',
        }
        json_data = get_data(page_url)
        # print(json_data)
        parse_data(json_data)
