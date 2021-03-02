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
       ```
     
     - 使配置生效：`source ~/.zshrc`
     
     - 验证：`adb --version`
     
     - 这里是 zsh 的配置，如果 Mac 使用的是 bash，则对应要修改的文件是 .bash_profile。配置过程和 .zshrc 相同


4. [appium-desktop](https://github.com/appium/appium-desktop/releases/tag/v1.20.2)
5. appium-python-client：`pip install appium-python-client`
6. appium-doctor：`npm install -g appium-doctor`
   - 验证：`appium-doctor --version`
7. 验证整个环境：`appium-doctor` 
8. [安卓模拟器](http://mumu.163.com/mac/index.html)



## demo

1. 打开 appium-desktop ，点击 start server
2. 打开手机模拟器
3. 新建 test_demo.py

test_demo.py

demo 中的 android 版本是 6.0，需要通过 android-studio-Preference-Appearance&Behavior-System Settings-Android SDK 安装

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
desired_caps["appPackage"] = "com.android.settings"
# 指定测试 app 的具体界面，也是通过 adb logcat |grep -i displayed 获取
desired_caps["appActivity"] = "com.android.settings.Settings"
# 连接 appium server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# 退出
driver.quit()
```

执行：`python test_demo.py`

执行完成之后，appium 的日志会显示一行：`[Instrumentation] OK (1 test)`



