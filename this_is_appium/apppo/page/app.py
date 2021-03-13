# 启动、停止、重启 app
import yaml
from appium.webdriver import webdriver

from this_is_appium.apppo.page.base_page import BasePage
from this_is_appium.apppo.page.main_page import MainPage

with open('../datas/caps.yml') as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']


class App(BasePage):
    def start(self):
        # 如果为 none ，创建
        if self.driver == None:
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            # 否则，直接启动
            # self.driver.start_activity('com.tencent.wework', '.launch.LaunchSplashActivity')
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.closs_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        return MainPage(self.driver)