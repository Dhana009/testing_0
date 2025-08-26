import allure

def test_pass():
    with allure.step("pass"):
        assert True
