import urllib.request
from bs4 import BeautifulSoup
import os

url = "https://www.starbucks.com.cn/menu/"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
     }

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode("utf-8")

soup = BeautifulSoup(content, 'html.parser')

# xpath: //ul[@class = "grid padded-3 product"]//strong/text()
name_list = soup.select('ul[class = "grid padded-3 product"] strong')
# xpath: //ul[@class = "grid padded-3 product"]//div/@style
src_list = soup.select('ul[class = "grid padded-3 product"] div')

names = []
urls = []

for name in name_list:
    name = name.get_text()
    image = name + ".jpg"
    names.append(image)

for src in src_list:
    content = src.get("style")
    content = content.split("(")[1].split(")")[0]
    url = f"https://www.starbucks.com.cn{content}".replace('"', '')
    urls.append(url)

dir = "爬虫进阶/网页html解析工具/bs4/星巴克/"

for name, url in zip(names, urls):

    name = name.replace("/", "")

    if name in os.listdir(dir):
        continue

    print("current image being downloaded: ", name)

    fname = dir + name

    # url代表下载的路径，filename文件的名字
    urllib.request.urlretrieve(url = url, filename =  fname)
