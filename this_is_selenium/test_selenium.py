from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
        # 判断百度一下按钮是不是可点击的状态
        ture_or_false = expected_conditions.element_to_be_clickable((By.ID, "su"))
        # 如果是，就不再等待，如果不是，就继续等待，最多等待10秒
        WebDriverWait(self.driver, 10).until(ture_or_false)
        # 点击百度一下按钮
        self.driver.find_element_by_id("su").click()

    def teardown(self):
        # 退出
        self.driver.quit()