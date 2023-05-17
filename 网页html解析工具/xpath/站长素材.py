from lxml import etree
import urllib.request

'''
    xpath解析
    (1) 本地文件:     html_tree = etree.parse('XX.html')
    (2) 服务器响应数据:       html_tree = etree.HTML(response.read().decode('utf-8'))
    (3) html_tree.xpath(xpath路径)

'''
# xpath语法： https://www.runoob.com/xpath/xpath-syntax.html

'''
基本语法

    1. 路径查询
        //: 查找所有子孙节点， 不考虑层级关系
        /. 找直接子节点

    2. 谓词查询
        //div[@d]
        //div[@id = "maincontent]

    3. 属性查询
        //@class

    4. 模糊查询
        //div[contains(@id, "he")]
        //div[starts-with(@id, "he")]
    
    5. 内容查询
        //div/h1/text()

    6. 逻辑运算
        //div[@id = "head" and @class = "s_down"]
        //title | //price
'''

def create_request(page):
    if (page == 1):
        url = "https://sc.chinaz.com/tupian/index.html"
    else:
        url = "https://sc.chinaz.com/tupian/index_%s.html"%page
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
     }

    # 请求对象的定制
    request = urllib.request.Request(url = url, headers = headers)

    return request

def get_content(request):
    response = urllib.request.urlopen(request, timeout = 30)
    content = response.read().decode("utf-8")

    return content

def download(content):

    tree = etree.HTML(content)

    name_list = tree.xpath('//div[@class = "container"]/div[@data-waterfall = "true"]//div/img/@alt')

    ''' 一般设计图片的网站都会懒加载'''
    src_list = tree.xpath('//div[@class = "container"]/div[@data-waterfall = "true"]//div/img/@data-original')

    dir = "D:/Python Tutorial/爬虫进阶/xpath/images/"

    for index, src in enumerate(src_list):

        print("https:" + src, dir + name_list[index] + '.jpg')
        # url代表下载的路径，filename文件的名字
        urllib.request.urlretrieve(url = "https:" + src, filename =  dir + name_list[index] + '.jpg')

if __name__ == "__main__":

    start = 1
    end = 10

    for page in range(start, end):
        request = create_request(page)
        content = get_content(request)
        download(content)
