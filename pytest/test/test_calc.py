import sys

import pytest

sys.path.append("..")


from ..dev.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print("开始")
        self.calculator = Calculator()

    @pytest.mark.parametrize("a, b, result", [[1, 1, 2], [1, 99, 100], [1, 0, 1]])
    def test_add(self, a, b,result):
        assert self.calculator.add(a, b) == result

    def test_div(self):
        assert self.calculator.div(9, 3) == 3

    def teardown_class(self):
        print("结束")



