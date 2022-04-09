import requests
from jsonpath import jsonpath
import math
from openpyxl import workbook
import sys

'''
    课程变动：
    对本周四的授课安排做个调整
    
    下载Todesk
'''

url = 'https://careers.tencent.com/tencentcareer/api/post/Query'
wb = workbook.Workbook()  # 创建Excel表格
ws = wb.active  # 激活当前表
# 向当前表添加标题
ws.append(['职位', '国家', '地区'])

# 发起请求
def get_data():
    try:
        # 构建身份认证信息
        headers = {
            'referer': 'https://careers.tencent.com/search.html',
            'cookie': 'pgv_pvid=5366037975; _ga=GA1.2.506032198.1625809331; _ga_J5ZYJSX9HN=GS1.1.1630290004.1.1.1630290656.0; _gcl_au=1.1.1084362274.1633764141; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2211c2f83f18a364483afb6a1182e79aa2%40devS%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217a89c9a34b3f4-0eccb293e10711-6373264-1382400-17a89c9a34cd3f%22%7D',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        }
        response = requests.get(url, headers=headers, params=data_parameter)
        # 当响应状态码==200的时候开始解析以及保存
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        raise Exception('NO data~')  # 状态码不是200 意味请求不到数据 抛出异常
    except:
        sys.setrecursionlimit(3)  # 设置递归限制
        return get_data()

# 解析数据
def parse_data():
    data = get_data()
    try:
        Counts = jsonpath(data, '$..Count')[0]  # 获取岗位总数量，用于计算翻页数量
        #  math.ceil()作用：向上取整 算出总页数
        page_num = math.ceil(Counts / 10)
        # print(page_num)
        for i in range(1, page_num + 1):
            print('当前正在下载{}页'.format(i))
            # 再次调用请求函数，向每一页url发请求以此得到每一页的响应数据交给jsonpath做解析
            page_data = get_data()
            # 因'pageIndex'参数为翻页参数，所以通过字典的拿键名改键值的方式修改'pageIndex'参数
            data_parameter['pageIndex'] = i
            # 职位
            position = jsonpath(page_data, '$..RecruitPostName')
            # 国家
            country = jsonpath(page_data, '$..CountryName')
            # 地区
            region = jsonpath(page_data, '$..LocationName')
            for positions, countrys, regions in zip(position, country, region):
                print('职位:', positions)
                print('国家:', countrys)
                print('地区:', regions)
                print('===' * 15)
                save_data(positions, countrys, regions)
    except:
        sys.exit(1)

    # 保存数据
def save_data(posi, count, reg):
    my_list = [posi, count, reg]
    ws.append(my_list)
    wb.save('腾讯招聘.xlsx')


if __name__ == '__main__':
    data_parameter = {
        'timestamp': '1636696353856',
        'countryId': '',
        'cityId': '',
        'bgIds': '',
        'productId': '',
        'categoryId': '',
        'parentCategoryId': '',
        'attrId': '',
        'keyword': '',
        'pageIndex': '1',
        'pageSize': '10',
        'language': 'zh-cn',
        'area': 'cn',
    }
    parse_data()
