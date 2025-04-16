import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
class TestLogout:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)
        self.login_page.go_to_login_page()
        self.login_page.login("testhayat@yopmail.com", "12345678")

    def test_logout(self):
        self.login_page.logout()
        assert self.login_page.is_logout_successful(), "Logout failed!"
