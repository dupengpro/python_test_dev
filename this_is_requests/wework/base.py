import requests


class Base:
    def __init__(self):
        self.session = requests.Session()
        self.token = self.get_token()
        # 把 token 加入 session ，就不用每次请求都添加 token 参数
        self.session.params = {"access_token": self.token}

    def get_token(self):
        r = self.session.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=xx")
        return r.json()["access_token"]

    def send(self, *args, **kwargs):
        return self.session.request(*args, **kwargs)