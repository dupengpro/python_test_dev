import sys

import yaml

from this_is_ui_framework.page.market import Market

sys.path.append("..")
from selenium.webdriver.common.by import By

from this_is_ui_framework.page.basepage import BasePage


class MainPage(BasePage):
    def goto_market(self):
        # self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        # self.find_and_click(By.XPATH, '//*[@text="行情"]')
        # 数据驱动
        self.parse('../page/main_page.yml', 'goto_market')
        return Market(self.driver)
