# 1. 导入selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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
path = "D:/Python Tutorial/爬虫进阶/selenium/chromedriver.exe"
browser = webdriver.Chrome(path)

# 3. 访问网址
url = "http://www.baidu.com"
browser.get(url)

time.sleep(2)

# 4. 获取文本框的对象
input = browser.find_element(By.ID, "kw")

# 5. 在文本框中输入周杰伦
input.send_keys('周杰伦')

time.sleep(2)

# 6. 获取百度一下的按钮
button = browser.find_element(By.ID, "su")

# 7. 点击按钮
button.click()

time.sleep(2)

# 8. 滑到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

time.sleep(2)

# 9. 获取下一页的按钮
next = browser.find_element(By.XPATH, "//a[@class = 'n']")

time.sleep(2)

# 10. 点击下一页
next.click()

time.sleep(2)

# 11. 回到上一页
browser.back()

time.sleep(2)

# 12. 回去
browser.forward()

time.sleep(2)

# 13. 退出
browser.quit()















