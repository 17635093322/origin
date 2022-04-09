import requests
from fake_useragent import UserAgent
from jsonpath import jsonpath
from openpyxl import workbook


ua = UserAgent()
headers = {
    'user-agent': ua.random
}
url = 'https://cms-api.csdn.net/v1/web_home/select_content?componentIds=www-recomend-community'
rep = requests.get(url, headers=headers)
res = rep.json()
re_data = jsonpath(res, '$..url')
print(re_data)
wb = workbook.Workbook()
ws = wb.active
ws.append(['标头'])
for i in range(1, len(re_data)):

    ws.append([re_data[i]])
    wb.save('CSDN首页.xlsx')

