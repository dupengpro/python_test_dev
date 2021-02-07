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
    
- 显示 fixture 的执行过程 `--setupshow`



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



## Fixture



Fixture 的功能类似于 setup, teardown ，前者比后者更灵活。

比如测试搜索和购物车功能不需要登录，测试订单功能需要登录：

test_fixture.py

```python
import pytest


# 给 login 函数添加 fixture
@pytest.fixture()
def login():
    print("登录")


def test_search():
    print("测试搜索功能")


def test_cart():
    print("测试购物车功能")


# 测试订单功能需要登录，把 login 函数作为参数传递进来
def test_order(login):
    print("测试订单功能")

```

查看 fixture 的执行过程：`pytest test_fixture --setupshow` 

执行结果：

```bash
collected 3 items                                                                                                                                                                                                         

test_fixture.py 
        test_fixture.py::test_search.
        test_fixture.py::test_cart.
        SETUP    F login
        test_fixture.py::test_order (fixtures used: login).
        TEARDOWN F login
```

Fixture 的执行过程显示：会在执行测试订单功能之前和之后各执行一次登陆功能。

除了作为参数传递，还可以通过装饰器 `@pytest.mark.usefixtures` 调用：

```python
@pytest.mark.usefixtures("login")
def test_order():
    print("测试订单功能")
```

### 添加多个 fixture

```python
import pytest


# 给 login 函数添加 fixture
@pytest.fixture()
def login():
    print("登录")


@pytest.fixture()
def get_username():
    print("获取用户名")


def test_search():
    print("测试搜索功能")


def test_cart():
    print("测试购物车功能")


# 通过 usefixtures 调用 fixture
@pytest.mark.usefixtures("get_username")
@pytest.mark.usefixtures("login")
def test_order():
    print("测试订单功能")

```

执行测试：`pytest test_fixture -vs`

执行结果：

```bash
collected 3 items                                                                                                                                                                                                         

test_fixture.py::test_search 测试搜索功能
PASSED
test_fixture.py::test_cart 测试购物车功能
PASSED
test_fixture.py::test_order 登录
获取用户名
测试订单功能
PASSED
```

执行结果显示会先调用 login 再调用 get_username



`@pytest.fixture(autouse=True)` 

如果设置了 `autouse=True` 那么所有的测试方法都会调用该 fixture 

```python
@pytest.fixture(autouse=True)
def login():
    print("登录")

......
```

执行结果：

```bash
collected 3 items                                                                                                                                                                                                         

test_fixture.py::test_search 登录
测试搜索功能
PASSED
test_fixture.py::test_cart 登录
测试购物车功能
PASSED
test_fixture.py::test_order 登录
获取用户名
测试订单功能
PASSED
```



### fixture 调用 fixture

```python
@pytest.fixture()
def login():
    print("登录")

# fixture get_username 调用 fixture login
@pytest.fixture()
def get_username(login):
    print("获取用户名")

......

# 这里通过 usefixtures 只调用 get_username，不调用 login
@pytest.mark.usefixtures("get_username")
def test_order():
    print("测试订单功能")
```

执行结果：

```bash
collected 3 items                                                                                                                                                                                                         

test_fixture.py::test_search 测试搜索功能
PASSED
test_fixture.py::test_cart 测试购物车功能
PASSED
test_fixture.py::test_order 登录
获取用户名
测试订单功能
PASSED
```

执行结果显示在调用 get_username 之前，先调用了 login



### fixture 的 yield

执行测试方法之前，执行 `yield` 之前的部分，执行测试方法之后，执行 `yield` 之后的部分

```python
@pytest.fixture()
def login():
    print("登录")
    yield
    print("登出")
......
```

执行结果：

```bash
collected 3 items                                                                                                                                                                                                         

test_fixture.py::test_search 测试搜索功能
PASSED
test_fixture.py::test_cart 测试购物车功能
PASSED
test_fixture.py::test_order 登录
获取用户名
测试订单功能
PASSED登出
```

使用 `yield` 返回信息

```python
......
# 给 login 函数添加 fixture
@pytest.fixture()
def login():
    print("登录")
    message = "我是 message"
    yield message
    print("登出")

......
# 此时只能通过传参的方式调用 fixture
def test_order(login):
    print("测试订单功能")
    print(login)
```

执行结果：

```bash
collected 3 items                                                                                                                                                                                                         

test_fixture.py::test_search 测试搜索功能
PASSED
test_fixture.py::test_cart 测试购物车功能
PASSED
test_fixture.py::test_order 登录
测试订单功能
我是 message
PASSED登出
```

注意，这里只能通过传参的方式调用 fixture ，不然 `print(login)` 输出的是 `login` 这个函数的对象。



### scope

`scope` 用来设置 fixture 的作用域，类似于 setup, teardown 的 module, class, function, method 这种

`scope` 的作用域有：函数（默认），类，模块，session 

> "function" (default), "class", "module", "session" or "invocation".

- session
- 模块
- 类
- 函数



### conftest 模块

这个模块里面可以添加一些自定义的功能，在当前目录下的所有模块都可以共用这些自定义的功能。可以把常用的 `fixture` 放在这里。使用了 `conftest` 中的功能的模块，在执行的时候，会在当前目录下找 `conftest` 模块，如果当前目录下没有找到 `conftest` 模块，会向上一级目录查找...

新建 conftest.py （文件名固定，不能修改）

```python
import pytest


@pytest.fixture()
def login():
    print("登录")
    message = "我是 message"
    yield message
    print("登出")
```

test_fixture.py 只保留以下内容：

```python
def test_search():
    print("测试搜索功能")


def test_cart():
    print("测试购物车功能")


def test_order(login):
    print("测试订单功能")
    print(login)
```

执行：`pytest test_fixture.py -vs`

执行结果：

```bash
collected 3 items                                                                                                                                                                                                         

test_fixture.py::test_search 测试搜索功能
PASSED
test_fixture.py::test_cart 测试购物车功能
PASSED
test_fixture.py::test_order 登录
测试订单功能
我是 message
PASSED登出
```

可以看到，test_fixture.py 文件中不需要导入任何模块，就可以执行成功。

