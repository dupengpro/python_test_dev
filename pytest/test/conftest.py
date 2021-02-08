from typing import List

import pytest


@pytest.fixture()
def login():
    print("登录")
    message = "我是 message"
    yield message
    print("登出")

def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)