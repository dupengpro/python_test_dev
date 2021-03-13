# appium

## 安装

1. Node.js：`brew install node`

   - 验证：`node -v`

2. [jdk](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)

   - 配置环境变量

     - `vim ~/.zshrc`

     - 添加：

       ```zsh
       # java 环境变量
       export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_281.jdk/Contents/Home
       export PATH=$PATH:$JAVA_HOME/bin:.
       export CLASS_PATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:.
       ```

     - 使配置生效：`source ~/.zshrc`

     - 验证：`java` 

     - 这里是 zsh 的配置，如果 Mac 使用的是 bash，则对应要修改的文件是 .bash_profile。配置过程和 .zshrc 相同

3. [Android-studio](https://developer.android.com/studio)

   - 配置 SDK 的环境变量：

     - `vim ~/.zshrc`

     - 添加：

       ```zsh
       # android sdk 环境变量
       export ANDROID_HOME=/Users/这里是用户名/Library/Android/sdk
       export PATH=$PATH:$ANDROID_HOME/platform-tools
       export PATH=$PATH:$ANDROID_HOME/tools/bin
       ```
     
     - 使配置生效：`source ~/.zshrc`
     
     - 验证：`adb --version`
     
     - 这里是 zsh 的配置，如果 Mac 使用的是 bash，则对应要修改的文件是 .bash_profile。配置过程和 .zshrc 相同


4. [appium-desktop](https://github.com/appium/appium-desktop/releases/tag/v1.20.2)
5. appium-python-client：`pip install appium-python-client`
6. appium-doctor：`npm install -g appium-doctor`
   - 验证：`appium-doctor --version`
7. 验证整个环境：`appium-doctor` 
8. 可选安装：[安卓模拟器](http://mumu.163.com/mac/index.html)


## Capability 设置

- `automationName` (android 默认使用 uiautomator2 ，ios 默认使用 XCUITest)
- `noReset` 是否重置测试环境
- `unicodeKsyBoard` `resetKeyBoard` 是否需要输入英文以外的语言并在测试完成后重置输入法
- `dontStopAppOnReset` 首次启动的时候，不停止
- `skipDeviceInitialization` 跳过安装、权限设置等操作，默认为 false 
- `skipServerInstallation` 跳过 UIautomator2 server 安装
- iOS only
  - `bundleId` 



## demo

1. 打开 appium-desktop ，点击 start server
2. 打开手机模拟器
3. 新建 test_demo.py

如果执行 `adb devices` 提示：List of devices attached

解决方法，重启服务：

1. `adb kill-server`
2. `adb start-server`

test_demo.py

demo 中的 android 版本是 6.0，需要通过 android-studio>Preference>Appearance&Behavior>System Settings>Android SDK 安装

```python
from appium import webdriver


desired_caps = {}
# 手机系统
desired_caps["platformName"] = "Android"
# 手机系统版本
desired_caps["platformVersion"] = "6.0"
# 设备名称，可以通过在命令行输入 adb devices 获取
desired_caps["deviceName"] = "emulator-5554"
# 指定测试 app 的包名，通过 adb logcat |grep -i displayed 获取
desired_caps["appPackage"] = "com.xueqiu.android"
# 指定测试 app 的具体界面，通过 adb logcat |grep -i displayed 获取
desired_caps["appActivity"] = "com.xueqiu.android.common.MainActivity"
# 不重置
desired_caps["noReset"] = "true"
# 不停止 app 的进程
desired_caps["dontStopAppOnReset"] = "true"
# 跳过设置
desired_caps["skipDeviceInitialization"] = "true"

# 连接 appium server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# 隐式等待
driver.implicitly_wait(5)
# 通过 id 定位到搜索框
driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('bytedance')
# 返回到上个页面
driver.back()
# 再返回一次，返回到首页
driver.back()
# 退出
driver.quit()
```

执行：`python test_demo.py`



## 移动端基础知识



### android 七大布局

- LinearLayout 线性布局
- RelativeLayout 相对布局
- FrameLayout 帧布局
- AbsoluteLayout 绝对布局
- TableLayout 表格布局
- GridLayout 网格布局
- ConstraintLayout 约束布局

### android 四大组件

- activity 与用户交互的可视化界面
- service 实现程序后台运行的解决方案
- content provider 内容提供者，提供程序所需要的数据
- broadcast receiver 广播接收器，监听外部事件

### android 常用控件

- TextView 文本控件
- EditText 可编辑的文本控件
- Button 按钮
- ImageButton 图片按钮
- ToggleButton 开关按钮
- ImageView 图片控件
- CheckBox 复选框
- RadioButton 单选框



布局是放置控件的容器，除了可以放置控件，还可以嵌套布局。



iOS 没有布局的概念，直接用变量之间的相对关系完成位置的计算。



## 元素定位

对控件进行定位。控件没有 CSS 。

定位方式：

- id

- accessibility_id

- classname

- xpath

  - `节点名` 选取此节点的所有子节点
- `/` 从根节点选取
  - `//` 相对定位
  - `.` 选取当前节点
  - `..` 选取当前节点的父节点
  - `@` 选择属性
  - `*` 任何元素
  - `@*` 任何属性



## 元素操作

常用方法：

- click 点击
- send_keys 输入
- set_value 设置元素的值
- clear 清除
- is_displayed() 是否可见，返回 ture 或 false
- is_selecetd() 是否被选中，返回 ture 或 false
- Is_enabled() 元素是否可用
- get_attribule() 获取属性值
- `.text` 获取元素文本
- `.location` 获取元素坐标
- `.size` 获取元素尺寸

## 触屏操作

- press 按下
- tap 点击
- release 释放
- move_to 移动到
- wait 等待
- longPress 长按
- cancel 取消
- perform 执行

滑动

```python
TouchAction().press(el0).moveTo(el1).release()
```

两点触控

```python
action0 = TouchAction().tap(el)
action1 = TouchAction().tap(el)
MultAction().add(action0).add(action1).perform()
```

获取窗口矩形坐标

```python
# 获取窗口的矩形坐标
window_rect = driver.get_window_rect()
width = window_rect['width']
height = window_rect['height']
# 滑动
x1 = int(width/2)
y_start = int(height * 4/5)
y_end = int(height * 1/5)
action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
```

手势解锁

```python
action = TouchAction(self.driver)
action.press().wart(100).move_to().wart(100).move_to().wart(100).move_to().wart(100).move_to().release().perform()
```


