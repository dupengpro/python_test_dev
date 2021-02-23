# allure

用于生成测试报告



官网：`http://allure.qatools.ru/`

安装：

1. 安装 allure ：`brew install allure`
2. 安装 allure-pytest 插件：`pip install allure-pytest`



## 常用特性

- `feature` 被测模块
- `story` 测试用例
- `step` 操作步骤



test_feature_story.py

```python
import allure
import pytest


@allure.feature("测试登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        pass

    @allure.story("登录失败")
    def test_login_fail(self):
        pass


@allure.feature("搜索模块")
class TestSearch():
    @allure.story("搜索测试用例1")
    def test_case1(self):
        pass

    @allure.story("搜索测试用例2")
    def test_case2(self):
        pass
```



测试指定的 feature

执行：`pytest test_feature_story.py --allure-features="测试登录模块" -vs`

执行结果：

```bash
collected 4 items                                                                                                                                                                                                         

test_feature_story.py::TestLogin::test_login_success PASSED
test_feature_story.py::TestLogin::test_login_fail PASSED
```

测试指定的 story

执行：`pytest test_feature_story.py --allure-stories="登录失败" -vs`

执行结果：

```bash
collected 4 items                                                                                                                                                                                                         

test_feature_story.py::TestLogin::test_login_fail PASSED
```

添加 step

```python
...
@allure.feature("测试登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1"):
            print("输入用户名")
        with allure.step("步骤2"):
            print("输入密码")
        with allure.step("步骤3"):
            print("点击登陆按钮")
...
```

执行：`pytest test_feature_story.py --allure-features="登录模块" -vs`

执行结果：

```bash
collected 4 items                                                                                                                                                                                                         

test_feature_story.py::TestLogin::test_login_success 输入用户名
输入密码
点击登陆按钮
PASSED
test_feature_story.py::TestLogin::test_login_fail PASSED
```

生成测试结果

执行：`pytest test_feature_story.py --allure-features="登录模块" -vs --alluredir=./result`

执行结束之后会在当前目录下生成 result 文件夹，文件夹中有生成了记录测试结果的 json 文件

生成测试报告

执行：`allure serve ./result`

执行结束之后，会自动通过浏览器打开生成的测试报告



关联测试用例

`@allure.testcase(testcase_link, testcase_title)`

test_testcase.py

```python
import allure


TEST_CASE_LINK = "https://github.com/dupengpro/python_test_dev"


@allure.testcase(TEST_CASE_LINK, "测试 testcase link")
def test_with_testcase_link():
    pass
```



执行测试：`pytest test_testcase.py --alluredir ./result1`

生成测试报告：`allure serve ./result1`

在测试报告的测试套（Suites）-- 总览（Overview）会有：链接（Linkes），可以跳转到添加的链接地址



生成测试报告文件

执行： `allure generate ./result1` 

执行完成之后会在当前目录下生成 allure-report 文件夹，在这个文件夹中会有一个 index.html 文件，这个文件就是生成的测试报告

在 PyCharm 中右键这个文件，选择 Open In -- Browser -- Chrome ，会在谷歌浏览器显示。

指定测试报告文件生成的目录可以通过添加参数： `-o 文件夹名称` ，比如 `allure generate ./result1 -o report` 



给测试用例定义重要级别

`@allure severity`

级别由高到低分别有：

- BLOCKER
- CRITICAL
- NORMAL
- MINOR
- TRIVIAL

test_severity.py

```python
import allure


def test_no_severity():
    pass


@allure.severity(allure.severity_level.BLOCKER)
def test_blocker_severity():
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_critical_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_normal_severity():
    pass


@allure.severity(allure.severity_level.MINOR)
def test_minor_severity():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
class TestSeverity:
    def test_case1(self):
        pass

    @allure.severity(allure.severity_level.NORMAL)
    def test_case2(self):
        pass
```

执行级别为 trivial 的测试用例：`pytest test_severity.py --allure-severities="trivial" -vs`

执行结果：

```bash
collected 7 items                                                                                                                                                                                                         

test_severity.py::TestSeverity::test_case1 PASSED
```



执行级别为 normal 的测试用例：`pytest test_severity.py --allure-severities="normal" -vs`

执行结果：

```bash
collected 7 items                                                                                                                                                                                                         

test_severity.py::test_normal_severity PASSED
test_severity.py::TestSeverity::test_case2 PASSED
```



通过执行结果可以看出，当类和方法都添加了 severity 的时候，会以方法指定的级别为准。



给测试用例添加标题

`@allure.title`

test_title.py

```python
import allure


@allure.title("测试 title")
def test_title():
    pass
```

执行测试：`pytest test_title.py --alluredir ./result3`

查看测试报告：`allure serve ./result3`

添加了 title 之后，这个测试用例的名称 `test_title`  在测试报告中会显示为：`测试 title`



添加截图

`allure.attach`

test_attach.py

```python
import allure


# 添加文本信息
def test_attach_text():
    allure.attach("文本信息", name="文本信息文件", attachment_type=allure.attachment_type.TEXT)


# 添加 html
def test_attach_html():
    allure.attach("<h3>html</h3>", name="html 文件", attachment_type=allure.attachment_type.HTML)


# 添加图片
def test_attach_picture():
    allure.attach.file("./test.jpg", name="图片文件", attachment_type=allure.attachment_type.JPG)
```

执行：`pytest test_attach.py --alluredir ./result4`

查看报告：`allure serve ./result4`

添加的内容可以在测试报告的概览中查看。



清空上一次的测试结果：`--clean-alluredir`

运行一个本地服务分享测试报告：

- `allure open -h 指定一个ip -p 指定一个端口 测试报告所在的文件夹`
- 比如：`allure open -h 192.168.3.119 -p 8883 ./report`
- 服务启动之后，会在本地的浏览器自动打开测试报告
- 通过链接可以分享测试报告





