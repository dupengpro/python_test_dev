import pytest


@pytest.mark.parametrize("name", ["小明", "小红"])
def test_encode(name):
    print(name)

