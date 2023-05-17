import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫文件的名字，用于运行爬虫的时候，使用的值
    name = "baidu"
    # 允许访问的域名
    # 在爬取时，不是此域名之下的url，会被过滤掉
    allowed_domains = ["www.baidu.com"]

    # 起始的url地址  指的是第一次要访问的域名， 可以是多个，但是一般是一个
    # 在allowed domain前添加 https://
    # 在allowed domain前添加 /
    start_urls = ["https://www.baidu.com"]

    # 是执行了start_urls之后 执行的方法 方法中的response就是返回的那个对象
    # 相当于 response = urllib.request.get() 
    #       response = requests.get()
    def parse(self, response):
        print("Hello World")
