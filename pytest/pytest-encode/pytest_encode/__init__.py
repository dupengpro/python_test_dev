from typing import List


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