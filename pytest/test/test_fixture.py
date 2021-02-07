import pytest


# # 给 login 函数添加 fixture
# @pytest.fixture(scope="session")
# def login():
#     print("登录")
#     message = "我是 message"
#     yield message
#     print("登出")


# @pytest.fixture()
# def get_username():
#     print("获取用户名")


def test_search():
    print("测试搜索功能")


def test_cart():
    print("测试购物车功能")


# @pytest.mark.usefixtures("login")
def test_order(login):
    print("测试订单功能")
    print(login)
