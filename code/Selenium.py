pip install selenium

'''
下载浏览器驱动: Selenium 需要一个与你的浏览器相对应的驱动程序来控制浏览器。例如，如果你使用的是 Chrome 浏览器，你需要下载 ChromeDriver。确保下载的驱动版本与你的浏览器版本相匹配。
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class wait_for_more_elements:
    def __init__(self, locator, count):
        self.locator = locator
        self.count = count

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        return len(elements) > self.count

class wait_for_less_elements:
    def __init__(self, locator):
        self.locator = locator
        self.count = 0

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        return len(elements) <= self.count

# 指定浏览器驱动的路径
driver = webdriver.Chrome('/path/to/chromedriver')

# 设置隐式等待为10秒 全局设置
driver.implicitly_wait(10)



# 打开网页
driver.get('http://www.example.com')

'''
find_element_by_class_name, find_element_by_xpath, find_element_by_css_selector
'''
download_button = driver.find_element_by_id('downloadButtonId')

# # 滚动到该元素
driver.execute_script("arguments[0].scrollIntoView();", download_button)

'''
presence_of_element_located: 等待直到指定的元素在 DOM 中出现，但不一定可见。
visibility_of_element_located: 等待直到指定的元素不仅出现在 DOM 中，且可见。
element_to_be_clickable: 等待直到元素可被点击。
text_to_be_present_in_element: 等待直到指定的元素中出现了预期的文本。
invisibility_of_element_located：等待指定元素消失在DOM中
staleness_of：这个条件用于检查某个元素是否不再附着于 DOM。它通常用于等待页面刷新后元素的消失。
'''
# 等待直到元素可见，最多等待10秒
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "myElementId"))
)

# 滚动到页面底部
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# 滚动到页面的特定高度（例如，向下滚动 1000 像素）
driver.execute_script("window.scrollTo(0, 1000);")

# 等待固定时间，例如5秒
time.sleep(5)
# 等待 JavaScript 表示页面加载完毕
WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

# 初始元素数量
initial_count = len(driver.find_elements(By.CSS_SELECTOR, '.my-items'))

# 等待某个元素数量超出设置的个数
WebDriverWait(driver, 10).until(wait_for_more_elements((By.CSS_SELECTOR, '.my-items'), initial_count))

# 等待某个元素数量为0，也就是消失
WebDriverWait(driver, 10).until(wait_for_less_elements((By.CSS_SELECTOR, '.my-items')))

# 点击按钮
download_button.click()

# 关闭浏览器
driver.quit()
