import allure
import pytest


@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1"):
            print("输入用户名")
        with allure.step("步骤2"):
            print("输入密码")
        with allure.step("步骤3"):
            print("点击登陆按钮")

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