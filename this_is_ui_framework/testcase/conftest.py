import os
import signal
import subprocess

import pytest

from this_is_ui_framework.page.logger import log_init


@pytest.fixture(scope='module', autouse=True)
def record():
    # 用例运行前
    log_init()
    # 录屏
    cmd = 'scrcpy -Nr tmp.mp4'
    p = subprocess.Popen(cmd, shell=True)
    yield
    # 用例运行后
    # 把 CTRL C 传给 pid
    os.kill(p.pid, signal.CTRL_C_EVENT)
