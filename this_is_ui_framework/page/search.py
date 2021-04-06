import yaml
from selenium.webdriver.common.by import By

from this_is_ui_framework.page.basepage import BasePage


class Search(BasePage):
    def search(self):
        # self.find_and_send(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
        # 数据驱动
        self.parse('../page/search.yml', 'search')
        return Search(self.driver)