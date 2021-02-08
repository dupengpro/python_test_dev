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

`conftest` 所在的目录必须是一个包（有 `__init__.py` 文件）

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



使用 fixture 替换测试计算机模块中的 setup 和 teardown

test_calc.py

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

# 添加 fixture 替换 setup 和 teardown
@pytest.fixture()
def get_instance():
    print("开始")
    calculator = Calculator()
    yield calculator
    print("结束")



class TestCalc:
    # 从 yml 文件中读取到的数据
    datas = get_datas()

    # 通过传参的方式调用 get_instance
    @pytest.mark.parametrize("a, b, result", datas["add"]["datas"], ids=datas["add"]["ids"])
    def test_add(self, a, b, result, get_instance):
        assert get_instance.add(a, b) == result

    # 通过传参的方式调用 get_instance
    @pytest.mark.parametrize("a, b, result", datas["div"]["datas"], ids=datas["div"]["ids"])
    def test_div(self, a, b, result, get_instance):
            assert get_instance.div(a, b) == result

    # 测试除法，除数为 0 的情况
    @pytest.mark.parametrize("a, b, result", datas["div_error"]["datas"], ids=datas["div_error"]["ids"])
    def test_div_error(self, a, b, result):
        # 使用 pytest 自带的异常捕获功能，捕获除数为 0 的异常
        with pytest.raises(ZeroDivisionError):
            result = a / b

```

执行：`pytest test_calc.py -vs`

执行结果：

```bash
collected 6 items                                                                                                                                                                                                         

test_calc.py::TestCalc::test_add[case1] 开始
PASSED结束

test_calc.py::TestCalc::test_add[case2] 开始
PASSED结束

test_calc.py::TestCalc::test_add[case3] 开始
PASSED结束

test_calc.py::TestCalc::test_div[case1] 开始
PASSED结束

test_calc.py::TestCalc::test_div[case2] 开始
PASSED结束

test_calc.py::TestCalc::test_div_error[ZeroDivisionError] PASSED
```



### fixture 参数化

test_fixture_param.py

```python
# fixture 参数化
import pytest


@pytest.fixture(params=["xiaoming", "xiaohong"])
def login(request):
    print("登录")
    # 返回参数，这里 request 也是一个 fixture
    return request.param


def test_login(login):
    name = login
    print(name + "登录")
```



执行：`pytest test_fixture_param.py -vs`

执行结果：

```bash
collected 2 items                                                                                                                                                                                                         

test_fixture_param.py::test_login[xiaoming] 登录
xiaoming登录
PASSED
test_fixture_param.py::test_login[xiaohong] 登录
xiaohong登录
PASSED
```





## 常用插件

### 失败用例重新运行

pytest-rerunfailures

安装 `pip install pytest-rerunfailures`

test_rerun.py

```python
def test_rerun():
    assert 1 == 2
```

重新运行 5 次，执行：`pytest test_rerun.py -vs --reruns 5`

执行结果：

```bash
collected 1 item                                                                                                                                                                                                          

test_rerun.py::test_rerun RERUN
test_rerun.py::test_rerun RERUN
test_rerun.py::test_rerun RERUN
test_rerun.py::test_rerun RERUN
test_rerun.py::test_rerun RERUN
test_rerun.py::test_rerun FAILED
```

重新运行 5 次，每次之间间隔 1 秒钟：

- 方式一，执行：`pytest test_rerun.py -vs --reruns 5 --reruns-delay 1`

- 方式二，使用装饰器：

  ```python
  import pytest
  
  
  @pytest.mark.flaky(reruns=5, reruns_delay=1)
  def test_rerun():
      assert 1 == 2
  ```

  

### 控制执行顺序

pytest-ordering

安装 `pip install pytest-ordering`

使用前：test_order.py

```python
def test_foo():
    assert True


def test_bar():
    assert True
```

执行：`pytest test_order.py -vs`

执行结果：

```bash
collected 2 items                                                                                                                                                                                                         

test_order.py::test_foo PASSED
test_order.py::test_bar PASSED
```

使用后：test_order.py

```python
import pytest


@pytest.mark.run(order=2)
def test_foo():
    assert True


@pytest.mark.run(order=1)
def test_bar():
    assert True
```

执行结果：

```bash
collected 2 items                                                                                                                                                                                                         

test_order.py::test_bar PASSED
test_order.py::test_foo PASSED
```

通过对比执行结果可以看到，使用前是按照从上到下的顺序执行的，使用后是按照 `order` 的值由小到大执行的。

 

### 用例依赖

pytest-dependency

设置用例之间的依赖关系，

安装 `pip install pytest-dependency`

添加依赖：`@pytest.mark.dependency()`

test_dependency.py

```python
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
```

执行：`pytest test_dependency.py -vs`

执行结果：

```bash
collected 5 items                                                                                                                                                                                                         

test_dependency.py::test_a XFAIL (deliberate fail)
test_dependency.py::test_b PASSED
test_dependency.py::test_c SKIPPED (test_c depends on test_a)
test_dependency.py::test_d PASSED
test_dependency.py::test_e SKIPPED (test_e depends on test_c)
```

通过执行结果可以看到 c 和 e 都跳过了，没有执行。



### 并发执行

pytest-xdist

安装： `pip install pytest-xdist`

使用：

- `pytest -n number` 用 number 指定线程数

- `pytest -n auto` 自动分配线程数

test_xdist.py

```python
import time


def test_1():
    time.sleep(3)
    print(1)


def test_2():
    time.sleep(3)
    print(2)


def test_3():
    time.sleep(3)
    print(3)
```

使用前，执行：`pytest test_xdist.py -vs`

执行结果：

```bash
collected 3 items                                                                                                                                                                                                         

test_xdist.py::test_1 1
PASSED
test_xdist.py::test_2 2
PASSED
test_xdist.py::test_3 3
PASSED

3 passed in 9.02s 
```

使用后，执行：`pytest test_xdist.py -vs -n auto`

执行结果：

```bash
[gw0] PASSED test_xdist.py::test_1 
[gw2] PASSED test_xdist.py::test_3 
[gw1] PASSED test_xdist.py::test_2 

3 passed in 4.10s 
```

对比使用前后的执行结果，可以看到使用后的执行用时缩短了近 5 秒钟。



## hook 函数

`/venv/lib/python3.9/site-packages/_pytest/hookspec.py` 

自己写的 `hook` 函数，可以放在 `conftest` 模块中

修改 `pytest_collection_modifyitems`

