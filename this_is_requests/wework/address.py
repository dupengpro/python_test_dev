from this_is_requests.wework.base import Base


class Address(Base):
    def create_user(self, userid, name, mobile, department):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = self.send("POST", url=url, json=data)
        return r.json()

    def get_user(self, userid):
        r = self.send("GET", f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}")
        return r.json()

    def update_user(self, userid, name):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name,
        }
        r = self.send("POST", url=url, json=data)
        return r.json()

    def delete_user(self, userid):
        userid = userid
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        r = self.send("GET", url)
        return r.json()