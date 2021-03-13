from this_is_appium.apppo.page.app import App


class TestContact:
    def setup(self):
        self.app = App().start()
        self.main = App().goto_main()

    def test_addcontact(self):
        editpage = self.main.goto_addresslist().click_addcontact().addcontact_menual()
        editpage.edit_contact(name, phonenum)
        editpage.verify_ok()

    def tesrdown(self):
        self.app.stop()