import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1683867448004_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'cookie': 'thw=au; _uetvid=6cb4af306a3611ed9c73c7a59b187d6b; _ga=GA1.2.240784170.1681808430; t=feef83f4ebf77604124be77ecd88b44b; hng=AU%7Czh-CN%7CAUD%7C36; _ga_YFVFB9JLVB=GS1.1.1681808429.1.1.1681808438.0.0.0; useNativeIM=false; wwUserTip=false; xlly_s=1; _samesite_flag_=true; cookie2=1a1240f4dbd406a5ceeef2b29ed23250; _tb_token_=ebe3676eb671e; _m_h5_tk=94f0db4ec1b8c0a999b65f6644d1f1c9_1683870983350; _m_h5_tk_enc=79626bab6b91197e3939c348cce37970; tb_city=110100; tb_cityName="sbG+qQ=="; mt=ci=0_0; v=0; cna=5+ypHAs1bn8CAa8kusVS/+wU; sgcookie=E100WOUJ6oxK8O6CFfkQfkB1lzoyRjpmsEIBFdxg9TllkBnqL9GEQA6290729N9qAEc4otrWbzwN%2FCTI2fFNY46WUgjysFdYgf0c5HkGhbX0U%2Bk%3D; uc1=cookie15=URm48syIIVrSKA%3D%3D&cookie21=UtASsssme%2BBq&cookie14=Uoe8idvuLkqNTg%3D%3D&pas=0&existShop=false&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D; uc3=id2=UNQ3HLYU0144dg%3D%3D&nk2=0%2B5q13SThg6169Yh&lg2=Vq8l%2BKCLz3%2F65A%3D%3D&vt3=F8dCsfAoLaunD35Kgo0%3D; csg=e9c656e0; lgc=%5Cu7231%5Cu8DF3%5Cu7684%5Cu9C7C5051; cancelledSubSites=empty; dnk=%5Cu7231%5Cu8DF3%5Cu7684%5Cu9C7C5051; skt=74c7f42fd6f631b7; existShop=MTY4Mzg2Njg2Nw%3D%3D; uc4=id4=0%40UgP8IagqCD%2BryHv%2Fa%2F0AiuaGaOt%2F&nk4=0%400VVDKwh1evhpB5622PdQEK23nJutNRk%3D; tracknick=%5Cu7231%5Cu8DF3%5Cu7684%5Cu9C7C5051; _cc_=VT5L2FSpdA%3D%3D; l=fB_pZwreTcIrRNtvBO5aourza77O3Idb8sPzaNbMiIEGa6sd9F97PNC_dO7WWdtjQTfbXetz_ANlDdF9lizp_giMW_N-1NKclYp6-bpU-L5..; isg=BFFRjniS0T0Y2joX3LH5ViTbYF3rvsUwWGFdyzPn05g32nAsewjiALs0fLY8Ul1o; tfstk=cfPcBmsBk-kXsSfTVoGfGb36sLBRZROZx5P7aNDQJuJEImFPiS9yL8nlrmjC0d1..',
    'referer': 'https://dianying.taobao.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url = url, headers = headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8').split('(')[1].split(')')[0]

with open("D:/Python Tutorial/爬虫进阶/网页html解析工具/jsonpath/淘票票.json", 'w', encoding = 'utf-8') as fp:
    fp.write(content)

obj = json.load(open('D:/Python Tutorial/爬虫进阶/网页html解析工具/jsonpath/淘票票.json', 'r', encoding = 'utf-8'))

city_list = jsonpath.jsonpath(obj, '$..regionName')

print(city_list)

