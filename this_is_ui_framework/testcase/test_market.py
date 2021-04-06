import sys

from this_is_ui_framework.page.logger import log_init

sys.path.append("..")
from this_is_ui_framework.page.app import App


class Market:
    def setup(self):
        self.app = App()

    def test_goto_market(self):
        self.app.start().goto_main().goto_market().goto_search().search()