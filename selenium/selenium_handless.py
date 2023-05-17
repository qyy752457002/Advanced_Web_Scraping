# 1. 导入selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
模拟浏览器功能. 自动执行浏览器中的js动态加载

'''

'''
载入cookie

browser.add_cookie(cookie)

'''

'''
元素定位

1. find_element(By.CLASS_NAME, "class name")

2. find_element(By.NAME, "name")

3. find_element(By.XPATH, "xpath")

4. find_element(By.TAG_NAME, "tag name")

5. ind_element(By.CSS_SELECTOR, "css selector")

6. find_element(By.LINK_TEXT, "link text")

7. find_element(By.ID, "id")

'''

'''
访问元素信息

1. 获取元素属性
   .get_attribute('class')

2. 获取元素文本
   .text

3. 获取id
   .id

4. 获取标签名
   .tag_name

'''

'''
交互

1. 点击: click()

2. 输入: send_keys()

3. 后退操作: browser.back()

4. 前进操作: browser.forward()

5. 模拟JS滚动:
    js = 'document.documentElement.scrollTop=100000'
    browser.execute_script(js) 执行js代码

6. 获取网页代码: page_source

7. 退出: browser.quit()

'''

# Selenium Tutorial: https://selenium-python.readthedocs.io/locating-elements.html#locating-by-id

# 2. 创建浏览器操作对象

def share_browser():
   options = Options()
   options.add_argument('--headless')
   options.add_argument('--disable-gpu')

   ''' path是本地chrome浏览器的文件路径 '''
   path = r'C:/Program Files/Google/Chrome/Application/chrome.exe'
   options.binary_location = path

   browser = webdriver.Chrome(options = options)

   return browser

if __name__ == "__main__":
       
   url = "https://www.baidu.com/"
       
   b = share_browser()
   b.get(url)

   # 对百度主页做截图
   b.save_screenshot("D:/Python Tutorial/爬虫进阶/selenium/baidu.png")

   b.quit()


