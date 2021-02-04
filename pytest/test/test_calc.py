import sys
sys.path.append("..")


from ..dev.calculator import Calculator


class TestCalc:
    def test_add(self):
        calculator = Calculator()
        assert 2 == calculator.add(1, 1)

