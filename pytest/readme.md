# pytest

安装

`pip install pytest`



## sample

test_sample.py

```python
def inc(x):
    return x + 1


def test_answer():
    # 断言
    assert inc(1) == 2
```



## 执行测试

`pytest test_sample.py`

### 常用执行参数

- 执行当前目录下名称中包含“关键字”的 py 文件： `pytest -k "关键字"`

- 输出执行过程中打印的信息： `pytest test_sample.py -vs`

- 执行添加了标签的测试用例

    - 给测试用例添加标签 `@pytest.mark.标签名`

    -  把标签添加到配置文件中：

        - 新建文件：pytest.ini

        - 添加：

            ```ini
            [pytest]
            markers = 标签名
            ```

    - 执行 `pytest -m 标签名`



## setup, teardown

- setup_module , teardown_module
- setup_class, teardown_class
- setup_function, teardown_function
- setup , teardown



## 参数化

`@pytest.mark.parametrize(key, value)`

```python
@pytest.mark.parametrize("a, b, result", [[1, 1, 2], [1, 99, 100], [1, 0, 1]])
    def test_add(self, a, b, result):
        assert self.calculator.add(a, b) == result
```



## 数据驱动

可以使用 Json , yaml ，这里选择 yaml

安装 yaml

`pip install pyyaml`

新建 yaml 文件 test.yaml

```yaml
# [a, b , result]
#- a
#- b
#- result

# {a:1, b:2, result:3}
#a:
#  1
#b:
#  2
#result:
#  3

# [[1, 1, 2], [1, 99, 100], [1, 0, 1]]
#  - [1, 1, 2]
#  - [1, 99, 100]
#  - [1, 0, 1]

add:
  datas:
    - [ 1, 1, 2 ]
    - [ 1, 99, 100 ]
    - [ 1, 0, 1 ]
  # 说明/备注
  ids: ["case1", "case2", "case3"]
```

读取 yaml 文件

test_yaml.py

```python
import yaml


def test_yaml():
    with open("../datas/test.yml") as f:
        # 读取 yml 文件中的内容
        data = yaml.safe_load(f)
        print(type(data))
        print(data)
```

执行：`pytest test_yaml.py -vs`

执行结果：

```bash
test_yaml.py::test_yaml <class 'dict'>
{'add': {'datas': [[1, 1, 2], [1, 99, 100], [1, 0, 1]], 'ids': ['case1', 'case2', 'case3']}}
```



## 测试计算器

被测试的文件 calculator.py

```python
# 计算器
class Calculator:
  # 加法
    def add(self, a, b):
        return a + b
	# 除法
    def div(self, a, b):
        return a / b

```

Yaml 文件 calc.yml

```yaml
# 加法
add:
  datas:
    - [ 1, 1, 2 ]
    - [ 1, 99, 100 ]
    - [ 1, 0, 1 ]
  # 说明/备注
  ids: ["case1", "case2", "case3"]

# 除法
div:
  datas:
    - [10, 5, 2]
    - [9, 3, 3]
  ids: ["case1", "case2"]

# 除法，除数为0
div_error:
  datas:
    - [1, 0, 0]
  ids: ["ZeroDivisionError"]
```



测试文件 test_calc.py

```python
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

    # setup 在每个测试方法执行之前，执行一次
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


```

执行结果：

```bash
collected 6 items                                                                                                                                                                                                         

test_calc.py::TestCalc::test_add[case1] 我是 setup_class
我是 setup
PASSED我是 teardown

test_calc.py::TestCalc::test_add[case2] 我是 setup
PASSED我是 teardown

test_calc.py::TestCalc::test_add[case3] 我是 setup
PASSED我是 teardown

test_calc.py::TestCalc::test_div[case1] 我是 setup
PASSED我是 teardown

test_calc.py::TestCalc::test_div[case2] 我是 setup
PASSED我是 teardown

test_calc.py::TestCalc::test_div_error[ZeroDivisionError] 我是 setup
PASSED我是 teardown
我是 teardown_class

```



Pytest 提供的异常捕获功能

`with pytest raises`





