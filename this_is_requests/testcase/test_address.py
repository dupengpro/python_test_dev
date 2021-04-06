from this_is_requests.wework.address import Address


class TestAddress:
    def setup_class(self):
        self.address = Address()
        self.user_id = "zhangsan"
        self.name = "张三"
        self.mobile = "13012345678"
        self.department = [1]

    def setup(self):
        self.address.delete_user(self.user_id)

    def test_create_user(self):
        r = self.address.create_user(self.user_id, self.name, self.mobile, self.department)
        assert r['errcode'] == 0
        assert r['errmsg'] == 'created'

    def test_get_user(self):
        self.address.create_user(self.user_id, self.name, self.mobile, self.department)
        r = self.address.get_user(self.user_id)
        assert r['errmsg'] == 'ok'
        assert r['name'] == self.name

    def test_update_user(self):
        self.address.create_user(self.user_id, self.name, self.mobile, self.department)
        new_name = "小明"
        r = self.address.update_user(self.user_id, new_name)
        assert r['errmsg'] == 'updated'
        r1 = self.address.get_user(self.user_id)
        assert r1['name'] == new_name

    def test_delete_user(self):
        self.address.create_user(self.user_id, self.name, self.mobile, self.department)
        r = self.address.delete_user(self.user_id)
        assert r['errmsg'] == 'deleted'
        r1 = self.address.get_user(self.user_id)
        assert r1['errcode'] == 60111

    def teardown(self):
        self.address.delete_user(self.user_id)
