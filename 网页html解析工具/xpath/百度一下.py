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

def get_content(url):

    url = "https://www.baidu.com/"

    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    # 请求对象的定制
    request = urllib.request.Request(url = url, headers = headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content

if __name__ == "__main__":

    url = "https://www.baidu.com/"

    content = get_content(url)

    tree = etree.HTML(content)

    # reterive the data we want
    result = tree.xpath("//input[@type = 'submit']/@value")[0]

    print(result)

