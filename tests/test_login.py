import pytest
from pages.login_page import LoginPage
from utils.common import take_screenshot

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login(self):
        try:
            login_page = LoginPage(self.driver)
            login_page.login("testhayat@yopmail.com", "12345678")
            
            # Add your assertion
            assert "Logged in" in self.driver.page_source

        except AssertionError as e:
            take_screenshot(self.driver, "login_failure")
            raise e  # re-raise so the test still fails
