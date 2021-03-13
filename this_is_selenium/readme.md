# selenium

官网：https://www.selenium.dev
安装：`pip install selenium`  

安装 ChromeDriver

- 根据 chrome 版本下载：`https://chromedriver.chromium.org/downloads`

- 解压下载的 zip

- 把解压出来的文件 chromedriver 复制或者移动到 `/usr/local/bin` 目录下



## Demo

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



## 元素的定位与操作

### 元素定位

- `id`
- `name`
- `class_name`
- `tag_name`
- `link_text` 文本链接
- `partial_link_text`  模糊匹配
- `xpath`

### 元素操作

- `click()`
- `clear()`
- `send_keys()`
- `ActionChains` 鼠标键盘
  - 鼠标
    - `click`
    - `click_and_hold`
    - `context_click` 右键
    - `double_click`
    - `drag_and_drop(source, target)` 拖动 
    - `Perform` 执行
  - 键盘
    - `key_down` 按下
    - `key_up` 松开
    - `send_keys(Keys.按键)` 输入某个按键
    - `Perform` 执行
- `TouchAction` 兼容H5页面
  - `tap` 点击
  - `double_tap` 双击
  - `tap_and_hold`
  - `move` 移动未释放
  - `release` 释放
  - `scroll` 按住滚动
  - `scroll_from_element` 从某个元素开始按住滚动
  - `long_press` 长按
  - `flick` 手势滑动
  - `flick_element` 从某个元素开始滑动
  - `Perform` 执行



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



模拟键盘鼠标操作

```python
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

...				
  			# 定位到一个按钮
        button = self.driver.find_element_by_id("test_button")
        # 定位到一个文本链接
        link_text = self.driver.find_element_by_link_text("test_link")

        # 定位到两个元素
        drag_element = self.driver.find_element_by_id("test_drag")
        drop_element = self.driver.find_element_by_id("test_drop")

        action = ActionChains(self.driver)
        # 点击
        action.click(button)
        # 点击按住
        action.click_and_hold(button)
        # 右键
        action.context_click(button)
        # 双击
        action.double_click(button)
        # 鼠标移动到这个文本链接
        action.move_to_element(link_text)
        # 将一个元素拖拽到另一个元素上
        action.drag_and_drop(drag_element, drop_element)

        # 键盘输入回车键
        action.send_keys(Keys.ENTER)

        # 执行
        action.perform()
...
```





## 等待的方式

- `time.sleep()` 等待的时间是固定的
- `implicitly_wait()` 隐式等待，设置一次，对全局的 driver 都启用相同的等待时间，找到元素就不再等待
- `WebDriverWait` 显示等待，根据传入的条件判断是否继续等待
  - `selenium` 提供 `expected_conditions` 方法
  - `expected_conditions` 方法提供了  `element_to_be_clickable` 等判断条件



### 隐式等待

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



### 显示等待

```python
...  
  def test_selenium(self):
        # 定位到搜索框，输入关键字
        self.driver.find_element_by_id("kw").send_keys("selenium")
        # 判断百度一下按钮是不是可点击的状态
        ture_or_false = expected_conditions.element_to_be_clickable((By.ID, "su"))
        # 如果是，就不再等待，如果不是，就继续等待，最多等待10秒
        WebDriverWait(self.driver, 10).until(ture_or_false)
        # 点击百度一下按钮
        self.driver.find_element_by_id("su").click()
...
```



## 多窗口处理

句柄，是窗口的 id 

先获取当前窗口的句柄，使用 `driver.current_window_handle`

然后获取所有窗口的句柄，使用 `driver.window_handles`

窗口切换，使用 `driver.switch_to.window()`

窗口切换的例子：

因为 setup 和 teardown 比较常用，所以这里把他们添加到了 base.py 中

base.py

```python
from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
```

窗口切换

test_window.py

```python
import sys
sys.path.append("..")

from this_is_selenium.base import Base


class TestWindow(Base):

    def test_window(self):
        # 访问百度
        self.driver.get("https://www.baidu.com")
        # 点击登录，点击之后，后有一个弹框
        self.driver.find_element_by_link_text("登录").click()
        # 点击弹框中的立即注册，点击之后，会在新窗口打开注册页面
        self.driver.find_element_by_link_text("立即注册").click()
        # 当前窗口的句柄
        now_window = self.driver.current_window_handle
        # 所有窗口的句柄
        all_window = self.driver.window_handles
        # 遍历所有窗口的句柄
        for window in all_window:
            # 如果不是当前窗口
            if window != now_window:
                # 切换窗口
                self.driver.switch_to.window(window)
        # 在新窗口的注册页面输入用户名
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")

```



