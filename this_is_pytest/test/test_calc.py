import sys
import pytest
import yaml

sys.path.append("..")


from ..dev.calculator import Calculator


# 读取 yml 文件中的数据
def get_datas(name):
    with open("../datas/calc.yml", encoding="utf-8") as f:
        all_datas = yaml.safe_load(f)
        datas = all_datas["datas"][name]
        ids = all_datas["ids"][name]
        return datas, ids


@pytest.fixture()
def get_instance():
    print("开始")
    calculator = Calculator()
    yield calculator
    print("结束")


@pytest.fixture(params=get_datas("add")[0], ids=get_datas("add")[1])
def get_datas_with_fixture(request):
    return request.param


class TestCalc:

    def test_add(self, get_instance, get_datas_with_fixture):
        data = get_datas_with_fixture
        assert get_instance.add(data[0], data[1]) == data[2]

    # 测试除法
    # @pytest.mark.parametrize("a, b, result", datas["div"]["datas"], ids=datas["div"]["ids"])
    # def test_div(self, get_instance, get_datas_with_fixture):
    #     data = get_datas_with_fixture
    #     assert get_instance.div(data[0], data[1]) == data[2]

    # # 测试除法，除数为 0 的情况
    # # @pytest.mark.parametrize("a, b, result", datas["div_error"]["datas"], ids=datas["div_error"]["ids"])
    # def test_div_error(self, get_instance, get_datas_with_fixture):
    #     # 使用 pytest 自带的异常捕获功能，捕获除数为 0 的异常
    #     with pytest.raises(ZeroDivisionError):
    #         data = get_datas_with_fixture["div_error"]
    #         print(data)
    #         # assert get_instance.div(data[0], data[1]) == data[2]





