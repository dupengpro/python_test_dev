from selenium import webdriver
import time


class TestBaidu:
    def setup(self):
        # 获取浏览器驱动
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(2)
        # 访问百度
        self.driver.get("https://www.baidu.com/")

    def test_selenium(self):
        # 定位到搜索框，输入关键字
        self.driver.find_element_by_id("kw").send_keys("selenium")
        # 定位到百度一下按钮，点击
        self.driver.find_element_by_id("su").click()

    def teardown(self):
        # 退出
        self.driver.quit()