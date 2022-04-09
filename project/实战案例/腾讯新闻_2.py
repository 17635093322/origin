import requests
from jsonpath import jsonpath
import sys
import time
import math
from openpyxl import workbook

wb = workbook.Workbook()  # 创建Excel表格
ws = wb.active  # 激活当前表
# 向当前表添加标题
ws.append(['职位', '国家', '地区', '职业内容', '发布日期', '详情链接'])


# 目标站点: https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1636683736379&countryId=&cityId=&bgIds=&productId=&categoryId=40001001,40001002,40001003,40001004,40001005,40001006&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn
# 抓取该站点内的招聘信息


# 发起请求
def initiate_request():
    try:
        # 构建身份认证信息
        headers = {
            # 'referer': 'https://careers.tencent.com/search.html',
            'cookie': 'pgv_pvid=5366037975; _ga=GA1.2.506032198.1625809331; _ga_J5ZYJSX9HN=GS1.1.1630290004.1.1.1630290656.0; _gcl_au=1.1.1084362274.1633764141; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211c2f83f18a364483afb6a1182e79aa2%40devS%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217a89c9a34b3f4-0eccb293e10711-6373264-1382400-17a89c9a34cd3f%22%7D',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        }
        response = requests.get(url, headers=headers, params=data)
        # 当响应状态码==200的时候开始解析以及保存
        if response.status_code == 200:
            json_data = response.json()
            return json_data
    except:
        return initiate_request()


# 解析数据
def parse_data():
    # 通过调用发起请求函数 接收返回值json_data
    obtain_func = initiate_request()
    print(obtain_func)
    # jsonpath只解析dict数据
    # 职位
    position = jsonpath(obtain_func, '$..RecruitPostName')
    # 国家
    country = jsonpath(obtain_func, '$..CountryName')
    # 地区
    region = jsonpath(obtain_func, '$..LocationName')
    # 职业内容
    occupation = jsonpath(obtain_func, '$..Responsibility')
    # 发布日期
    release = jsonpath(obtain_func, '$..LastUpdateTime')
    # 详情链接
    link = jsonpath(obtain_func, '$..PostURL')
    for position, country, region, occupation, release, link in zip(position, country, region, occupation, release,
                                                                    link):
        print('===================正在保存岗位信息: ===================')
        print('职位:', position)
        print('国家:', country)
        print('地区:', region)
        print('发布日期:', occupation)
        print('负责内容:', release)
        print('详情链接:', link)
        print('===================岗位信息保存完成!=================== \n')
        save_data(position, country, region, occupation, release, link)


# 保存数据
def save_data(position, country, region, occupation, release, link):
    # 向表格里添加数据
    mylist = [position, country, region, occupation, release, link]
    ws.append(mylist)
    # 保存到表格wb
    wb.save('腾讯招聘.xlsx')


# 运行体
if __name__ == '__main__':
    # data = math.ceil(3796/10)
    for i in range(20):
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query'
        print('============================正在进行翻页操作, 现在是第{}页============================\n'.format(i + 1))

        data = {
            'timestamp': '1636696353856',
            'countryId': '',
            'cityId': '',
            'bgIds': '',
            'productId': '',
            'categoryId': '',
            'parentCategoryId': '',
            'attrId': '',
            'keyword': '',
            'pageIndex': '{}'.format(i + 1),
            'pageSize': '10',
            'language': 'zh-cn',
            'area': 'cn',
        }
        parse_data()
    print('============================数据已经保存完毕============================')
    print('============================数据已经保存完毕============================')

