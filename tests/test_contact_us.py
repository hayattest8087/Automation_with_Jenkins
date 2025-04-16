import pytest
from pages.contact_us_page import ContactUsPage

@pytest.mark.usefixtures("driver")
class TestContactUs:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.contact_page = ContactUsPage(self.driver)
        self.contact_page.go_to_contact_us_page()

    def test_submit_contact_form(self):
        self.contact_page.submit_contact_form(
            name="Test User",
            email="test@example.com",
            subject="Feedback",
            message="Great website!"
        )
