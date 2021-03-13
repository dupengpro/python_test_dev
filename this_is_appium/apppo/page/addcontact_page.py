# 添加成员页面
from appium.webdriver.common.mobileby import MobileBy

from this_is_appium.apppo.page.base_page import BasePage
from this_is_appium.apppo.page.editcontact_page import EditContactPage


class AddcontactPage(BasePage):

    def addcontact_menual(self):
        # 手动输入添加
        self.driver.find_element(MobileBy.XPATH, )
        return EditContactPage()

    def test_delcontact(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/igk').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="搜索"]').send_keys('usernmae')
        elelist = self.driver.find_elements(MobileBy.XPATH, '//*[@text="username"]')
        if len(elelist) > 1:
            elelist[1].click()

