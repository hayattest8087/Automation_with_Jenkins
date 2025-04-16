from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_home_page_elements(self):
        header = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        footer = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        assert header.is_displayed(), "Header not displayed"
        assert footer.is_displayed(), "Footer not displayed"
