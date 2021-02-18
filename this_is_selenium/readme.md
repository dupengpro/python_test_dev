# selenium

官网：https://www.selenium.dev
安装：`pip install selenium`  

安装 ChromeDriver

- 根据 chrome 版本下载：`https://chromedriver.chromium.org/downloads`

- 解压下载的 zip

- 把解压出来的文件 chromedriver 复制或者移动到 `/usr/local/bin` 目录下

test_selenium.py

```python
from selenium import webdriver
import time


def test_selenium():
    # 获取浏览器驱动
    driver = webdriver.Chrome()
    # 访问百度
    driver.get("https://www.baidu.com/")
    # 等待
    time.sleep(2)
    # 退出
    driver.quit()
```

执行：`pytest test_selenium.py`



在百度首页输入关键字进行搜索

test_selenium.py

```python
from selenium import webdriver
import time


class TestBaidu:
    def setup(self):
        # 获取浏览器驱动
        self.driver = webdriver.Chrome()
        # 访问百度
        self.driver.get("https://www.baidu.com/")

    def test_selenium(self):
        time.sleep(2)
        # 定位到搜索框，输入关键字
        self.driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(2)
        # 定位到百度一下按钮，点击
        self.driver.find_element_by_id("su").click()

    def teardown(self):
        time.sleep(2)
        # 退出
        self.driver.quit()
```



隐式等待，定位到元素之后就进行下一步操作，不再继续等待

```python
...
    def setup(self):
        # 获取浏览器驱动
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(2)
        # 访问百度
        self.driver.get("https://www.baidu.com/")
...
```



