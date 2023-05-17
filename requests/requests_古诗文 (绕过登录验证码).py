# 通过登录，进入主页面

# 通过登录接口，我们发现，登录时候需要的参数很多

'''
__VIEWSTATE:  a3CURl/bGbshuconvZsK3VqU0/05TmbRwAAIQJ2L+LsfRja23Dtlfdk1/D41O1iRUgVOoIk1MJCnVM2wbHH3dGz9T9pincURurdye4bFo7fscrz0+0Br3SCLy3ry8bKyYt+HF5IxVxOl9kIPK7QPm/Ple+w=
__VIEWSTATEGENERATOR: C93BE1AE
from: http://so.gushiwen.cn/user/collect.aspx
email: 752457002@qq.com
pwd: qyy2614102
code: 9W21
denglu: 登录

难点: (1) __VIEWSTATE, __VIEWSTATEGENERATOR是可变的 (一般情况下看不到的数据都是咋页面的)
      我们观察到
      (2) 验证码

'''
import requests
from bs4 import BeautifulSoup
import urllib.request

url = "https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx"

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
            }

# 获取网页源码
response = requests.get(url = url, headers = headers)
content = response.text

# 解析页面
soup = BeautifulSoup(content, "html.parser")

# 获取_VIEWSTATE
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取_VIEWSTATE
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# 获取验证码属性
code = soup.select("#imgCode")[0].attrs.get('src')
code_url = "https://so.gushiwen.cn" + code

# 获取验证码的图片之后，下载到本地，然后观察验证码，观察之后，然后在控制台输入这个验证码，就可以将这个值给code的参数，就可以登陆
# urllib.request.urlretrieve(url = code_url, filename = 'D:/Python Tutorial/爬虫进阶/requests/code.jpg')

''' requests 里面有一个方法session, 通过session的返回值，就能使请求变成一个对象'''

session = requests.session()
# 验证码url的内容
response_code = session.get(code_url)
# 注意次数使用二进制数据，因为我们要使用的是图片下载
content_code = response_code.content
# wb模式就是将二进制文件写入文件
with open('D:/Python Tutorial/爬虫进阶/requests/code.jpg', 'wb') as fp:
    fp.write(content_code)

# 用户胡输入验证码
code_name = input("请输入你的验证码: ")

# 点击登陆
url_post = "https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx"

data_post = {
      '__VIEWSTATE': viewstate,
      '__VIEWSTATEGENERATOR': viewstategenerator,
      'from': 'http://so.gushiwen.cn/user/collect.aspx',
      'email': '752457002@qq.com',
      'pwd': 'qyy2614102',
      'code': code_name,
      'denglu': '登录'
}

# 获取登录后的网页源码
response_post = session.post(url = url_post, headers = headers, data = data_post)
content_post = response_post.text

with open("D:/Python Tutorial/爬虫进阶/requests/gushiwen.html", 'w', encoding = 'utf-8') as fp:
    fp.write(content_post)




