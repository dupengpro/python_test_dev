import sys
import pytest
import yaml

sys.path.append("..")


from ..dev.calculator import Calculator


# 读取 yml 文件中的数据
def get_datas():
    with open("../datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        return datas


class TestCalc:
    # 从 yml 文件中读取到的数据
    datas = get_datas()

    # setup_class 在类被调用的时候，在所有测试方法执行之前，执行一次
    def setup_class(self):
        print("我是 setup_class")
        self.calculator = Calculator()

    # setup 在每个测试方法被调用之前，执行一次
    def setup(self):
        print("我是 setup")
    # 测试加法，使用从 yml 文件中读取到的数据进行参数化 (key, values, 描述)
    @pytest.mark.parametrize("a, b, result", datas["add"]["datas"], ids=datas["add"]["ids"])
    def test_add(self, a, b, result):
        assert self.calculator.add(a, b) == result

    # 测试除法
    @pytest.mark.parametrize("a, b, result", datas["div"]["datas"], ids=datas["div"]["ids"])
    def test_div(self, a, b, result):
            assert self.calculator.div(a, b) == result

    # 测试除法，除数为 0 的情况
    @pytest.mark.parametrize("a, b, result", datas["div_error"]["datas"], ids=datas["div_error"]["ids"])
    def test_div_error(self, a, b, result):
        # 使用 pytest 自带的异常捕获功能，捕获除数为 0 的异常
        with pytest.raises(ZeroDivisionError):
            result = a / b

    # 在每个测试方法执行之后，执行一次
    def teardown(self):
        print("我是 teardown")

    # 在所有测试方法执行之后，执行一次
    def teardown_class(self):
        print("我是 teardown_class")



