import sys
sys.path.append("..")

from this_is_selenium.base import Base


class TestWindow(Base):

    def test_window(self):
        # 访问百度
        self.driver.get("https://www.baidu.com")
        # 点击登录，点击之后，后有一个弹框
        self.driver.find_element_by_link_text("登录").click()
        # 点击弹框中的立即注册，点击之后，会在新窗口打开注册页面
        self.driver.find_element_by_link_text("立即注册").click()
        # 当前窗口的句柄
        now_window = self.driver.current_window_handle
        # 所有窗口的句柄
        all_window = self.driver.window_handles
        # 遍历所有窗口的句柄
        for window in all_window:
            # 如果不是当前窗口
            if window != now_window:
                # 切换窗口
                self.driver.switch_to.window(window)
        # 在新窗口的注册页面输入用户名
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")

