import jsonpath
import json

'''
    只能解析本地文件，不能解析服务器响应数据
    
    obj = json.load(open('json文件', 'r', encoding = 'utf-8))
    ret = jsonpath.jsonpath(obj, 'jsonpath语法)

'''
# JSONPATH入门
# https://blog.csdn.net/Obstinate_L/article/details/125294971

'''

    XPath	JSONPath	       Description
    /	    $	                表示根元素
    .	    @	                当前元素
    /	    . or []	            子元素
    ..	    n/a	                父元素
    //	    ..	                递归下降, JSONPath是从E4X借鉴的。
    *	    *	                通配符，表示所有的元素
    @	    n/a	                属性访问字符
    []	    []	                子元素操作符
    |	    [,]	                连接操作符在XPath 结果合并其它结点集合。JSONP允许name或者数组索引。
    n/a	    [start:end:step]    数组分割操作从ES4借鉴。
    []	    ?()	                应用过滤表示式
    n/a	    ()	                脚本表达式，使用在脚本引擎下面。
    ()	    n/a	                Xpath分组


'''

if __name__ == "__main__":

    obj = json.load(open('D:/Python Tutorial/爬虫进阶/网页html解析工具/jsonpath/book.json', 'r', encoding = 'utf-8'))

    ''' 书店所有书的作者 '''
    author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
    print(author_list)

    ''' 所有的作者 '''
    author_list = jsonpath.jsonpath(obj, '$..author')
    print(author_list)

    ''' store下面所有的元素 '''
    tag_list = jsonpath.jsonpath(obj, '$.store')
    print(tag_list)

    ''' store里面所有东西的price'''
    price_list = jsonpath.jsonpath(obj, '$.store..price')
    print(price_list)

    ''' 第三本书 '''
    third_book = jsonpath.jsonpath(obj, '$..book[2]')
    print(third_book)

    ''' 最后一本书 '''
    last_book = jsonpath.jsonpath(obj, '$..book[(@.length - 1)]')
    print(last_book)

    ''' 前面两本书'''
    book_list = jsonpath.jsonpath(obj, '$..book[0, 1]')
    book_list = jsonpath.jsonpath(obj, '$..book[:2]')
    print(book_list)

    ''' 条件过滤需要在()前面加一个问号'''
    ''' 过滤出所有包含isbn的书 '''
    filtered_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
    print(filtered_list)

    ''' 条件过滤需要在()前面加一个问号'''
    ''' 过滤出所有价格高于10的书 '''
    filtered_price_list = jsonpath.jsonpath(obj, '$..book[?(@.price > 10)]')
    print(filtered_price_list)

    ''' 所有元素 '''
    elements = jsonpath.jsonpath(obj, '$..*')
    print(elements)