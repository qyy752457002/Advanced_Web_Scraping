import urllib.request
import urllib.parse
import json

def Baidu_Translate():

    # 请求路径
    url = 'https://fanyi.baidu.com/sug'

    # 请求头
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    # 参数
    data = {
        'kw' : 'spider'
    }

    # post请求的参数必须进行编码，然后在用utf-8进行encode
    data = urllib.parse.urlencode(data).encode('utf-8')

    # post的请求参数是不会拼接在url后面的， 而是需要放在请求对象定制的参数中
    request = urllib.request.Request(url = url, data = data, headers = headers)

    # 模拟向浏览器发送请求
    response = urllib.request.urlopen(request)

    # 获取响应的数据
    content = response.read().decode('utf-8')

    # Convert string to Python dict
    data = json.loads(content)

    '''
        post请求的参数必须进行编码    data = urllib.parse.urlencode(data)
        编码之后 必须调用encode方法   data = urllib.parse.urlencode(data).encode('utf-8')
        参数是放在请求对象定制的方法中 request = urllib.request.Request(url = url, data = data, headers = headers)

    '''
    return data

print(Baidu_Translate())



