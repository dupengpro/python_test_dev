from appium import webdriver


desired_caps = {}
# 手机系统
desired_caps["platformName"] = "Android"
# 手机系统版本
desired_caps["platformVersion"] = "6.0"
# 设备名称，可以通过在命令行输入 adb devices 获取
desired_caps["deviceName"] = "emulator-5554"
# 指定测试 app 的包名，通过 adb logcat |grep -i displayed 获取
desired_caps["appPackage"] = "com.android.settings"
# 指定测试 app 的具体界面，通过 adb logcat |grep -i displayed 获取
desired_caps["appActivity"] = "com.android.settings.Settings"
# 连接 appium server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# 退出
driver.quit()