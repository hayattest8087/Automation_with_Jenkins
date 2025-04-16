import pytest
from pages.cart_page import CartPage

@pytest.mark.usefixtures("driver")
class TestCart:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.cart_page = CartPage(driver)

    def test_add_product_to_cart(self):
        self.cart_page.add_first_product_to_cart()
        assert self.cart_page.is_product_added_to_cart(), "Product not added to cart"
