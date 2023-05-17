import urllib.request

def Urllib_Six_Methods():

    ''' IMPORTANT: 一个类型和六个方法'''

    url = "https://www.baidu.com/"

    ''' IMPORTANT: Open the URL url, which be either a string or a Request object'''
    response = urllib.request.urlopen(url)

    ''' 3 ways to get content '''

    ''' 一次性读取整个文件内容 '''
    print(response.read())

    ''' 每次读取一行内容 '''
    print(response.readline())

    ''' 一次性读取整个文件内容, 并按行返回到list, 方便我们遍历 '''
    print(response.readlines())

    ''' get status code '''
    print(response.getcode()) 

    ''' get url '''
    print(response.geturl())

    ''' get headers '''
    print(response.getheaders())

def Urllib_Download_Content():

    dir = "D:/Python Tutorial/爬虫进阶/urllib/"

    ''' 下载网页 '''
    url_page = "https://www.baidu.com/"
    # url代表下载的路径，filename文件的名字
    urllib.request.urlretrieve(url = url_page, filename = dir + "baidu.html")

    ''' 下载图片 '''
    url_picture = "	https://t7.baidu.com/it/u=3631608752,3069876728&fm=193&f=GIF"
    # url代表下载的路径，filename文件的名字
    urllib.request.urlretrieve(url = url_picture, filename =  dir + "picture.gif")

    ''' 下载视频 '''
    url_video = "https://www.youtube.com/7e8572e6-671b-40cf-b770-3a6a1c44bf9e"
    # url代表下载的路径，filename文件的名字
    urllib.request.urlretrieve(url = url_video, filename =  dir + "video.mp4")

def Urllib_Custom():

    ''' 定制请求对象 '''

    url = "https://www.baidu.com/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    # 请求对象的定制是为了解决反爬的第一种手段
    # 因为参数顺序的问题，不能直接写url和headers, 中间还有data，所以需要关键字传参
    request = urllib.request.Request(url = url, headers = headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content

if __name__ == "__main__":

    Urllib_Six_Methods()





