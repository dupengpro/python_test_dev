import yaml


def test_yaml():
    with open("../datas/calc.yml") as f:
        # 读取 yml 文件中的内容
        data = yaml.safe_load(f)
        print(type(data))
        print(data)