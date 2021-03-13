from appium.webdriver.webdriver import WebDriver

from this_is_appium.apppo.page.addcontact_page import AddcontactPage
from this_is_appium.apppo.page.base_page import BasePage


class AddressListPage(BasePage):

    def click_addcontact(self):
        element = self.swipe_find('添加成员')
        element.click()
        return AddcontactPage()