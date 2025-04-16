import pytest
from pages.product_detail_page import ProductDetailPage

@pytest.mark.usefixtures("driver")
class TestProductDetail:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.product_detail = ProductDetailPage(driver)

    def test_product_detail_page(self):
        self.product_detail.open_first_product_detail()
        details = self.product_detail.verify_product_details()

        assert details["name"] != "", "Product name is empty"
        assert "Category" in details["category"], "Category is missing"
        assert "Rs." in details["price"], "Price is not displayed"
        assert "In Stock" in details["availability"], "Availability info missing"
        assert details["condition"] != "", "Condition info missing"
        assert details["brand"] != "", "Brand info missing"
