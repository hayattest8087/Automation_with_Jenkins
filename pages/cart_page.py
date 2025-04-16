from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_product_to_cart(self):
        # Scroll to product and click "Add to cart"
        self.driver.execute_script("window.scrollTo(0, 600);")
        add_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'Add to cart')])[1]")))
        add_btn.click()

        # Wait for modal and click "View Cart"
        view_cart_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//u[contains(text(),'View Cart')]")))
        view_cart_btn.click()

    def is_product_added_to_cart(self):
        # Verify product table appears
        return self.wait.until(EC.presence_of_element_located((By.XPATH, "//section[@id='cart_items']//tr"))).is_displayed()
