import urllib.request
import urllib.parse

''' 汉字转换成unicode编码 '''
def Urllib_Quote():

    url = "https://www.baidu.com/s?wd="

    # 请求对象的定制是为了解决反爬的第一种手段

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    ''' 
    将周杰伦三个字变成unicode编码的格式
    依赖urllib.parse  
    '''
    name = urllib.parse.quote('周杰伦')

    url += name

    # 请求对象的定制
    request = urllib.request.Request(url = url, headers = headers)

    # 模拟向浏览器发送请求
    response = urllib.request.urlopen(request)

    # 获取响应的内容
    content = response.read().decode("utf-8")

    return content

''' 汉字批量转换成unicode编码 '''
def Urllib_Urlencode():

    base_url = 'https://www.baidu.com/s?'

    data = {
        'wd' : '周杰伦',
        'sex': '男',
        'location': '中国台湾省'
    }

    new_data = urllib.parse.urlencode(data)

    url = base_url + new_data

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    # 请求对象的定制
    request = urllib.request.Request(url = url, headers = headers)

    # 模拟向浏览器发送请求
    response = urllib.request.urlopen(request)

    # 获取响应的内容
    content = response.read().decode("utf-8")

    return content






