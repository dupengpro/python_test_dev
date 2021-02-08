import pytest


@pytest.mark.flaky(reruns=5, reruns_delay=1)
def test_rerun():
    assert 1 == 2

