import requests


class TestAddress:
    def setup(self):
        self.token = self.get_token()

    def get_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=xx")
        return r.json()["access_token"]

    # def test_create_user(self):
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
    #     data = {
    #             "userid": "zhangsan",
    #             "name": "张三",
    #             "mobile": "+86 13800111000",
    #             "department": 1
    #             }
    #     r = requests.post(url=url, json=data)
    #     print(r.json())

    def test_get_user(self):
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=zhangsan")
        print(r.json())