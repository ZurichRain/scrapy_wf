pip install selenium

'''
下载浏览器驱动: Selenium 需要一个与你的浏览器相对应的驱动程序来控制浏览器。例如，如果你使用的是 Chrome 浏览器，你需要下载 ChromeDriver。确保下载的驱动版本与你的浏览器版本相匹配。
'''

from selenium import webdriver

# 指定浏览器驱动的路径
driver = webdriver.Chrome('/path/to/chromedriver')

# 打开网页
driver.get('http://www.example.com')

'''
find_element_by_class_name, find_element_by_xpath, find_element_by_css_selector
'''
download_button = driver.find_element_by_id('downloadButtonId')

# # 滚动到该元素
driver.execute_script("arguments[0].scrollIntoView();", download_button)

# 滚动到页面底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 滚动到页面的特定高度（例如，向下滚动 1000 像素）
driver.execute_script("window.scrollTo(0, 1000);")

# 点击按钮
download_button.click()

# 关闭浏览器
driver.quit()
