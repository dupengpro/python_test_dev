import allure


def test_no_severity():
    pass


@allure.severity(allure.severity_level.BLOCKER)
def test_blocker_severity():
    pass


@allure.severity(allure.severity_level.CRITICAL)
def test_critical_severity():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_normal_severity():
    pass


@allure.severity(allure.severity_level.MINOR)
def test_minor_severity():
    pass


@allure.severity(allure.severity_level.TRIVIAL)
class TestSeverity:
    def test_case1(self):
        pass

    @allure.severity(allure.severity_level.NORMAL)
    def test_case2(self):
        pass