import requests
'''================================1，下方举例：以代码的形式去提取芝麻代理的IP  --前提条件是你的本地局域IP必须在芝麻代理的白名单内================================'''
zhima_api = 'http://http.tiqu.letecs.com/getip3?num=1&type=2&pro=0&city=0&yys=0&port=1&time=' \
            '1&ts=1&ys=0&cs=1&lb=1&sb=0&pb=45&mr=1&regions=&gm=4'
proxie_ip = requests.get(zhima_api).json()['data'][0]
print(proxie_ip)
# 将提取后的IP处理成字典形式 构造完整HTTP代理
proxies = {
    'http': str(proxie_ip['ip']) + ':' + str(proxie_ip['port']),
    'https': str(proxie_ip['ip']) + ':' + str(proxie_ip['port'])
}
print(proxies)

# ======================同上方代码作用一样,只是写法不同===========================
zhima_api = 'http://http.tiqu.letecs.com/getip3?num=1&type=2&pro=0&city=0&yys=0&port=1&time=' \
            '1&ts=1&ys=0&cs=1&lb=1&sb=0&pb=45&mr=1&regions=&gm=4'
proxy_response = requests.get(zhima_api).json()
ip_port = str(proxy_response['data'][0]['ip']) + ':' + str(proxy_response['data'][0]['port'])
proxies = {
    'http': ip_port,
    'https': ip_port,
}
print(proxies)


'''================================2，以下举例：日常使用单个IP================================'''
# proxies = {
#     'http': 'http://49.85.95.63:4226',
#     'https': 'https://49.85.95.63:4226'
# }
# print(proxies)


'''================================3，以下举例：请求网站时做到随机切换IP去请求================================'''
# import random
#
# # 将从芝麻代理提取出的IP:端口构造在列表里
# proxies_list = [
#     '49.65.134.55:4254',
#     '125.87.82.103:4256',
#     '114.103.89.0:4258',
# ]
# proxies = {
#     'http': 'http://'+random.choice(proxies_list),
#     'https': 'https://'+random.choice(proxies_list),
# }
# print("随机取到的的IP为：", proxies)
# 接下来正常写爬虫请求代码，并通过proxies参数挂上代理
# response = requests.get('https://www.baidu.com',proxies=proxies)
# print(response.text)


'''================================4，以下举例：芝麻代理自带的代理使用模板================================'''
# coding=utf-8
# import requests
#
# # 请求地址
# targetUrl = "https://www.baidu.com"
#
# # 代理服务器
# proxyHost = "ip"  # 换上提取出的ip
# proxyPort = "port"  # 换上提取出的ip所对应的端口
#
# # 给代理添加HTTP协议及域名信息
# proxyMeta = "http://%(host)s:%(port)s" % {
#
#     "host": proxyHost,
#     "port": proxyPort,
# }
# print(proxyMeta)
#
# # 模板已构造好的完整代理
# proxies = {
#     "http": proxyMeta,
#     "https": proxyMeta
# }
# # 正常发请求
# resp = requests.get(targetUrl, proxies=proxies)
# print(resp.status_code)
# print(resp.text)