## frame 切换

frame 是框架，在一个页面中可能存在多个 frame ，相互独立，所以会出现在这个 frame 中定位不到另一个 frame 中的元素的情况。这个时候需要切换 frame 。

`driver.switch_to.frame()`

`driver.switch_to.default_content()` 切换到默认 frame

`driver.switch_to.parent_frame()` 切换到父级 frame



## 执行 JS

`execute_script` 执行

`return` 返回 js 的返回结果

`execute_script` arguments 传参

test_js.py

```python
import sys
sys.path.append("..")
from this_is_selenium.base import Base
import time


class TestJS(Base):
    # 执行 js 控制滚动条
    def test_js(self):
        self.driver.get("https://www.baidu.com")
        # 浏览器窗口最大化
        self.driver.maximize_window()
        # 搜索关键字
        self.driver.find_element_by_id("kw").send_keys("selenium")
        # 点击百度一下按钮
        self.driver.find_element_by_id("su").click()
        time.sleep(3)
        # 执行 js 获取当前页面的 title
        js_title = "return document.title"
        print(self.driver.execute_script(js_title))
        time.sleep(3)
        # 执行 js 将滚动条拖到底部
        js_scroll = "document.documentElement.scrollTop=10000"
        self.driver.execute_script(js_scroll)
        # 点击用户反馈
        self.driver.find_element_by_link_text("用户反馈").click()
        time.sleep(3)

```

有的日期控件是只读的，通过 selenium 不能赋值，可以通过执行 js 脚本

1. 获取到日期控件：`date_input = document.getElementById("train_date")`
2. 去掉日期控件的只读属性：`date_input.removeAttribute("readonly")`
3. 赋值：`date_input.value="1949-09-30"`



test_dateinput.py

```python
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
      
```

执行：`pytest test_dateinput.py -vs`

执行结果：

```bash
collected 1 item                                                                                                                                                                                                          

test_dateinput.py::TestDataInput::test_dateinput 1949-09-30
PASSED
```



## 文件上传

`send_keys("文件路径")`

## 弹框处理

`switch_to.alert()` 

`accept()` 确认

- `driver.switch_to.alert.acceppt()`

`dismiss` 取消

`text` 获取弹框上面的文本信息



## 复用浏览器

不重新打开新的浏览器。应用场景：比如有时候需要通过手机扫码登录，selenium 无法实现扫码操作。可以通过复用浏览器的方式，因为复用的浏览器会记录浏览器的会话状态。

命令行输入 `chrome -remote-debugging-port=9999`

```python
chrome_arg = webdeiver.ChromeOptions()
chrome_arg.debugger_address = '127.0.0.1:9999'
self.driver = webdriver.Chrome(options=chrome_arg)
self.driver.get('...')
```



## 使用 cookie

```python
...
# 登录
...
# 获取
cookies = driver.get_cookies()
# 添加
for i in cookies:
	driver.add_cookie(i)

```



## page object 设计模式

页面 --> 类

​	首页 --> class HomePage

​	注册页 --> class RegisterPage

​	登录页 --> class LoginPage

​	...

pages

首页有哪些功能：进入注册页，进入登录页...

home_page.py

```python
class HomePage:
	def goto_register(self):
		pass
  def goto_login(self):
    pass
```

注册页有哪些功能：注册...

register_page.py

```python
class RegisterPage:
	def register(self):
    pass
```

登录页有哪些功能：进入注册页，登录，忘记密码...

login_page.py

```python
class LoginPage:
  def goto_register(self):
		pass
  
  def login(self):
    pass
  
	def forget_password(self)
  	pass
```

实现功能

home_page.py

```python
class HomePage:
  def __init__(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(10)
    self.driver.get("...")
    
	def goto_register(self):
		self.driver.find_element_by_id("register").click()
  	return RegisterPage(self.driver)
  
  def goto_login(self):
    self.driver.find_element_by_id("login").click()
    return LoginPage(self.driver)
```

register_page.py

```python
class RegisterPage:
  def __init__(self, driver):
    self.driver = driver
    
	def register(self):
    pass
```

login_page.py

```python
class LoginPage:
  def __init__(self, driver):
    self.driver = driver
  
  def goto_register(self):
		self.driver.find_element_by_id("register").click()
  	return RegisterPage(self.driver)
  
  def login(self):
    pass
  
	def forget_password(self)
  	pass
```

测试

cases

test_register.py

```python
class TestRegister:
  def test_register(self):
    home = HomePage()
    home.goto_register().register()
	
  def test_register_from_login(self):
    home = HomePage()
    home.goto_login().goto_register().register()
    
```



