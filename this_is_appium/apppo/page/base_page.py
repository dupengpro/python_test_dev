from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, deiver: WebDriver=None):
        self.driver = deiver

    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def swipe_find(self):
        while True:
            try:
                element = self.driver.find_element_by_id('test')
                return element
            except:
                print('未找到')
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get('height')
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)