from bs4 import BeautifulSoup

''' 
    通过解析本地文件 将bs4的基础语法进行讲解
    默认打开文件的编码格式是gbk,所以在打开文件的时候需要指定编码
'''
soup = BeautifulSoup(open('D:/Python Tutorial/爬虫进阶/网页html解析工具/bs4/weibo.html', encoding = 'utf-8'), 'html.parser')

'''
    根据标签名查找节点
    找到的是第一个符合条件的数据
'''
print(soup.a)
''' 获取标签的属性和属性值'''
print(soup.a.attrs)

# bs4 教程: http://c.biancheng.net/python_spider/bs4.html

'''bs4的一些函数'''

''' (1) find 返还第一个符合条件的数据 
        根据class的值找到对应的标签对象，注意class需要添加下划线
'''

# soup.find('a', title = 'a2')
# soup.find('a', class_ = 'a1')

''' (2) find_all 返还一个列表, 列表内是符合条件的数据
        根据class的值找到对应的标签对象，注意class需要添加下划线

        如果想获取多个标签的数据，需要在finall_all的参数在添加列表的数据

        limit的作用是查找前n个数据
'''

# soup.find_all('a')
# soup.find_all(['a', 'span'])
# soup.find_all('li', limit = 2)

''' (3) select 返还一个列表, 列表内是符合条件的数据
'''
# bs4 教程: https://www.jianshu.com/p/dc8df30ee0c8

# CSS 标签选择器：根据标签名称查询标签对象

'''
    res1 = soup.select("span")
    print(res1)

    # 2. CSS ID选择器：根据ID查询标签对象
    res2 = soup.select("#gender")
    print(res2)

    # 3. CSS 类选择器：根据class属性查询标签对象
    res3 = soup.select(".intro")
    print(res3)

    # 4. CSS 属性选择器
    res41 = soup.select("span[id]")
    print(res41)
    res42 = soup.select("span[id='gender']")
    print(res42)

    # 5. CSS 包含选择器
    # IMPORTANT: all children below tag p 
    res5 = soup.select("p span#name")
    print(res5)

    # 6. 获取标签内容
    # IMPORTANT: one level below node with tag p, just direct child
    res6 = soup.select("p > span.intro")
    print(res6[0].string)
    print(res6[0].getText())

'''