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