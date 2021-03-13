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