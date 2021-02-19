import sys
sys.path.append("..")
from this_is_selenium.base import Base
import time


class TestJS(Base):
    # 执行 js 控制滚动条
    def test_js(self):
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        # 执行 js 获取当前页面的 title
        js_title = "return document.title"
        print(self.driver.execute_script(js_title))
        time.sleep(3)
        # 执行 js 将滚动条拖到底部
        js_scroll = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js_scroll)
        # 点击用户反馈
        self.driver.find_element_by_link_text("用户反馈").click()
        time.sleep(3)

