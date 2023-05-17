# 不能定制请求头
''' urllib.request.urlopen(url / Request) '''

# 可以定制请求头
''' urllib.request.Request(url, headers, data) '''

# IMPORTANT: 定制更高级的请求头，用来处理每次登录后cookie不一样(动态cookie)的情况, 以及设置代理
''' Handler '''

import urllib.request
import urllib.parse

# 请求路径
url = 'https://fanyi.baidu.com/sug'

# 请求头
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }

request = urllib.request.Request(url = url, headers = headers)

''' 三大关键字: HTTPHandler  build_opener  open'''

''' (1) 获取handler 对象 ''' 
handler = urllib.request.HTTPHandler()

''' (2) 获取opener对象 ''' 
opener = urllib.request.build_opener(handler)

''' (3) 调用open方法'''
response = opener.open(request)

content = response.read().decode('utf-8')


