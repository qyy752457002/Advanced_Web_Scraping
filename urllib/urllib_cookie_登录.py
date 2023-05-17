import urllib.request
import urllib.parse

'''
    适用场景: 数据采集的时候， 需要绕过登录，然后进入到某个页面
    个人信息页面是utf-8, 但是还是是报错了编码, 因为没有进入到个人信息页面，而是跳转到登录页面
    那么登录页面utf-8, 所以报错

'''
    
base_url = 'https://m.weibo.cn/profile/1827749407'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    # cookie携带你的登录信息，如果登录之后有cookie，我们就可以携带cookie进入任何页面
    'cookie': "WEIBOCN_FROM=1110006030; WEIBOCN_WM=3349; SUB=_2A25JWL26DeRhGedG6VUW9CfIyzuIHXVqosPyrDV6PUJbkdB-LXDGkW1NUVtfjIher8J0kFULq2DzNuNKIemaI3bR; MLOGIN=1; _T_WM=91956219445; M_WEIBOCN_PARAMS=lfid=102803&luicode=20000174&uicode=20000174; XSRF-TOKEN=eddd60",
    # referer 判断当前路径是不是由上一个路径进来的
    'referer': 'https://m.weibo.cn/login?phone=13958310806&key=2NzZkXM3YAARQ1NQvQ2fMc1o0Esam7d41DXB3YV9yZWdfbG9naW4.&loginScene=102003&backURL=https%3A%2F%2Fm.weibo.cn%2F'
        }
    
# 请求对象的定制
request = urllib.request.Request(url = base_url, headers = headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

print(content)

with open ('D:/Python Tutorial/爬虫进阶/urllib/weibo.html', 'w', encoding = 'utf-8') as fp:
    fp.write(content)

