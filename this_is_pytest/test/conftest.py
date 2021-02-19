from typing import List

import pytest


@pytest.fixture()
def login():
    print("登录")
    message = "我是 message"
    yield message
    print("登出")


# 这个 hook 函数会收集所有测试用例
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 这里的 items 是测试用例列表

    # 对测试用例进行中文编码设置
    for item in items:
        # item.name 是测试用例的名称
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        # item._nodeid 是测试用例的路径
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")

        # 给测试用例加标签
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)

    # 反转测试用例列表的顺序
    items.reverse()