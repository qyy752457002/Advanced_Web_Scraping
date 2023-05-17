'''

urllib
(1) 一个类型以及六个方法
(2) get请求
(3) post请求 百度翻译
(4) ajax的get请求
(5) ajax的post请求
(6) cookie登陆 微博
(7) 代理

'''

'''

requests
(1) 一个类型以及六个属性
(2) get请求
(3) post请求
(4) 代理
(5) cookie 验证


'''

import requests
import json

def requests_get():

    url = 'https://www.baidu.com/s?'

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
            }

    response = requests.get(url = url, headers = headers)

    content = response.text

    return content

'''
    总结
    (1) 参数使用params传递
    (2) 参数无需urlencode编码
    (3) 不需要请求对象的定制
    (4) 请求资源路径中的 ? 可加可不加

'''

def requests_post():

    url = "https://fanyi.baidu.com/sug"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"

    }

    data = {
        "kw" : "eye"
    }

    response = requests.post(url = url, data = data, headers = headers)

    content = response.text

    # convert json to python dictionary
    return json.loads(content, encoding = "utf-8")

'''
    总结
    (1) post请求 是不需要编码的
    (2) post请求的参数是data
    (3) 不需要请求对象的定制
    (4) 请求资源路径中的 ? 可加可不加

'''

if __name__ == "__main__":

    print(requests_get())

    print(requests_post())
