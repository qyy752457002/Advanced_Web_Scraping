import requests

url = "https://www.baidu.com/s?"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }

proxy = {
    'http': '182.34.102.50 : 9999'
}

response = requests.get(url = url, headers = headers, procies = proxy)

content = response.text

with open('D:/Python Tutorial/爬虫进阶/requests/daili.html', 'w', encoding = 'utf-8') as fp:
    fp.write(content)