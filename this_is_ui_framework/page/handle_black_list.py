import allure
from selenium.webdriver.common.by import By
from this_is_ui_framework.page.logger import log


def handle_black():
    def run(*args, **kwargs):
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        # 相当于 self
        instance = args[0]
        try:
            log.debug("find " + args[2])
            return fun(*args, **kwargs)
        except Exception:
            # 把截图添加到测试报告中
            allure.attach(instance.screenshot(), attachment_type=allure.attachment_type.PNG)
            for ele_xpath in black_list:
                eles = instance.finds(By.XPATH, ele_xpath)
                if len(eles) > 0:
                    eles[0].click()
                    return fun(*args, **kwargs)

    return run