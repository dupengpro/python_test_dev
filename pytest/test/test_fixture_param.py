# fixture 参数化
import pytest


@pytest.fixture(params=["xiaoming", "xiaohong"])
def login(request):
    print("登录")
    # 返回参数，这里 request 也是一个 fixture
    return request.param


def test_login(login):
    name = login
    print(name + "登录")

