from appium.webdriver.common.mobileby import MobileBy

from this_is_appium.apppo.page.addresslist_page import AddressListPage
from this_is_appium.apppo.page.base_page import BasePage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, '//*[@text="通讯录"]')

    def goto_addresslist(self):
        # 点击通讯录
        self.find(*self.addresslist_element).click()
        return AddressListPage(self.driver)