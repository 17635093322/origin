

# 实战案例：
import requests
import tqdm


url = 'https://www.python.org/ftp/python/3.9.10/python-3.9.10-embed-amd64.zip'

res = requests.get(url, stream=True)  # stream：请求数据分包

# print(res)  # <Response [200]>
# print(res.headers)

# 这是数据大小 --- 'Content-Length': '5293941'

size = int(res.headers['Content-Length'])/1024

with open('forge-1.17.1-37.0.116-installer.jar', 'wb') as f:
    data = res.iter_content(1024)
    # iterable 规划好的数据  total 总大小
    for data in tqdm.tqdm(iterable=data, total=size, desc='正在下载', unit='KB'):
        f.write(data)
