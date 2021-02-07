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

- 执行当前目录下名称中包含“关键字”的 py 文件 `pytest -k "关键字"`

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

`@pytest.mark.parametrize`











