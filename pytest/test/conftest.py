import pytest


@pytest.fixture()
def login():
    print("登录")
    message = "我是 message"
    yield message
    print("登出")