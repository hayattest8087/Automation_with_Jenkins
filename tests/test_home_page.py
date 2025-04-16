import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("driver")
class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.home_page = HomePage(self.driver)

    def test_home_page_load(self):
        assert self.home_page is not None, "HomePage is not initialized"
        self.home_page.verify_home_page_elements()
