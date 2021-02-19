import sys
sys.path.append("..")
from this_is_selenium.base import Base
import time


class TestDataInput(Base):

    def test_dateinput(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.maximize_window()
        self.driver.execute_script('date_input=document.getElementById("train_date")')
        self.driver.execute_script('date_input.removeAttribute("readonly")')
        print(self.driver.execute_script('return date_input.value="1949-09-30"'))
        time.sleep(3)
