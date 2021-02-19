# 官方例子
import pytest


@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a():
    # a 失败
    assert False


@pytest.mark.dependency()
def test_b():
    pass


@pytest.mark.dependency(depends=["test_a"])
def test_c():
    # c 依赖 a ，a 失败了，所以 c 不会执行
    pass


@pytest.mark.dependency(depends=["test_b"])
def test_d():
    # d 依赖 b
    pass


@pytest.mark.dependency(depends=["test_b", "test_c"])
def test_e():
    # e 依赖 b 和 c ， c 不会执行，e 会不会执行呢？
    pass