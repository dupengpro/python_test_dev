import sys

import yaml

from this_is_ui_framework.page.logger import log

sys.path.append("..")
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator, value):
        log.debug('find' + value)
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def find_and_click(self, locator, value):
        self.find(locator, value).click()

    def find_and_send(self, locator, value, content):
        self.find(locator, value).send_keys(content)

    # 截图（通过 appium）
    def screenshot(self):
        return self.driver.get_screenshot_as_png()

    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次， 未找到。")
            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def parse(self, yaml_path, fun_name):
        # 数据驱动
        with open(yaml_path, 'r', encoding='utf-8') as f:
            function = yaml.load(f)
        steps = function.get(fun_name)
        for step in steps:
            if step.get('action') == 'find_and_click':
                self.find_and_click(step.get('locator'), step.get('value'))
            elif step.get('action') == 'find_and_send':
                self.find_and_send(step.get('locator'), step.get('value'), step.get('content'))
