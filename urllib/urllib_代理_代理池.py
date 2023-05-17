import urllib.request
import random

'''
    代理的功能
    1. 突破自身IP访问限制，访问国外站点
    2. 访问一些单位或团体内部资源
    3. 提高访问速度
    4. 隐藏真实IP
'''

url = "https://www.baidu.com/s?wd=ip"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
     }

# 请求对象的定制
request = urllib.request.Request(url = url, headers = headers)

''' 三大关键字: HTTPHandler  build_opener  open'''

# 快代理: https://www.kuaidaili.com/free/
proxies_pool = [

    {'http': '27.42.168.46 : 55481'},
    {'http': '116.9.163.205 : 58080'},
    {'http': '182.34.17.104 : 9999'},

]

''' (1) 获取handler 对象 ''' 
handler = urllib.request.ProxyHandler(proxies= random.choice(proxies_pool))

''' (2) 获取opener对象 ''' 
opener = urllib.request.build_opener(handler)

''' (3) 调用open方法'''
response = opener.open(request)

# 获取响应的信息
content = response.read().decode('utf-8')

# 保存
with open('D:/Python Tutorial/爬虫进阶/urllib/daili.html', 'w', encoding = 'utf-8') as fp:
    fp.write(content)
