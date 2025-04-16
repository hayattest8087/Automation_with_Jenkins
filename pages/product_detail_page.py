from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_first_product_detail(self):
        self.driver.execute_script("window.scrollTo(0, 600);")
        view_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(text(),'View Product')])[1]")))
        view_btn.click()

    def verify_product_details(self):
     self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-information")))

     name = self.driver.find_element(By.XPATH, "//div[@class='product-information']//h2").text
     category = self.driver.find_element(By.XPATH, "//div[@class='product-information']//p").text
     price = self.driver.find_element(By.XPATH, "//div[@class='product-information']//span/span").text
     availability = self.driver.find_element(By.XPATH, "//div[@class='product-information']//b[normalize-space(text())='Availability:']/parent::p").text
     condition = self.driver.find_element(By.XPATH, "//div[@class='product-information']//b[normalize-space(text())='Condition:']/parent::p").text
     brand = self.driver.find_element(By.XPATH, "//div[@class='product-information']//b[normalize-space(text())='Brand:']/parent::p").text

     return {
        "name": name.strip(),
        "category": category.strip(),
        "price": price.strip(),
        "availability": availability.strip(),
        "condition": condition.strip(),
        "brand": brand.strip()
    }

