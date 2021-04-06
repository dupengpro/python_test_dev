import yaml
from selenium.webdriver.common.by import By

from this_is_ui_framework.page.basepage import BasePage
from this_is_ui_framework.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find_and_click(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
        # 数据驱动
        self.parse('../page/market.yml', 'goto_search')
        return Search(self.driver)
