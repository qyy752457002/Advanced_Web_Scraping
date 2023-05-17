import urllib.request
import urllib.parse


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
     }
    
    data = {
        'start' : (page - 1) * 20,
        'limit' : 20
    }

    # urllib.parse.urlencode做编码
    data = urllib.parse.urlencode(data)

    url = base_url + data

    # 请求对象的定制
    request = urllib.request.Request(url = url, headers = headers)

    return request

def get_content(request):

    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    return content

def down_load(page, content):

    with open(f"D:/Python Tutorial/爬虫进阶/urllib/豆瓣电影/douban_{page}.json", 'w', encoding = 'utf-8') as fp:
        fp.write(content)

# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')

# with open('douban.json', 'w', encoding = 'utf-8') as fp:
#     fp.write(content)

if __name__ == "__main__":

    start_page = int(input("请输入起始页码"))
    end_page = int(input("请输入结束页码"))

    for page in range(start_page, end_page + 1):
        # get request
        request = create_request(page)
        # get content
        content = get_content(request)
        # 下载
        down_load(page, content)



